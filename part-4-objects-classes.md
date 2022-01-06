# Objects

An object is an instantiated piece of data with some combination of properties and methods attached to it. For instance, a string is an object. It has methods you can call to perform actions with the string.

(see the [official docs on `str`](https://docs.python.org/3/library/stdtypes.html#str) for the full list of methods)

```py
some_string = "this is a string"

# a method that tells you if the string is upper cased
some_string.isupper() # False

# a method to actually uppercase the string
some_string.upper() # "THIS IS A STRING"

# there are many methods to find substrings
some_string.index("a") # 8

# you can split strings into a list of substrings
some_string.split(" ") # ['this', 'is', 'a', 'string']
```

Both methods and properties are accessed using dot notation.

## Classes

See the [official docs on classes](https://docs.python.org/3/tutorial/classes.html)

You can create your own types of objects using classes. A class takes the following basic form:

```py
class NameOfClass(optional_super_class):
    """
    A description of this class
    """
    def __init__(self, arg1, arg2):
        # the class constructor. this method is run when you instantiate a new instance of this class
        # it must take `self` as the first argument

        # this is an example of setting a property on this instance
        self.property1 = "this is a property"

        # this is an example of using an argument passed to the constructor to create a property
        self.property2 = arg1

        do_more_work_to_setup_object()

    def method1(self):
        """
        A function that lives on this object. think of this method as something this object can do. the method has access to all other properties and methods on the object
        """

        # do work here

        pass

    def method2(self, arg3):
        """
        A method that takes another argument and uses the properties on the object. it returns a value
        """

        return self.arg2 * arg3
```

Let's look at a concrete example of a class and object in part-4-objects-classes.py.

## Exercise 4.1

Do you have a dog at home? Make a `Dog` object representing them. (If you don't have a dog, feel free to make one up.)

## Exercise 4.2

What do you see when you run `print(hawkeye)`?

The `__str__` method can be added to any class to change how its objects are printed. Add the `__str__` method to `Dog` to make it print "{name}, {breed}" instead. You should see the following:

```py
print(hawkeye) # "Hawkeye, husky"
```

See the [official documentation on `__str__`](https://docs.python.org/3/reference/datamodel.html#object.__str__).
