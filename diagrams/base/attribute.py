from typing import Any, Optional

class Attribute(object):

    def __init__(self, attribute: str, value: Optional[Any] = None) -> None:
        """Wrapper for attribute attributes."""
        # Store values
        self.attribute = attribute
        self.value     = value

    ########################################################################
    #                              Properties                              #
    ########################################################################

    @property
    def type(self) -> Any:
        """Returns method signature."""
        return type(self.value).__name__

    @property
    def is_dunder(self) -> bool:
        """Returns whether method is constructor."""
        return self.attribute.startswith('__') and self.attribute.endswith('__')

    ########################################################################
    #                                String                                #
    ########################################################################

    def __str__(self) -> str:
        """Return a string representation of the method."""
        return f"{self.attribute}: {self.type}"

    def __repr__(self) -> str:
        """Return a representation of the method."""
        return f"<Attribute[{self.attribute}] object at {hex(id(self))}>"
