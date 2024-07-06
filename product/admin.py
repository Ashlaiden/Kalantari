from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish', 'status', 'gallery', 'views_count', 'sold', 'score', 'uid']
    readonly_fields = []
    ordering = ['-id', '-publish', 'title']
    list_filter = ['status', 'publish']
    search_fields = ['id', 'title', 'description']
    # raw_id_fields = ['store']
    date_hierarchy = 'publish'
    # prepopulated_fields = {"slug": ["title"]}
    list_editable = ['status']
    list_display_links = ['title']
    # filter_horizontal = ['category', 'tags']
    exclude = ['on_delete']

    def get_readonly_fields(self, request, obj=None):
        # Specify fields that should be read-only
        if obj:
            if obj.publish and obj.status == 'PB':
                return super().get_readonly_fields(request, obj) + ['publish']
            else:
                return super().get_readonly_fields(request, obj) + []
        return self.readonly_fields

    # def custom_visit_count(self, obj):
    #     visit_count = obj.visit_count
    #     if visit_count == 0:
    #         return mark_safe('<span style="color: orange;">-</span>')
    #     else:
    #         return mark_safe(f'<span style="color: white;">{visit_count}</span>')
    #
    # custom_visit_count.short_description = 'visit_count'

    def gallery(self, obj):
        gallery_count = ProductGallery.object.filter(product_id=obj.id).count()
        return gallery_count

    gallery.short_description = 'Gallery'

    # def tags_count(self, obj):
    #     tags_count = Product.all_products.all_product_tags(obj=obj).distinct().count()
    #     return tags_count


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product_id']
    ordering = ['-id']
    list_filter = ['id']
    search_fields = ['product_id', 'title']
    raw_id_fields = ['product']
    # date_hierarchy = 'publish'
    # prepopulated_fields = {"slug": ["title"]}
    # list_editable = ['product_status']
    list_display_links = ['title']
    # filter_horizontal = ['product']


@admin.register(ProductView)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'product', 'user_field', 'created']
    ordering = ['-id']
    list_filter = ['product']
    search_fields = ['product', 'user']
    # raw_id_fields = ['product']
    list_display_links = ['ip_address']

    def user_field(self, obj):
        if obj.user_id is not None:
            user = Account.object.get(pk=obj.user_id)
            return f'{user.uid}-{user.email}'
        else:
            return '-'

    user_field.short_description = 'user'


