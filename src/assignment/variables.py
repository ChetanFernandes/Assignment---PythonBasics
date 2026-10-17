def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_variable_name_valid(name):
    """Return True if name is a valid Python identifier string for a variable name."""
    return isinstance(name, str) and name.isidentifier()
