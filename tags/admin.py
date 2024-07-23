from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'active']
    readonly_fields = ['created']
    ordering = ['-id']
    # list_filter = ['status', 'publish']
    # search_fields = ['id', 'title', 'description']
    # raw_id_fields = ['store']
    # date_hierarchy = 'publish'
    # prepopulated_fields = {"slug": ["title"]}
    list_editable = ['active']
    list_display_links = ['name']
    # filter_horizontal = ['category', 'tags']
    # exclude = ['on_delete']


@admin.register(GroupTags)
class GroupTagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'active']
    readonly_fields = ['created']
    ordering = ['-id']
    # list_filter = ['status', 'publish']
    # search_fields = ['id', 'title', 'description']
    # raw_id_fields = ['store']
    # date_hierarchy = 'publish'
    # prepopulated_fields = {"slug": ["title"]}
    list_editable = ['active']
    list_display_links = ['name']
    # filter_horizontal = ['category', 'tags']
    # exclude = ['on_delete']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'active']
    readonly_fields = ['created']
    ordering = ['-id']
    # list_filter = ['status', 'publish']
    # search_fields = ['id', 'title', 'description']
    # raw_id_fields = ['store']
    # date_hierarchy = 'publish'
    # prepopulated_fields = {"slug": ["title"]}
    list_editable = ['active']
    list_display_links = ['name']
    # filter_horizontal = ['category', 'tags']
    # exclude = ['on_delete']


