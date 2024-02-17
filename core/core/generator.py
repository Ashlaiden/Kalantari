from django.db import models
from django.contrib.auth.models import User
from product.models import Product, ProductGallery
from sitesetting.models import SiteSetting, SocialMedia
from account.models import Account


def generate_id(sender):
    # Generate ID
    max_id = None

    if sender == 'product':
        # Find the maximum existing custom_id and start from there
        max_id = Product.object.aggregate(models.Max('id'))['id__max']
    elif sender == 'productgallery':
        max_id = ProductGallery.object.aggregate(models.Max('id'))['id__max']
    elif sender == 'socialmedia':
        max_id = SocialMedia.object.aggregate(models.Max('id'))['id__max']
    elif sender == 'sitesetting':
        max_id = SiteSetting.object.aggregate(models.Max('id'))['id__max']
    elif sender == 'account':
        max_id = Account.object.aggregate(models.Max('uid'))['uid__max']

    if max_id is not None:
        return max_id + 1
    else:
        if sender == 'account':
            starter_account_uid = 101837295
            return starter_account_uid
        else:
            return 1  # Start from 1 if no records exist yet


def generate_user_name(sender):
    if sender == 'account':
        return generate_id('account')
    else:
        return None
