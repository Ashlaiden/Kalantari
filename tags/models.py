from django.db import models
from django.urls import reverse_lazy

from core.core.file_presave import upload_image_path


# Managers
class BranchManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def actives(self):
        return self.get_queryset().filter(active=True)


class GroupTagsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def actives(self):
        return self.get_queryset().filter(active=True)


class TagsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def actives(self):
        return self.get_queryset().filter(active=True)


# ---------------------------------------------------------
# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)

    active = models.BooleanField(default=False, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    manager = BranchManager()
    object = models.Manager()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('workshop:product_list', args=[self.name.lower()])


class GroupTags(models.Model):
    name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)

    active = models.BooleanField(default=False, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    manager = GroupTagsManager()
    object = models.Manager()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return self.name

    def get_constraints(self):
        return reverse_lazy('workshop:product_list', args=[self.name])


class Tags(models.Model):
    name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)

    active = models.BooleanField(default=False, blank=True)

    group = models.ForeignKey(GroupTags, on_delete=models.CASCADE, null=True)

    created = models.DateTimeField(auto_now_add=True)

    manager = TagsManager()
    object = models.Manager()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return self.name

    def get_constraints(self):
        return reverse_lazy('workshop:product_list', args=[self.name])




