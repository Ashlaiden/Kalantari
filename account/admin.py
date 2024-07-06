from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    fieldsets = (
        ('Account Info', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ['phone', 'first_name', 'last_name', 'gender', 'birth_date']}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'j_updated', 'last_IP')}),
        # Add your custom fields here
        ('UID', {'fields': ('uid',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        ('Personal Info', {'fields': ['phone', 'first_name', 'last_name', 'gender']}),
    )
    # Specify the field name that is used for logging in
    username_field = "email"
    # exclude = ('username',)

    list_display = ['id', 'name', 'email', 'is_active', 'is_staff', 'uid']
    readonly_fields = ['uid', 'last_IP', 'j_updated', 'last_login', 'date_joined']
    ordering = ['-id']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['id', 'uid', 'email', 'phone', 'name']
    # raw_id_fields = ['store']
    date_hierarchy = 'j_created'
    # prepopulated_fields = {"slug": ["title"]}
    # list_editable = ['product_status']
    list_display_links = ['name']
    # filter_horizontal = ['category', 'tags']

    # def get_readonly_fields(self, request, obj=None):
    #     # Specify fields that should be read-only
    #     if obj:
    #         return super().get_readonly_fields(request, obj) + ['visit_count']
    #     return self.readonly_fields
    #
    def name(self, obj):
        first_name = obj.first_name
        last_name = obj.last_name
        return f'{first_name} {last_name}'

    name.short_description = 'Full Name'
    #
    # def custom_visit_count(self, obj):
    #     visit_count = obj.visit_count
    #     if visit_count == 0:
    #         return mark_safe('<span style="color: orange;">-</span>')
    #     else:
    #         return mark_safe(f'<span style="color: white;">{visit_count}</span>')
    #
    # custom_visit_count.short_description = 'visit_count'
    #
    # def gallery(self, obj):
    #     gallery_count = ProductGallery.address_manager.filter(product_id=obj.id).count()
    #     return gallery_count
    #
    # def tags_count(self, obj):
    #     tags_count = Product.all_products.all_product_tags(obj=obj).distinct().count()
    #     return tags_count


admin.site.register(Account, AccountAdmin)







