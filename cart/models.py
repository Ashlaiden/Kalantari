from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from account.models import Account
from product.models import Product


# Create your models here.
class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_active_order(self, user):
        return self.get_queryset().filter(user_id=user.id, is_paid=False).first()

    def get_order_items(self, user):
        order = self.get_active_order(user)
        items = OrderItem.order_detail_manager.get_by_order(order)
        return items
        # items = self.get_queryset().prefetch_related('items').filter(order_id=order.id)


class OrderItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_id(self, order, product_id):
        return self.get_queryset().get(order_id=order.id, product_id=product_id)

    def get_by_id(self, pk):
        try:
            return self.get_queryset().get(id=pk)
        except ObjectDoesNotExist:
            return None

    def get_detail(self, user, detail_uid):
        detail: OrderItem = self.get_queryset().filter(uid=detail_uid).first()
        if detail.order.user == user:
            return detail
        else:
            return None

    def get_by_order(self, order):
        return self.get_queryset().filter(order=order)


# Create your models here.
class Order(models.Model):
    uid = models.IntegerField(null=False, editable=False, unique=True)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(blank=True, null=True)

    # class PaymentMethod(models.TextChoices):
    #     UNPAID = "NP", 'unpaid'
    #
    # payment_method = models.CharField(max_length=2, choices=PaymentMethod.choices, default=PaymentMethod.UNPAID)

    object = models.Manager()
    order_manager = OrderManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f'{self.user.uid}-[{self.user.first_name}-{self.user.last_name}]'

    def save(self, *args, **kwargs):
        # Generate UID
        from core.core.model_methods import pre_save_uid
        self.uid = pre_save_uid(self.uid, 'order')
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    uid = models.IntegerField(null=False, editable=False, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField()
    count = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    object = models.Manager()
    order_detail_manager = OrderItemManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        # Generate UID
        from core.core.model_methods import pre_save_uid
        self.uid = pre_save_uid(self.uid, 'orderitem')
        super(OrderItem, self).save(*args, **kwargs)

