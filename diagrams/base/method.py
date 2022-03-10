import inspect
import types

class Method(object):

    def __init__(self, method) -> None:
        """Wrapper for method attributes."""
        # Store method
        self.method = method

    ########################################################################
    #                              Properties                              #
    ########################################################################

    @property
    def name(self) -> str:
        """Returns method name."""
        return self.method.__name__

    @property
    def signature(self) -> inspect.Signature:
        """Returns method signature."""
        return inspect.signature(self.method)

    @property
    def parameters(self) -> inspect.Parameter:
        """Returns the parameters of method."""
        return self.signature.parameters

    @property
    def doc(self) -> str:
        """Returns method documentation."""
        return inspect.getdoc(self.method)

    @property
    def is_constructor(self) -> bool:
        """Returns whether method is constructor."""
        return self.name == '__init__' or self.name == '__new__'

    @property
    def is_dunder(self) -> bool:
        """Returns whether method is constructor."""
        return self.name.startswith('__') and self.name.endswith('__')

    ########################################################################
    #                                String                                #
    ########################################################################

    def __str__(self) -> str:
        """Return a string representation of the method."""
        return f"{self.name}{self.signature}"

    def __repr__(self) -> str:
        """Return a representation of the method."""
        return f"<Method[{self.name}] object at {hex(id(self))}>"
