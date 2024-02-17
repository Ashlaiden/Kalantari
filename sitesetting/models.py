from django.db import models

from core.core.file_presave import upload_image_path


# Managers
class ActiveSettingManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().all()

    def get_active(self):
        try:
            active_setting = self.get_queryset().get(active=True)
            return active_setting
        except:
            active_setting = self.get_queryset().filter(active=True)
            if active_setting.count() <= 2:
                return active_setting.first()
            else:
                return active_setting



class FooterTables(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_active_heads(self):
        return self.get_queryset().filter(active=True)

    def get_tables(self):
        all_heads = self.get_active_heads()
        main_group_data = []
        for head in all_heads:
            rows = head.footertablerow_set.all()
            main_group_data.append({
                'head': head,
                'rows': rows,
            })
        return main_group_data


# Create your models here.
class SocialMedia(models.Model):
    title = models.CharField(max_length=80, help_text='this only visible in admin-panel')
    name = models.CharField(max_length=50, help_text='this will be applied to the site')
    image = models.ImageField(upload_to=upload_image_path, help_text='this is a small picture of your social-media')
    link = models.URLField(help_text='please enter your social-media page link here')

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
            self.id = generate_id('socialmedia')
        super(SocialMedia, self).save(*args, **kwargs)


class SiteSetting(models.Model):
    title = models.CharField(max_length=100, help_text='this is only for display setting config in admin panel')
    brand_name = models.CharField(max_length=100, help_text='enter your site title here')
    company_address = models.CharField(max_length=300, null=True, blank=True, help_text='write your company address here')
    phone = models.BigIntegerField(null=True, blank=True, help_text='enter your company phone number')
    fax = models.BigIntegerField(null=True, blank=True, help_text='enter your company fax')
    email_address = models.EmailField(null=True, blank=True, help_text='enter your site support email address here')
    logo = models.ImageField(upload_to=upload_image_path)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # company_location_image = models.ImageField(upload_to=upload_image_path)
    social_media = models.ManyToManyField(
        SocialMedia, help_text='if you do not have social-media yet...'
                               'please add one from social-media section'
    )
    copy_right = models.CharField(max_length=300, null=True, blank=True, help_text='write copyright text here')
    about_us = models.TextField(help_text='enter some information about your business')

    active = models.BooleanField(
        default=False, help_text='this checkbox means these settings should be replaced to your current site settings'
                                 'if you make this True, the currently active settings will be automatically disabled'
                                 'and these settings will be applied to the site'
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    object = models.Manager()
    setting_manager = ActiveSettingManager()

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
            self.id = generate_id('sitesetting')
        super(SiteSetting, self).save(*args, **kwargs)


class FooterTableHead(models.Model):
    title = models.CharField(max_length=70, help_text='you can set some items to this head in rows section')
    active = models.BooleanField(
        default=True,
        blank=True,
        help_text='When you set this option to False, this column will no longer be displayed on the website'
    )

    object = models.Manager()
    table_manager = FooterTables()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return self.title


class FooterTableRow(models.Model):
    title = models.CharField(max_length=70, help_text='this is for display in rows of table head')
    link = models.URLField(blank=True, help_text='enter the url of some site section for on_click option')
    table_head = models.ForeignKey(FooterTableHead, on_delete=models.CASCADE, help_text='assign item to a table head')

    object = models.Manager()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return self.title








