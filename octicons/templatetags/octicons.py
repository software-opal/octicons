from django import template
from octicons.store import default_store

assert default_store is not None

register = template.Library()


@register.simple_tag
def octicon(name, **options):
    return default_store.get_as_html(name, **options)
