# Debugging

Debugging is the general term for inspecting code to determine why it isn't working as expected. As an interpreted language, Python allows you to stop execution at any time and inspect the current namespace, including all variables and objects that are in scope.

There are multiple ways to debug Python code. The three we'll try are:

1. `print` statements
2. `pdb` debugger
3. VS Code debugger

## Print Statements

While `print` isn't going to stop execution of your code, it can still give you insight into how your program is executing. My advice is to use `print` statements sparingly - if you `print` too much, it can be hard to find the information you need. A good idea is to remove `print` statements as soon as you determine the chunk of code is working as expected.

## `pdb`

The standard library includes a debugger, `pdb` (see [official documentation](https://docs.python.org/3/library/pdb.html)). This can be a very powerful tool, especially when you don't have access to an IDE such as VS Code.

```py
import pdb

# ... your code here

pdb.set_trace()
```

`pdb.set_trace()` will stop execution and open up a REPL in your shell to let you inspect the current state of the stack. I won't go into further detail here, but it's worth trying on your own.

## The Sample Code

`main.py` contains a `Stringfy` function that is supposed to turn an integer 0-99 into an English string. For example: `11` -> `"eleven"`

We'll be looking at it in a moment.

## Testing

Testing your code is always a good idea. In this directory, I've setup a `main.py` file with a function in it called `Stringify`. There are accompanying unit tests in `test_main.py`. These tests were written using Python's built-in test framework, [unittest](https://docs.python.org/3/library/unittest.html).

Before we even look at the code, we can run the tests.

```sh
python -m unittest part-6-debugging/test_main.py
```

You should see some tests fail.

## VS Code

See the [official documentation on VS Code + Python debugging](https://code.visualstudio.com/docs/python/debugging)

Install the official Python extensions from Microsoft:
1. Python ([home page](https://marketplace.visualstudio.com/items?itemName=ms-python.python))
2. Pylance ([home page](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance))

You can now run Python and set breakpoints from VS Code. The easiest way to get started is to open a Python file (any file that ends in `.py`) and then click on the "Run and Debug" menu on the left side of the screen. You should see an option to "create a launch.json file". Click it and select "Python File". You should see a new file get added to the repo under `.vscode/launch.json`. This is a configuration file for launching and debugging Python from VS Code. For now, you won't need to edit the configuration file, but you may need to edit it with more complex projects. See the official documentation linked above.

You should also note that installing these extensions should give you hints when you hover your mouse cursor over Python code. This is really helpful! Try hitting tab as you work and VS Code will help you pick variables and find methods. This is a feature in VS Code called [Intellisense](https://code.visualstudio.com/docs/editor/intellisense).

## Exercise 6.1

There are 3 bugs in the `Stringify` function. Head over to `part-6-debugging/main.py` and use your debugger to see if you can find and fix them!
