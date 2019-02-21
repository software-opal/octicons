from django import template

register = template.Library()


@register.simple_tag
def octicon(name, **options):
    from octicons.store import default_store
    assert default_store is not None
    return default_store.get_as_html(name, **options)
