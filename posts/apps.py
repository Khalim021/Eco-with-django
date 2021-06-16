from django.apps import AppConfig
from django.utils.translation import  ugettext_lazy as _


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name = _('posts')
