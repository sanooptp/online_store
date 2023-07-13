from django.apps import AppConfig
from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver

def create_initial_items(sender, **kwargs):
    if sender.name == 'users' and kwargs.get('app') == apps.get_app_config('users'):
        try:
            MigrationHistory = apps.get_model('users', 'MigrationHistory')
            first_run = not MigrationHistory.objects.exists()
        except LookupError:
            # MigrationHistory model not found, assuming first run
            first_run = True

        if first_run:
            # Import and call the function to create initial items
            from .initial_data import create_items
            create_items()

@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    create_initial_items(sender, **kwargs)
