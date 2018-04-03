"""
Test user retirement methods
"""
import json

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
import pytest

from student.models import (
    get_all_retired_emails_by_email,
    get_all_retired_usernames_by_username,
    get_potentially_retired_user_by_username_and_hash,
    get_retired_email_by_email,
    get_retired_username_by_username,
    is_username_retired
)
from student.helpers import (
    RETIRED_USERNAME_START,
    RETIRED_USERNAME_END,
    RETIRED_EMAIL_START,
    RETIRED_EMAIL_END
)
from student.tests.factories import UserFactory


# Tell pytest it's ok to user the Django db
pytestmark = pytest.mark.django_db

# Make sure our settings are sane
assert "{}" in settings.RETIRED_USERNAME_FMT
assert "{}" in settings.RETIRED_EMAIL_FMT


def check_username_against_fmt(hashed_username):
    """
    Checks that the given username is formatted correctly using
    our settings. The format string may put the hashed string
    anywhere, and the hasher is opaque, so this just looks for
    our surrounding strings, if they exist.
    """
    assert len(hashed_username) > len(settings.RETIRED_USERNAME_FMT)

    if RETIRED_USERNAME_START:
        assert hashed_username.startswith(RETIRED_USERNAME_START)
    if RETIRED_USERNAME_END:
        assert hashed_username.endswith(RETIRED_USERNAME_END)


def check_email_against_fmt(hashed_email):
    """
    Checks that the given email is formatted correctly using
    our settings. The format string may put the hashed string
    anywhere, and the hasher is opaque, so this just looks for
    our surrounding strings, if they exist.
    """
    assert len(hashed_email) > len(settings.RETIRED_EMAIL_FMT)

    if RETIRED_EMAIL_START:
        assert hashed_email.startswith(RETIRED_EMAIL_START)
    if RETIRED_EMAIL_END:
        assert hashed_email.endswith(RETIRED_EMAIL_END)


def test_get_retired_username():
    """
    Basic testing of getting retired usernames. The hasher is opaque
    to us, we just care that it's succeeding and using our format.
    """
    user = UserFactory()
    hashed_username = get_retired_username_by_username(user.username)
    check_username_against_fmt(hashed_username)


def test_get_all_retired_usernames_by_username():
    """
    Check that all salts are used for this method and return expected
    formats.
    """
    user = UserFactory()
    hashed_usernames = list(get_all_retired_usernames_by_username(user.username))
    assert len(hashed_usernames) == len(settings.RETIRED_USER_SALTS)

    for hashed_username in hashed_usernames:
        check_username_against_fmt(hashed_username)

    # Make sure hashes are unique
    assert len(hashed_usernames) == len(set(hashed_usernames))


def test_is_username_retired_is_retired():
    """
    Check functionality of is_username_retired when username is retired
    """
    user = UserFactory()
    original_username = user.username
    retired_username = get_retired_username_by_username(user.username)

    # Fake username retirement.
    user.username = retired_username
    user.save()

    assert is_username_retired(original_username)


def test_is_username_retired_not_retired():
    """
    Check functionality of is_username_retired when username is not retired
    """
    user = UserFactory()
    assert not is_username_retired(user.username)


def test_get_retired_email():
    """
    Basic testing of retired emails.
    """
    user = UserFactory()
    hashed_email = get_retired_email_by_email(user.email)
    check_email_against_fmt(hashed_email)


def test_get_all_retired_email_by_email():
    """
    Check that all salts are used for this method and return expected
    formats.
    """
    user = UserFactory()
    hashed_emails = list(get_all_retired_emails_by_email(user.email))
    assert len(hashed_emails) == len(settings.RETIRED_USER_SALTS)

    for hashed_email in hashed_emails:
        check_email_against_fmt(hashed_email)

    # Make sure hashes are unique
    assert len(hashed_emails) == len(set(hashed_emails))


def test_get_potentially_retired_user_username_match():
    """
    Check that we can pass in an un-retired username and get the
    user-to-be-retired back.
    """
    user = UserFactory()
    hashed_username = get_retired_username_by_username(user.username)
    assert get_potentially_retired_user_by_username_and_hash(user.username, hashed_username) == user


def test_get_potentially_retired_user_hashed_match():
    """
    Check that we can pass in a hashed username and get the
    user-to-be-retired back.
    """
    user = UserFactory()
    orig_username = user.username
    hashed_username = get_retired_username_by_username(orig_username)

    # Fake username retirement.
    user.username = hashed_username
    user.save()

    # Check to find the user by original username should fail,
    # 2nd check by hashed username should succeed.
    assert get_potentially_retired_user_by_username_and_hash(orig_username, hashed_username) == user


def test_get_potentially_retired_user_does_not_exist():
    """
    Check that the call to get a user with a non-existent
    username and hashed username bubbles up User.DoesNotExist
    """
    fake_username = "fake username"
    hashed_username = get_retired_username_by_username(fake_username)

    with pytest.raises(User.DoesNotExist):
        get_potentially_retired_user_by_username_and_hash(fake_username, hashed_username)


def test_get_potentially_retired_user_bad_hash():
    """
    Check that the call will raise an exeption if the given hash
    of the username doesn't match any salted hashes the system
    knows about.
    """
    fake_username = "fake username"

    with pytest.raises(Exception):
        get_potentially_retired_user_by_username_and_hash(fake_username, "bad hash")


class TestRegisterRetiredUsername(TestCase):
    """
    Tests to ensure that retired usernames can no longer be used in registering new accounts.
    """
    def setUp(self):
        super(TestRegisterRetiredUsername, self).setUp()
        self.url = reverse('create_account')
        self.url_params = {
            'username': 'username',
            'email': 'foo_bar' + '@bar.com',
            'name': 'foo bar',
            'password': '123',
            'terms_of_service': 'true',
            'honor_code': 'true',
        }

    def _validate_exiting_username_response(self, orig_username, response):
        """
        Validates a response stating that a username already exists.
        """
        assert response.status_code == 400
        obj = json.loads(response.content)
        assert obj['value'].startswith('An account with the Public Username')
        assert obj['value'].endswith('already exists.')
        assert orig_username in obj['value']
        assert obj['field'] == 'username'
        assert not obj['success']

    def test_retired_username(self):
        """
        Ensure that a retired username cannot be registered again.
        """
        user = UserFactory()
        orig_username = user.username

        # Fake retirement of the username.
        user.username = get_retired_username_by_username(orig_username)
        user.save()

        # Attempt to create another account with the same username that's been retired.
        self.url_params['username'] = orig_username
        response = self.client.post(self.url, self.url_params)
        self._validate_exiting_username_response(orig_username, response)

    def test_username_close_to_retired_format(self):
        """
        Ensure that a username similar to the format of a retired username cannot be created.
        """
        # Attempt to create an account with a username similar to the format of a retired username.
        self.url_params['username'] = RETIRED_USERNAME_START
        response = self.client.post(self.url, self.url_params)
        self._validate_exiting_username_response(RETIRED_USERNAME_START, response)
