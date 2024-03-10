from django.db import models
from django.contrib.auth.models import User
from product.models import Product, ProductGallery
from sitesetting.models import SiteSetting, SocialMedia
from account.models import Account
from cart.models import Order, OrderItem


def get_max(sender):
    sender = str(sender).lower()
    # Generate ID
    max_id = None
    max_uid = None

    if sender == 'product':
        # Find the maximum existing custom_id and start from there
        max_id = Product.object.aggregate(models.Max('id'))['id__max']
        max_uid = Product.object.aggregate(models.Max('uid'))['uid__max']
    elif sender == 'productgallery':
        max_id = ProductGallery.object.aggregate(models.Max('id'))['id__max']
        max_uid = ProductGallery.object.aggregate(models.Max('uid'))['uid__max']
    elif sender == 'socialmedia':
        max_id = SocialMedia.object.aggregate(models.Max('id'))['id__max']
        max_uid = SocialMedia.object.aggregate(models.Max('uid'))['uid__max']
    elif sender == 'sitesetting':
        max_id = SiteSetting.object.aggregate(models.Max('id'))['id__max']
        max_uid = SiteSetting.object.aggregate(models.Max('uid'))['uid__max']
    elif sender == 'account':
        max_id = Account.object.aggregate(models.Max('id'))['id__max']
        max_uid = Account.object.aggregate(models.Max('uid'))['uid__max']
    elif sender == 'order':
        max_id = Order.object.aggregate(models.Max('id'))['id__max']
        max_uid = Order.object.aggregate(models.Max('uid'))['uid__max']
    elif sender == 'orderitem':
        max_id = OrderItem.object.aggregate(models.Max('id'))['id__max']
        max_uid = OrderItem.object.aggregate(models.Max('uid'))['uid__max']

    return max_id, max_uid


def generate_id(sender):
    # Generate ID
    max_id, _ = get_max(sender)

    if max_id is not None:
        return max_id + 1
    else:
        return 1  # Start from 1 if no records exist yet


def generate_uid(sender):
    # Generate ID
    _, max_uid = get_max(sender)

    if max_uid is not None:
        return max_uid + 1
    else:
        if sender == 'account':
            starter_account_uid = 101837295
            return starter_account_uid
        elif sender == 'product':
            starter_product_uid = 1100167943
            return starter_product_uid
        elif sender == 'productgallery':
            starter_product_gallery_uid = 120168435
        elif sender == 'order':
            starter_order_uid = 301837295
            return starter_order_uid
        elif sender == 'orderitem':
            starter_order_item_uid = 501837295
            return starter_order_item_uid
        else:
            return 1  # Start from 1 if no records exist yet


def generate_user_name(sender):
    if sender == 'account':
        return generate_id('account')
    else:
        return None
