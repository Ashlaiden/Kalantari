from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Import and execute your signals.py file
        import core.signals  # Replace 'your_app_name' with your app's actual name

