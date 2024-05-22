from django.contrib import admin
from favorite.models import Favorite


# Register your models here.
@admin.register(Favorite)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'created', 'session_uid']
    readonly_fields = ['created']
    ordering = ['-id']
    # list_filter = ['is_paid']
    search_fields = ['id']
    raw_id_fields = ['product', 'user']
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
