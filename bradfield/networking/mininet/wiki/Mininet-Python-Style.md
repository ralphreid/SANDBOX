Mininet is currently written in the **Mininet Python Style**, which is based on the Arista Networks Python style. It mainly follows [PEP8](http://legacy.python.org/dev/peps/pep-0008), but differs in several important ways, including the following:

* Spaces are inserted inside parentheses, such as those in function definitions and calls, for readability. They may be omitted in mathematical formulas if readability would otherwise be compromised.

* `camelCase` is used for method and variable names in preference to `under_scores`. This is intended to give named identifiers (including those for classes, methods, instance variables, local variables, and parameters) a more consistent look and to reduce cognitive load. However, for easier filename typing, core Mininet package names (`nodelib`, `topolib`, etc.) are usually lowercase.

* Single-line docstrings are surrounded by single double-quotes. This makes them more compact.

* Multi-line docstrings are surrounded by triple double-quotes. This differs from single-line docstrings, which use single quotes. The ending triple-quote is at the end of the last line of docstring text, and text is lined up as shown below.

The Mininet code style can be checked (more or less) by running `make codecheck`. A utility to help with conversion from PEP8 to Mininet style is provided as `util/unpep8`.

Mininet also uses `doxypy` for automatic API documentation. We run a pre-processor which eliminates most uses of the `@` character in docstrings. For example:

```python
def someFunction( someArg, anotherArg=False ):
   """This function does something
      someArg: an argument
      anotherArg: another argument
      returns: True on success"""
   return True
```

The utility `util/doxify.py` converts this format into something that can be parsed by `doxypy`.