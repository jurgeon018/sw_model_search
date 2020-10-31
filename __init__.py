
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


from .lib import (
    normalize_query, model_search, tags_search, build_query,
)


__all__ = ['normalize_query', 'build_query', 'model_search']


class ModelSearchConfig(AppConfig):
    name = 'sw_model_search'
    verbose_name = _("Search")


default_app_config = 'sw_model_search.ModelSearchConfig'
