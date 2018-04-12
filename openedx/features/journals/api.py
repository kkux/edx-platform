"""
APIs providing support for Journals functionality.
"""
import logging
import hashlib
import json
from urlparse import urlsplit, urlunsplit
import six

from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from edx_rest_api_client.client import EdxRestApiClient
from openedx.core.djangoapps.catalog.models import CatalogIntegration
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.lib.token_utils import JwtBuilder
from slumber.exceptions import HttpClientError, HttpNotFoundError, HttpServerError


LOGGER = logging.getLogger("edx.journals")
JOURNALS_CACHE_TIMEOUT = 3600  # Value is in seconds
JOURNALS_API_PATH = '/journal/api/v1/'
# TODO move this to settings
JOURNALS_API_URL = 'http://journals.app:18606/api/v1/'


class DiscoveryApiClient(object):
    """
    Class for interacting with the discovery service journals endpoint
    """
    def __init__(self, user):
        """
        Initialize an authenticated Enterprise service API client by using the
        provided user.
        """
        self.user = user
        jwt = JwtBuilder(user).build_token([])
        url = configuration_helpers.get_value('COURSE_CATALOG_API_URL', settings.COURSE_CATALOG_API_URL)
        self.client = EdxRestApiClient(self.create_journals_url(url), jwt=jwt)

    def create_journals_url(self, url):
        '''rewrite the discovery url to point to journals endpoint'''
        split_url = urlsplit(url)
        override_url = urlunsplit((
            split_url.scheme,
            split_url.netloc,
            JOURNALS_API_PATH,
            split_url.query,
            split_url.fragment,
        ))
        return override_url

    def get_journals(self, partner, org):
        # TODO filter on partner/org
        try:
            response = self.client.journals.get()
            LOGGER.info('response is type=%s', type(response))
            return response.get('results')
        except (HttpClientError, HttpServerError) as err:
            LOGGER.exception(
                'Failed to get journals from discovery-service [%s]',
                err.content
            )
            return []


class JournalsApiClient(object):
    """
    Class for interacting with the Journals Service
    """
    def __init__(self, user):
        """
        Initialize an authenticated Enterprise service API client by using the
        provided user.
        """
        self.user = user
        jwt = JwtBuilder(user).build_token([])
        self.client = EdxRestApiClient(
            configuration_helpers.get_value('JOURNALS_API_URL', JOURNALS_API_URL),
            jwt=jwt
        )


def get_cache_key(**kwargs):
    """
    Get MD5 encoded cache key for given arguments.

    Here is the format of key before MD5 encryption.
        key1:value1__key2:value2 ...

    Example:
        >>> get_cache_key(site_domain="example.com", resource="enterprise-learner")
        # Here is key format for above call
        # "site_domain:example.com__resource:enterprise-learner"
        a54349175618ff1659dee0978e3149ca

    Arguments:
        **kwargs: Key word arguments that need to be present in cache key.

    Returns:
         An MD5 encoded key uniquely identified by the key word arguments.
    """
    key = '__'.join(['{}:{}'.format(item, value) for item, value in six.iteritems(kwargs)])

    return hashlib.md5(key).hexdigest()


def journals_enabled():
    """
    Determines whether the Journals app is installed and enabled
    """
    return 'openedx.features.journals.apps.JournalsConfig' in settings.INSTALLED_APPS and settings.FEATURES.get('ENABLE_JOURNAL_INTEGRATION', False)


def get_journals(site, partner=None, org=None):
    """Retrieve journals from the discovery service.

    Keyword Arguments:
        name (string): Name identifying a specific program.

    Returns:
        list of dict, representing journal types.
        dict, if a specific journal type is requested.
    """
    if not journals_enabled():
        return []

    api_resource = 'journals'

    cache_key = get_cache_key(
        site_domain=site.domain,
        resource=api_resource,
        partner=partner,
        org=org
    )

    # look up in cache
    journals = cache.get(cache_key)

    if not journals:
        catalog_integration = CatalogIntegration.current()
        if catalog_integration.enabled:
            try:
                user = catalog_integration.get_service_user()
            except ObjectDoesNotExist:
                return []

            api_client = DiscoveryApiClient(user)
            journals = api_client.get_journals(partner, org)
            LOGGER.info('found journals=%s', journals)
            cache.set(cache_key, journals, JOURNALS_CACHE_TIMEOUT)
        else:
            return []

    return journals
