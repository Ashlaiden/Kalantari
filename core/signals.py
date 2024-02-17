from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from sitesetting.models import SiteSetting


# Use a signal to handle the deletion of authors
@receiver(pre_save, sender=SiteSetting)
def pre_save_settings_handler(sender, instance, **kwargs):
    if instance.active:
        settings = SiteSetting.object.filter(active=True).all()

        if settings:
            for setting in settings:
                setting.active = False
                setting.save()

