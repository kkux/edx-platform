"""
Image encoding helpers for the verification app.
"""
import logging
import boto3
from django.conf import settings


log = logging.getLogger(__name__)


class InvalidImageData(Exception):
    """
    The provided image data could not be decoded.
    """
    pass


def decode_image_data(data):
    """
    Decode base64-encoded image data.

    Arguments:
        data (str): The raw image data, base64-encoded.

    Returns:
        str

    Raises:
        InvalidImageData: The image data could not be decoded.

    """
    try:
        return (data.split(",")[1]).decode("base64")
    except (IndexError, UnicodeEncodeError):
        log.exception("Could not decode image data")
        raise InvalidImageData


def get_image_url(sspv, image_type):

    config = settings.VERIFY_STUDENT['SOFTWARE_SECURE']
    try:
        conn = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        location = config['STORAGE_KWARGS']['location'] + image_type
        image_url = conn.generate_presigned_url(
            'get_object',
            Params = {
                'Bucket': config['STORAGE_KWARGS']['bucket'],
                'Key': location + sspv.receipt_id
            },
            ExpiresIn = 100
        )
    except:
        image_url = 'https://cdn.browshot.com/static/images/not-found.png'
    return image_url

