

class SafeHtmlString(str):

    def __html__(self):
        return self


_mark_safe = SafeHtmlString


def _conditional_escape(text):
    # Taken from django.utils.html.conditional_escape (Django version 2.0.8)
    if hasattr(text, '__html__'):
        return text.__html__()
    else:
        return _escape(text)


def _escape(text):
    # Taken from django.utils.html.escape (Django version 2.0.8)
    return _mark_safe(
        _force_text(text).replace('&', '&amp;').replace('<', '&lt;')
        .replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')
    )


def _force_text(s, encoding='utf-8', strings_only=False, errors='strict'):
    # Adapted from django.utils.encoding.force_text (Django version 2.0.8)
    if issubclass(type(s), str):
        return s
    if isinstance(s, bytes):
        return str(s, encoding, errors)
    else:
        return str(s)


try:
    # Support no django; but prefer django if it's avaliable
    from django.utils.encoding import force_text
    from django.utils.html import conditional_escape, escape
    from django.utils.safestring import mark_safe
except:
    conditional_escape = _conditional_escape
    escape = _escape
    mark_safe = _mark_safe
    force_text = _force_text
