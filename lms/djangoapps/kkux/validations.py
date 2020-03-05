import os

from django.core.exceptions import ValidationError



def image_validations(value):
    """
    For Image Validation
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported Image extension')
    if value.height < 125 or value.width < 125:
        raise ValidationError('Too Low Resolution')
    ratio = value.width / float(value.height)
    image_size = value.size / 1024
    max_limit = 5
    max_upload_limit = max_limit * 1024

    if int(image_size) > max_upload_limit:
        raise ValidationError('Image Size must be less than %s MB' % max_limit)