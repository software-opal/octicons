# A Python port of GitHub's [Octicons](https://octicons.github.com/) for [Django](https://www.djangoproject.com/).

Octicons version: [v8.4.2](https://github.com/primer/octicons/releases/tag/v8.4.2)

Install this package from [PyPI](https://pypi.org/project/octicons/) using `pip` or your favorite Python package manager:

```
$ pip install octicons
```

## API

This package comes with the Octicons `data.json` built-in but you are not limited to using it.

### `octicons.store.default_store`

This is an `OcticonsStore` instance that loads the built-in data set. Use this unless you *really* need to use another.

### `octicons.octicons.OcticonStore`

This object handles creating and aliasing individual `Octicons`. You won't need to create an instance of this unless you have a special use-case, or are loading your own `data.json` file. 

- `OcticonStore.from_file(file=None)`(classmethod) -- Create an `OcticonsStore` instance by loading the given file(or the built-in file in `file` is not given). 
- `OcticonStore(data_dict, *, Octicon=Octicon)` -- Create an `OcticonsStore` instance using the `data_dict` given. Here you can also override the `Octicons` class used to create each icon instance. 

- `store.get_icon(name)`, `store[name]` -- Get the octicon with the name or alias of `name`. Returns an `Octicons` instance.
- `store.get_as_html(name, **opts)` -- A convenience method which gets the icon's instance; then calls `as_html` on that instance; passing any keyword arguments through to that call.

### `octicons.octicons.Octicon`

This is an instance of a single icon. Instances are built as part of the `__init__` method of `OcticonsStore`.

- `Octicons(data)` -- Create an icon instance using the information contained in the `data` dictionary.

- `icon.width`, `icon.height` -- The floating-point width and height the output SVG should be.
- `icon.path` -- A string representing the SVG path that creates the icon.
- `icon.name` -- Used to construct the correct `class` when generating the HTML.
- `icon.keywords` -- A list of the supported icon aliases.
- `icon.size_ratio` -- The ratio(`width/height`) between the width and the height of the icon. This is used when only one of `width` or `height` are specified to `as_html`.

- `icon.as_html(**opts)` -- Build HTML from the icon's information and the given options:
  - `width`/`height` -- If none are given; then use the icons width/height. If one is given; use it to calculate the missing dimension such that it maintains the aspect ratio. If both are given then use those values exactly.
  - `class`, `classes` -- Either a string or an iterable of strings to *append* to the default classes(`octicons` and `octicons-{self.name}`)
  - `aria_label` -- Makes the icon visible to screen-readers and changes the icon's role to `img`.
  - All other arguments will have `_`s replaced with `-` and added to the `<svg>` tag

Examples(paths snipped for brevity):
```
>>> from octicons.store import default_store
>>> default_store.get_as_html('like', id="my-like-button")
'<svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-thumbsup" aria-hidden="true" id="my-like-button"><path ...snip.../></svg>'
>>> default_store.get_as_html('like', classes="special", width=200)
'<svg version="1.1" width="200" height="200.0" viewBox="0 0 16 16" class="octicon octicon-thumbsup special" aria-hidden="true"><path ...snip.../></svg>'
>>> default_store.get_as_html('like', width=20, height=400, aria_label="Tall like button")
'<svg version="1.1" width="20" height="400" viewBox="0 0 16 16" class="octicon octicon-thumbsup" aria-label="Tall like button" role="img"><path ...snip.../></svg>'
```

## Django API

To use, add `'octicons'` to your `INSTALLED_APPS` list; then in your templates:

```
{% load octicons %}

{% octicon 'check' %}
<br />
{% octicon 'like' width=100 color="blue" class="facebook-like" %}
<br />
{% octicon 'gift' height="10" aria_label='This is a gift for you <3' %}
```

This is exactly equivalent to importing the `default_store` and calling `get_as_html`. Check that method's documentation for information on how it handles arguments.

## Overriding the default `data.json` file

There may be circumstances where the built-in data file is not what you're after. In that case you can use `OpticonStore.from_file` to load another `data.json` file. To get the `data.json` file for a specific version of Octicons you can copy it from the `build/data.json` of the [`octicons` npm package](https://www.npmjs.com/package/octicons). Have a look at the `update_data_json.sh` file for how to do that.

## Extending

Obviously the name and the naming scheme implies tight integration with Octicons; however this is not necessarily the case. All that is needed is a JSON file with a dictionary of icons, for example:

```
{
  "plus": {
    "name": "plus",
    "keywords": ["add", "new", "more"],
    "width":12,
    "height":16,
    "path":"<path fill-rule=\"evenodd\" d=\"M12 9H7v5H5V9H0V7h5V2h2v5h5v2z\"/>"
  },
  ...
}
```

## Versioning

This project follows Semantic versioning, ish. Due to the need to track 2 separate versions, the API and the Octicons themselves, versioning will be as follows: `MAJOR.OCTICONS_MINOR.OCTICONS_PATCH.PATCH`

Breaking changes such as changing either the Django or Python API will increment the `MAJOR` version. As will upgrading Octicons to a new major version(e.g. Octicons 9.x.x). The `MINOR.PATCH` will use the Octicons minor and patch as that is the most useful information. The final field will be added when bug-fixes or patches are made that don't change the Octicons version.

If you have a better solution feel free to open an issue/PR. Chances are it'll be better than this franken-versioning scheme I came up with.
