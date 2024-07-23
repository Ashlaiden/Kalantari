from datetime import timedelta

from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.db.models import Q

from account.models import Account
# import custom modules
from core.core.file_presave import upload_image_path
from core.core.slug_auto_generate import slug_generator
# from core.core.id_generator import generate_id
from core.core.model_methods import calculate_score
from tags.models import Branch, Tags


# Managers
# Product Managers-------------------------------------------
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.PUBLISHED)

    def get_by_branch(self, branch):
        try:
            return self.get_queryset().filter(branch=branch)
        except Product.DoesNotExist:
            return None

    def get_by_uid(self, uid: int):
        try:
            return self.get_queryset().get(uid=uid)
        except Product.DoesNotExist:
            return None

    def get_product(self, uid: int, slug=None):
        try:
            if slug is not None:
                return self.get_queryset().get(uid=uid, slug=slug)
            else:
                return self.get_queryset().get(uid=uid)
        except Product.DoesNotExist:
            return None

    def add_view_count(self, product_uid):
        try:
            product = self.get_by_uid(uid=product_uid)
            if product:
                product.views_count += 1
                product.save()
                self.update_product_score(product_uid)
                return True
            else:
                return False
        except Product.DoesNotExist:
            return False

    def add_bought_count(self, product_uid):
        try:
            product = self.get_by_uid(uid=product_uid)
            if product:
                product.bought_count += 1
                product.save()
                self.update_product_score(product_uid)
                return True
            else:
                return False
        except Product.DoesNotExist:
            return False

    def update_product_score(self, product_uid):
        try:
            product = self.get_by_uid(uid=product_uid)
            if product:
                score = calculate_score(
                    bought_count=product.bought_count,
                    views_count=product.views_count,
                    stock=product.stock,
                    created=product.created
                )
                product.score = score
                product.save()
                return True
            else:
                return False
        except Product.DoesNotExist:
            return False

    def get_highest_score_products(self, count: int):
        return self.get_queryset().order_by('-score')[:count]

    # def search(self, query):
    #     lookup = (
    #             Q(title__icontains=query) |
    #             Q(description__icontains=query) |
    #             Q(tag__title__icontains=query)
    #     )
    #     return self.get_queryset().filter(lookup).distinct()

    # def get_by_category(self, category_name):
    #     return self.get_queryset().filter(category__slug__iexact=category_name)

    # def related_products_by_categories(self, obj):
    #     return self.get_queryset().filter(category__product=obj).distinct()

    # def product_tags(self, obj):
    #     return self.get_queryset().get(id=obj.id).tags.all().distinct()

    # def related_products_by_tags(self, obj):
    #     return self.get_queryset().filter(product_status=obj.status).distinct()

    # def get_price(self, product_id):
    #     product = self.get_queryset().filter(id=product_id).first()
    #     return product.price

    # def get_products_by_group_category(self, group_slug):
    #     return self.get_queryset().filter(category__group_category__slug__iexact=group_slug)

    # def most_visited(self, count: int = None):
    #     if count > 0:
    #         return self.get_queryset().order_by('-visit_count').all()[:count]
    #     else:
    #         return self.get_queryset().order_by('-visit_count').all()

    # def latest_product(self, count: int = None):
    #     if count > 0:
    #         return self.get_queryset().order_by('-created').all()[:count]
    #     else:
    #         return self.get_queryset().order_by('-created').all()


class ViewManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def add_product_view(self, ip_address, product_uid, user_id=None):
        try:
            try:
                vws = self.get_queryset().filter(ip_address=ip_address, product__uid=product_uid).order_by('-created')
                dif_time = timezone.now() - vws.first().created
                if dif_time < timedelta(hours=2):
                    return False
            except Exception:
                pass
            prd = Product.published.get_by_uid(uid=product_uid)
            self.create(ip_address=ip_address, user_id=user_id if user_id is not None else None, product=prd)
            Product.published.add_view_count(product_uid=prd.uid)
            return True
        except Exception:
            return False

    def get_product_views(self, uid=None, product=None):
        try:
            if uid is not None:
                return self.get_queryset().filter(product__uid=uid).all()
            if product is not None:
                return self.get_queryset().filter(product=product).all()
            return None
        except Exception:
            return None

    def get_product_view_count(self, uid=None, product=None):
        try:
            if uid is not None:
                return self.get_queryset().filter(product__uid=uid).count()
            if product is not None:
                return self.get_queryset().filter(product=product).count()
            return None
        except ProductView.DoesNotExist:
            return None


# Create your models here.
# Product---------------------------------------------------
class Product(models.Model):
    uid = models.IntegerField(unique=True, editable=False, null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    price = models.IntegerField()
    cover_image = models.ImageField(
        upload_to=upload_image_path,
        null=True,
        blank=True
    )
    hover_image = models.ImageField(
        upload_to=upload_image_path,
        null=True,
        blank=True
    )
    slug = models.SlugField(max_length=250, blank=True, allow_unicode=True)
    stock = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tags, related_name='tags', related_query_name='tags', blank=True)

    class Status(models.TextChoices):
        DRAFT = "DF", 'draft'
        PUBLISHED = "PB", 'published'

    # choice field
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    # Date
    publish = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    views_count = models.IntegerField(default=0)
    score = models.DecimalField(max_digits=15, decimal_places=4, default=0)

    object = models.Manager()
    published = PublishedManager()

    on_delete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('product:product_detail', args=[self.uid, self.slug])

    # make slug from title with slug_generator in .core.slug_auto_generate
    def save(self, *args, **kwargs):
        if self.status == 'PB' and not self.publish:
            self.publish = timezone.now()
        elif self.status == 'PB' and self.publish is not None and self.pk:
            original = Product.object.get(pk=self.pk)
            if original.status != self.status:
                self.publish = timezone.now()
        # Generate a slug from the title
        if not self.slug:
            self.slug = slug_generator(self.title, alternative='-')
        # Call the save method of the parent class
        # Generate ID
        if not self.id:
            from core.core.generator import generate_id
            self.id = generate_id('product')
        from core.core.model_methods import pre_save_uid
        self.uid = pre_save_uid(self.uid, 'product')
        self.score = calculate_score(
            bought_count=self.sold if self.sold is not None else 0,
            views_count=self.views_count if self.views_count is not None else 0,
            stock=self.stock if self.stock is not None else 0,
            created=self.created
        )
        super(Product, self).save(*args, **kwargs)


class ProductGallery(models.Model):
    uid = models.IntegerField(unique=True, editable=False, null=False)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_image_path, null=False, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Gallery', related_query_name='gallery')

    object = models.Manager()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate ID
        if not self.id:
            from core.core.generator import generate_id
            self.id = generate_id('productgallery')
        from core.core.model_methods import pre_save_uid
        self.uid = pre_save_uid(self.uid, 'productgallery')
        super(ProductGallery, self).save(*args, **kwargs)


class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)
    # j_created = jmodels.jDateTimeField(auto_now_add=True)

    object = models.Manager()
    view_manager = ViewManager()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return f"{self.product.title}--{self.ip_address}-{self.created}"














