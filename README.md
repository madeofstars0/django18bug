### Django 1.8 Postgres ArrayField Bug

I found an issue when upgrading to Django 1.8 and using the new ArrayField. The code here is setup to show the problems. I have reproduced this problem on OSX 10.10 with Postgresql 9.4 and in the provided Vagrant environment (Ubuntu 14.04, Postgresql 9.3).

Take a look at the tests.

#### An instance method on a model - This doesn't work

```
def add_to_array(self, item):
    if item not in self.array_field:
        self.array_field.append(item)
```

#### This workaround 'works'

```
def add_to_array(self, item):
    existing = self.array_field

    if item not in self.array_field:
        self.array_field = existing + [item]
```