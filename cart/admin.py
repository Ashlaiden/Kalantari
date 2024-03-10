from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     ('Account Info', {'fields': ('email', 'password')}),
    #     ('Personal Info', {'fields': ['phone', 'first_name', 'last_name', 'gender', 'birth_date']}),
    #     ('Permissions', {
    #         'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     ('Important dates', {'fields': ('last_login', 'date_joined', 'j_updated', 'last_IP')}),
    #     # Add your custom fields here
    #     ('UID', {'fields': ('uid',)}),
    # )
    #  add_fieldsets = (
    #      (None, {
    #          'classes': ('wide',),
    #          'fields': ('user',),
    #      }),
    # )
    # Specify the field name that is used for logging in
    # username_field = "email"
    # exclude = ('username',)

    list_display = ['id', 'user', 'is_paid', 'created', 'uid']
    readonly_fields = ['uid']
    ordering = ['-id']
    list_filter = ['is_paid']
    search_fields = ['id', 'uid']
    raw_id_fields = ['user']
    date_hierarchy = 'created'
    # prepopulated_fields = {"slug": ["title"]}
    # list_editable = ['product_status']
    list_display_links = ['user']
    # filter_horizontal = ['category', 'tags']

    # def name(self, obj):
    #     first_name = obj.first_name
    #     last_name = obj.last_name
    #     return f'{first_name} {last_name}'
    #
    # name.short_description = 'Full Name'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'count', 'uid']
    readonly_fields = ['uid']
    ordering = ['-id']
    # list_filter = ['is_paid']
    search_fields = ['id', 'uid']
    raw_id_fields = ['product']
    date_hierarchy = 'created'
    # prepopulated_fields = {"slug": ["title"]}
    # list_editable = ['product_status']
    list_display_links = ['order']
    # filter_horizontal = ['category', 'tags']

    # def name(self, obj):
    #     first_name = obj.first_name
    #     last_name = obj.last_name
    #     return f'{first_name} {last_name}'
    #
    # name.short_description = 'Full Name'


