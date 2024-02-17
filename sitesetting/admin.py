from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# Register your models here.
@admin.register(SiteSetting)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'custom_setting_title', 'brand_name', 'created', 'active', 'updated', 'social_count']
    ordering = ['-created', '-updated']
    list_filter = ['active', 'created']
    # search_fields = ['id', 'title', 'description']
    # raw_id_fields = ['store']
    # date_hierarchy = 'created'
    prepopulated_fields = {"title": ["brand_name"]}
    # list_editable = ['product_status']
    list_display_links = ['custom_setting_title']
    filter_horizontal = ['social_media']

    def custom_setting_title(self, obj):
        obj_title = obj.title
        status = obj.active
        if status:
            return mark_safe(f'<span style="color: green;">{obj_title}</span>')
        else:
            return mark_safe(f'<span style="color: red;">{obj_title}</span>')

    custom_setting_title.short_description = 'title'

    def social_count(self, obj):
        obj_socials = obj.social_media.count()
        status = obj.active
        if status:
            return mark_safe(f'<span style="color: green;">{obj_socials}</span>')
        else:
            return mark_safe(f'<span style="color: red;">{obj_socials}</span>')

    social_count.short_description = 'social'


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    ordering = ['-title']
    # list_filter = ['product_status', 'publish', 'offer', 'store']
    search_fields = ['id', 'title']
    # raw_id_fields = ['store']
    # date_hierarchy = 'publish'
    prepopulated_fields = {"title": ["name"]}
    # list_editable = ['product_status']
    list_display_links = ['title']


@admin.register(FooterTableHead)
class FooterTableHeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'custom_title', 'active', 'rows_count']
    ordering = ['-id']
    # list_filter = ['product_status', 'publish', 'offer', 'store']
    # search_fields = ['id', 'title']
    # raw_id_fields = ['store']
    # date_hierarchy = 'publish'
    # # prepopulated_fields = {"slug": ["title"]}
    list_editable = ['active']
    list_display_links = ['custom_title']
    # filter_horizontal = ['category', 'tags']

    def custom_title(self, obj):
        title = obj.title
        active = obj.active
        rows = obj.footertablerow_set.count()
        if active and rows != 0:
            return mark_safe(f'<span style="color: green;">{title}</span>')
        elif active and rows == 0:
            return mark_safe(f'<span style="color: orange;">{title}</span>')
        elif not active and rows == 0:
            return mark_safe(f'<span style="color: red;"><span style="color: orange;">!-</span>{title}</span>')
        else:
            return mark_safe(f'<span style="color: red;">{title}</span>')

    custom_title.short_description = 'title'

    def rows_count(self, obj):
        count = obj.footertablerow_set.count()
        if count != 0:
            return mark_safe(f'<span style="color: green;">{count}</span>')
        else:
            return mark_safe(f'<span style="color: orange;">!-!</span>')

    rows_count.short_description = 'rows-count'


@admin.register(FooterTableRow)
class FooterTableRowAdmin(admin.ModelAdmin):
    list_display = ['id', 'custom_title', 'table_head_id']
    ordering = ['-id', 'title']
    list_filter = ['table_head_id']
    search_fields = ['id', 'title']
    # raw_id_fields = ['store']
    # date_hierarchy = 'publish'
    # # prepopulated_fields = {"slug": ["title"]}
    # list_editable = ['product_status']
    list_display_links = ['custom_title']
    # filter_horizontal = ['category', 'tags']

    def custom_title(self, obj):
        title = obj.title
        obj_head_status = obj.table_head.active
        if obj_head_status:
            return mark_safe(f'<span style="color: green;">{title}</span>')
        elif not obj_head_status:
            return mark_safe(f'<span style="color: red;">{title}</span>')

    custom_title.short_description = 'title'
