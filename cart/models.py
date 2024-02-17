from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from account.models import Account
from product.models import Product


# Create your models here.
class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_active_order(self, user):
        return self.get_queryset().filter(user_id=user.id, is_paid=False)


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


# Create your models here.
class Order(models.Model):
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


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
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

