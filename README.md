A Python port of GitHub's [Octicons](https://octicons.github.com/) for [Django](https://www.djangoproject.com/).

Octicons version: [v8.0.0](https://github.com/primer/octicons/releases/tag/v8.0.0)

To use, add `'octicons'` to your `INSTALLED_APPS` list; then in your templates:

```
{% load octicons %}

{% octicon 'check' %}
<br />
{% octicon 'like' width=100 color="blue" class="facebook-like" %}
<br />
{% octicon 'gift' height="10" aria_label='This is a gift for you <3' %}
```

The first argument is the icon name, or an alias, the remaining arguments must 
be keyword arguments and they are added as-is(with some exceptions) to the 
output SVG. The exceptions are:

 - All values are conditionally escaped using Django's 
    built-in `conditional_escape` function.
 - Any `'_'`s in the name of a keyword argument will be replaced 
    unconditionally with `'-'`s
 - Specifying only one of the `width` or `height` will fill the other value in 
    maintaining the aspect ratio.
 - Specifying `class` will cause the classes defined to be added to the two 
    default classes(`octicon` and `octicon-<name>` where `<name>` is the name 
    listed in the data-file; not necessarily the name given).
 - Adding `aria-label`(keyword argument `aria_label`) will remove the 
    `aria-hidden` attribute and set `role="img"`.
