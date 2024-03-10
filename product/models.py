from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q

# import custom modules
from core.core.file_presave import upload_image_path
from core.core.slug_auto_generate import slug_generator
# from core.core.id_generator import generate_id


# Managers
# Product Managers-------------------------------------------
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.PUBLISHED)

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


# Create your models here.
# Product---------------------------------------------------
class Product(models.Model):
    uid = models.IntegerField(unique=True, editable=False, null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    slug = models.SlugField(max_length=250, blank=True, allow_unicode=True)
    stock = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

    class Status(models.TextChoices):
        DRAFT = "DF", 'draft'
        PUBLISHED = "PB", 'published'

    # choice field
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    # Date
    publish = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
        return reverse('shop-product-urls:product_pk', args=[{self.id}])

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

