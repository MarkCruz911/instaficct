"""posts application module."""


from django.apps import AppConfig


class PostsConfig(AppConfig):
    """posts application settings."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    varbose_name='Posts'
