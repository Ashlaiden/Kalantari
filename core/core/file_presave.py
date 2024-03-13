from os.path import basename, splitext
import random
import inspect
from django.db import models


def get_filename_ext(filepath):
    base_name = basename(filepath)
    name, ext = splitext(base_name)
    return name, ext


def get_sender(instance):
    model_name = instance._meta.model_name
    name = str(model_name).lower()
    if name == 'product':
        return 'product'
    elif name == 'productgallery':
        return 'productgallery'
    elif name == 'socialmedia':
        return 'socialmedia'
    elif name == 'sitesetting':
        return 'sitesetting'


def get_sender_field_name():
    # Inspect the stack to find out who is calling the function
    stack = inspect.stack()
    # Look for the 'field' attribute in the stack frames
    for frame_record in stack:
        frame = frame_record.frame
        local_vars = frame.f_locals
        for var_name, var_value in local_vars.items():
            if hasattr(var_value, 'field') and isinstance(var_value.field, models.ImageField):
                return var_value.field.name
    return None


def upload_image_path(instance, filename):
    sender = get_sender(instance)
    new_name = random.randint(8765, 27564231864)
    name, ext = get_filename_ext(filename)
    final_name = f'{instance.id}--[{instance.title}]--{new_name}{ext}'
    if sender == 'product':
        field_name = get_sender_field_name()
        if field_name == 'cover_image':
            return f'products/{instance.id}/cover-{final_name}'
        elif field_name == 'hover_image':
            return f'products/{instance.id}/hover-{final_name}'
        else:
            return f'products/{instance.id}/{final_name}'
    elif sender == 'productgallery':
        return f'products/{instance.product_id}/gallery-{final_name}'
    elif sender == 'socialmedia':
        return f'settings/social_media/socialmedia-{final_name}'
    elif sender == 'sitesetting':
        return f'settings/site_setting/{instance.id}/setting-{final_name}'


