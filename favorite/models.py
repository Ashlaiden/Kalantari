import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from account.models import Account
from product.models import Product


# Manager
class FavoriteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_favorites(self, user=None, session_uid=None):
        item = None
        if user:
            try:
                item = self.get_queryset().filter(user=user)
            except ObjectDoesNotExist:
                item = None
            except TypeError:
                item = None
            finally:
                if item is not None:
                    return item
        elif session_uid:
            try:
                item = self.get_queryset().filter(session_uid=session_uid)
            except ObjectDoesNotExist:
                item = None
            except TypeError:
                item = None
            finally:
                if item is not None:
                    return item
        else:
            return None

    def get_favorite(self, product_uid, user=None, session_uid=None):
        item = None
        if user:
            try:
                item = self.get_queryset().filter(user=user, product__uid=product_uid)
            except ObjectDoesNotExist:
                item = None
            except TypeError:
                item = None
            finally:
                if item is not None:
                    return item
        elif session_uid:
            try:
                item = self.get_queryset().filter(session_uid=session_uid, product__uid=product_uid)
            except ObjectDoesNotExist:
                item = None
            except TypeError:
                item = None
            finally:
                if item is not None:
                    return item
        else:
            return None

    def is_in_favorites(self, product_uid, user=None, session_uid=None):
        item = None
        if user:
            try:
                item = self.get_queryset().get(user=user, product__uid=product_uid)
            except ObjectDoesNotExist:
                item = None
            except TypeError:
                item = None
            finally:
                if item is not None:
                    return True
        if session_uid:
            try:
                item = self.get_queryset().get(session_uid=session_uid, product__uid=product_uid)
            except ObjectDoesNotExist:
                item = None
            except TypeError:
                item = None
            finally:
                if item is not None:
                    return True
        if item is None:
            return False


# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    session_uid = models.CharField(max_length=100, default=None, null=True, blank=True)

    object = models.Manager()
    manager = FavoriteManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        if self.user:
            self.session_uid = None
        return super(Favorite, self).save(*args, **kwargs)






