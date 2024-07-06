import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from icecream import ic

from account.models import Account, Address
from product.models import Product


# Create your models here.
class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_active_order(self, user=None, session_uid=None):
        try:
            if user is not None:
                order = self.get_queryset().filter(user_id=user.id, is_paid=False).first()
                if order is None:
                    Order.order_manager.create(user=user, is_paid=False)
                return order if order is not None else self.get_queryset().filter(user_id=user.id, is_paid=False).first()
            if session_uid is not None:
                order = self.get_queryset().filter(session_uid=session_uid, is_paid=False).first()
                if order is None:
                    Order.order_manager.create(session_uid=session_uid, is_paid=False)
                return order if order is not None else self.get_queryset().filter(session_uid=session_uid, is_paid=False).first()
        except ObjectDoesNotExist:
            return None

    def get_order_items(self, user=None, session_uid=None):
        try:
            order = self.get_active_order(
                user=user if user is not None and session_uid is None else None,
                session_uid=session_uid if session_uid is not None and user is None else None
            )
            items = OrderItem.order_detail_manager.get_by_order(
                user=user if user is not None and session_uid is None else None,
                session_uid=session_uid if session_uid is not None and user is None else None,
                order=order
            )
            return items
            # if user is not None:
            #     order = self.get_active_order(user=user)
            #     items = OrderItem.order_detail_manager.get_by_order(user=user, order=order)
            #     print(f'user: {items}')
            #     return items
            # if session_uid is not None:
            #     order = self.get_active_order(session_uid=session_uid)
            #     print(f'order: {order}')
            #     items = OrderItem.order_detail_manager.get_by_order(order=order)
            #     print(f'session: {items}')
            #     return items
        except Exception:
            print('error!')
            return None
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

    def get_detail(self, user=None, session_uid=None, uid=None, product=None, product_uid=None):
        item = None
        print(1)
        if uid:
            print(2)
            try:
                print(3)
                item = self.get_queryset().get(
                    order__user=user if user is not None else None,
                    order__session_uid=session_uid if session_uid is not None and user is None else None,
                    uid=uid
                )
                print(4)
            except ObjectDoesNotExist:
                print(5)
                item = None
            finally:
                print(6)
                if item:
                    print(7)
                    return item
        if product:
            print(8)
            try:
                print(9)
                # item = self.get_queryset().get(
                #     order__user=user if user is not None else None,
                #     order__session_uid=session_uid if session_uid is not None and user is None else None,
                #     order__is_paid=False,
                #     product=product
                # )
                item = self.get_queryset().filter(
                    order__user=user if user is not None and session_uid is None else None,
                    order__session_uid=session_uid if session_uid is not None and user is None else None,
                    order__is_paid=False,
                    product=product
                ).first()
                print(10)
                print(f'item: {item}')
            except ObjectDoesNotExist:
                print(11)
                item = None
            finally:
                print(12)
                if item:
                    print(13)
                    return item
        if product_uid:
            print(14)
            try:
                print(15)
                item = self.get_queryset().get(
                    order__user=user if user is not None else None,
                    order__session_uid=session_uid if session_uid is not None and user is None else None,
                    order__is_paid=False,
                    product__uid=product_uid
                )
                print(16)
            except ObjectDoesNotExist:
                print(17)
                item = None
            finally:
                print(18)
                if item:
                    print(19)
                    return item
        if item:
            print(20)
            return item
        else:
            print(21)
            return None

    def is_exist(self, user=None, session_uid=None, product_uid=None):
        try:
            self.get_queryset().get(
                order__user=user if user is not None else None,
                order__session_uid=session_uid if session_uid is not None else None,
                order__is_paid=False,
                product__uid=+product_uid
            )
            return True
        except PermissionError:
            return False
        except TypeError:
            return False
        except ObjectDoesNotExist:
            return False

    def get_count(self, user=None, session_uid=None, uid=None, product=None):
        if uid:
            try:
                return self.get_queryset().get(
                    order__user=user if user is not None else None,
                    order__session_uid=session_uid if session_uid is not None else None,
                    uid=uid
                ).count
            except ObjectDoesNotExist:
                return None
        elif product:
            try:
                return self.get_queryset().get(order__user=user, order__is_paid=False, product=product).count
            except ObjectDoesNotExist:
                return None
        else:
            return None

    def get_by_order(self, user=None, session_uid=None, order=None):
        try:
            _order = Order.order_manager.get_active_order(
                user=user if user is not None else None,
                session_uid=session_uid if session_uid is not None else None
            )
            return self.get_queryset().filter(
                order=order if order is not None else _order,
                order__user=user if user is not None else None,
                order__session_uid=session_uid if session_uid is not None else None
            )
        except ObjectDoesNotExist:
            return None


# Create your models here.
class Order(models.Model):
    uid = models.IntegerField(null=False, editable=False, unique=True)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    session_uid = models.CharField(max_length=100, default=None, null=True, blank=True)
    offer_code = models.CharField(max_length=100, default=None, null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True)
    address_finalized = models.CharField(max_length=500, null=True, blank=True)
    step_updated = models.DateTimeField(auto_created=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class STATUS(models.TextChoices):
        OPEN = "OP", "OPEN"
        PENDING = "PE", "PENDING"
        IN_PROGRESS = "IP", "IN_PROGRESS"
        COMPLETED = "CM", "COMPLETED"
        CANCELLED = "CA", "CANCELLED"
        ERROR = "ER", "ERROR"

    status = models.CharField(max_length=2, choices=STATUS.choices, default=STATUS.OPEN)

    class STEP(models.TextChoices):
        OPEN = "OP", "OPEN"
        ADDRESSING = "AD", "ADDRESSING"
        CHECKOUT = "CO", "CHECKOUT"
        RECEIPT = "RC", "RECEIPT"
        PAYMENT = 'PA', 'PAYMENT'
        CANCELLED = "CA", "CANCELLED"
        ERROR = "ER", "ERROR"

    step = models.CharField(max_length=2, choices=STEP.choices, default=STEP.OPEN)

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
        return f'{self.user.uid}-[{self.user.first_name}-{self.user.last_name}]' if self.user is not None else f'{self.session_uid}'

    def save(self, *args, **kwargs):
        # Generate UID
        from core.core.model_methods import pre_save_uid
        self.uid = pre_save_uid(self.uid, 'order')
        if self.user is not None:
            self.session_uid = None
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

