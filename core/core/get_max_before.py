from django.db import models
# from shop_settings.models import FooterTableHead, FooterTableRow


# def get_sender(instance):
#     model_name = instance._meta.model_name
#     name = str(model_name).lower()
#     if name == 'productslider':
#         return 'slider'
#     elif name == 'product':
#         return 'product'
#     elif name == 'productgallery':
#         return 'productgallery'
#     elif name == 'sitesettings':
#         return 'sitesettings'
#     elif name == 'socialmedia':
#         return 'socialmedia'

def get_max_plus_one(instance, attr, model):
    if not instance.attr:
        model_name = instance._meta.model_name
        # Find the maximum existing custom_id and start from there
        max_attr = model_name.object.aggregate(models.Max('attr'))[f'{attr}__max']
        if max_attr is not None:
            instance.attr = max_attr + 1
        else:
            instance.attr = 1  # Start from 471 if no records exist yet


