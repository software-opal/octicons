import warnings

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def octicon(name, **options):
    from octicons.octicons import OcticonStore

    if hasattr(settings, 'OCTICONS_BASE_FILE'):
        base_file = settings.OCTICONS_BASE_FILE
    else:
        base_file = None
    if hasattr(settings, 'OCTICONS_ADDITIONAL_FILE'):
        additional_file = settings.OCTICONS_ADDITIONAL_FILE
    else:
        additional_file = None
    try:
        default_store = OcticonStore.from_file(base_file, additional_file=additional_file)
    except Exception as e:
        default_store = None
        warnings.warn("Failed to load Octicons store.", source=e)
        raise

    assert default_store is not None
    return default_store.get_as_html(name, **options)
