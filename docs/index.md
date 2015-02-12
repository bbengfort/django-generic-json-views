# Django Generic JSON Views

**Class based generic views that render JSON data.**

The `django.views.generic` package has several generic class based views
that render HTML for a model or a set of applications and provide an API
to use those views and modify querysets and context data. However, Django
recommends that to specify the output of JSON data, you use a mixin or
another approach to `render_to_response` the JSON.

Many AJAX applications, however, have the need for quick views like the
ones specified the in the `generic` package to either serialize a model
or to provide other context data in the View logic. These generic views
allow that, and correctly render JSON data with the correct HTTP Headers.

## Installation

The easiest way to install this library is to use `pip` as follows:

```bash
$ pip install django-generic-json-views
```

Alternatively you can download the source code and run the following:

```bash
$ python setup.py install
```

Otherwise copy the views.py file to a utils directory in your Django Project and import it correctly from there.

## Basic Usage

There are several provided classes that work right off the bat:

* `JSONDataView`
* `JSONDetailView`
* `JSONListView`
* `PaginatedJSONListView`
* `JSONFormView`

These classes all provide the following functionality:

1. Render the output of `get_context_data` as a JSON object
2. Serialize Django Models and Querysets with a Lazy Encoder
3. Correctly add the application/json HTTP header
4. Remove duplicate objects and middleware context built into Django

The most simple example is the `JSONDataView` which will allow you to output generic JSON data as needed:

```python
class JSONTime(JSONDataView):

    def get_context_data(self, **kwargs):
        context = super(JSONTime, self).get_context_data(**kwargs)
        context['current_time'] = datetime.now.strftime("%c")
        return context
```

In order to render the detail view of a model as a JSON serialization,
use the `JSONDetailView` -- note that this view can be used for both
serialization and deserialization as noted in the section below.

```python
class CustomerJSON(JSONDetailView):

    model = Customer
```

Many JSON views are centered around lists, hence the `JSONListView` and
the `PaginatedJSONListView`.

```python
class ProductsJSON(JSONListView):

    model = Product
```

The `PaginatedJSONListView` looks up the special parameter `page=n` to
decide which part of the list to return. It also removes the Django paginator
object and returns the following data:

```python
{
    'pages': Number,
    'count': Number,
    'is_paginated': Bool,
    'per_page': Number,
    'current': Number,
    'object_list': List
}
```

An example of using this view is:

```python
class PaginatedProducts(PaginatedJSONListView):

    paginate_by = 10
    count_query = 'count'
    count_only  = False

    def get_querset(self):
        return Product.objects.filter(instores=True)
```

`count_query` specifies the name of the property to pass in as kwargs in
a GET request that will force the view to only return the total number
of expected items, and not fetch them from the db. E.g. if you use
`/?count=true` in your url, the view will respond only with the total number.

Finally the JSONFormView accepts incoming JSON data to populate a form
rather than waiting for HTTP POST data, this is how you would do AJAX login
forms. Note that GET requests are not allowed.

```python
class LoginForm(JSONFormView):

    form = LoginForm
```

In the form view, a parameter `success` is passed back, as either True or
False. This can be customized by overriding `get_context_data`.

## Serialization & Deserialization

The lazy encoder attempts to serialze the model into a dictionary or other
compatible JSON-Python type, and does so in a recursive fashion,
continuing to serialize objects, the default serialization is this:

1. If the object is an iterable- construct a list
2. If the object extends `ModelBase` attempt to call a `serialize` method
3. Utilize `force_unicode` to force the object to unicode data.

Therefore if your `Models` provide a `serialize` method that returns a
dictionary, you can very easily control what fields and what format the
model is serialized to.

Additionally you can specify a `@classmethod` `deserialize` that accepts
as input a dictionary and returns an instance of the `Model`.

Here is an example of the serialization of a UserProfile, as an extension
of the `django.contrib.auth` package.

```python
class UserProfile(models.Model):

    user  = models.OneToOneField( 'django.contrib.auth.User', editable=False, related_name='profile' )
    bio   = models.CharField( max_length=255, null=True, blank=True, default=None )
    birth = models.DateField( )

    def serialize(self):
        return {
            'username': self.user.username,
            'email': self.user.email,
            'name': " ".join((self.user.first_name, self.user.last_name)),
            'birthday': self.birth.strftime("%d %M, %Y"),
        }

    @classmethod
    def deserialize(klass, data):
        username = data.get('username', None)
        if username:
            try:
                return klass.objects.get(username=username)
            except klass.DoesNotExist:
                pass
        return klass(**data)
```
