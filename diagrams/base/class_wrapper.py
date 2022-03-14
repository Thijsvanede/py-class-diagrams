from diagrams.base.attribute import Attribute
from diagrams.base.method    import Method
from typing                  import Any, Dict, Iterable
import inspect

class Class(object):

    def __init__(self, object: Any):
        """Wrapper for class attributes."""
        # Initialise object based on class
        if inspect.isclass(object):
            self.object = None
            self.cls    = object

        # Initialise object based on object
        else:
            self.object = object
            self.cls    = type(self.object)

        # Get attributes
        self.attribute_dict = self.get_attributes()

        # Get methods
        self.method_dict = self.get_methods()

    ########################################################################
    #                          Initialise methods                          #
    ########################################################################

    def get_attributes(
            self,
            ignore_attributes: Iterable[str] = {'__module__', '__doc__'},
        ) -> Dict[str, Attribute]:
        """Get attributes from a given object.

            Parameters
            ----------
            ignore_attributes : Iterable

            Returns
            -------
            attributes : Dict[Method]
                Dict of name -> attribute in object.
            """
        # Get all attributes of class
        attributes = [
            (attribute, value) for attribute, value in self.cls.__dict__.items()
            if not inspect.isfunction(value) and
            type(value).__name__ != 'classmethod' and
            type(value).__name__ != 'staticmethod' and
            attribute not in ignore_attributes
        ]

        # Return result
        return {
            attribute: Attribute(attribute, value)
            for attribute, value in attributes
        }


    def get_methods(self) -> Dict[str, Method]:
        """Get attributes from a given object.

            Returns
            -------
            methods : Dict[Method]
                Dict of name -> method in object.
            """
        # Get all methods of class
        methods = inspect.getmembers(self.cls, lambda x:
            inspect.isfunction(x) and x.__module__ == self.cls.__module__
        )

        # Return methods of module
        return {name: Method(method) for name, method in methods}


    ########################################################################
    #                              Properties                              #
    ########################################################################

    @property
    def name(self):
        """Returns class name."""
        return self.cls.__name__

    @property
    def module(self):
        """Returns class module name."""
        if self.cls.__module__ == "builtins":
            return None
        else:
            return self.cls.__module__

    @property
    def fullname(self):
        """Returns the full name of Class as <module.name>."""
        if self.module:
            return f"{self.module}.{self.name}"
        else:
            return self.name

    @property
    def attributes(self):
        """Returns non-dunder attributes."""
        return filter(lambda x: not x.is_dunder, self.attribute_dict.values())

    @property
    def attributes_dunder(self):
        """Returns dunder attributes."""
        return filter(lambda x: x.is_dunder, self.attribute_dict.values())

    @property
    def attributes_all(self):
        """Returns all attributes."""
        return self.attribute_dict.values()

    @property
    def methods(self):
        """Returns non-dunder methods."""
        return [
            method for name, method in self.method_dict.items()
            if
            not method.is_dunder and
            not isinstance(self.cls.__dict__[name], staticmethod)
        ]

    @property
    def methods_dunder(self):
        """Returns dunder methods."""
        return filter(lambda x: x.is_dunder, self.method_dict.values())

    @property
    def methods_static(self):
        """Returns static methods."""
        return [
            method for name, method in self.method_dict.items()
            if isinstance(self.cls.__dict__[name], staticmethod)
        ]

    @property
    def methods_all(self):
        """Returns all methods."""
        return self.method_dict.values()

    @property
    def constructor(self):
        """Returns constructor method."""
        return self.method_dict.get('__init__')

    @property
    def doc(self):
        """Returns class documentation."""
        return self.cls.__doc__

    @property
    def superclasses(self):
        """Returns superclasses of class"""
        return self.cls.__bases__

    ########################################################################
    #                           Equality methods                           #
    ########################################################################

    def __eq__(self, other: Any) -> bool:
        """Return equality between Class and object."""
        return (
            isinstance(other, Class) and
            self.object == other.object and
            self.cls    == other.cls
        )

    def __hash__(self):
        """Override hash method of Class as hash method of object xor cls."""
        return hash(self.object) ^ hash(self.cls)

    ########################################################################
    #                             I/O Methods                              #
    ########################################################################

    def __str__(self) -> str:
        """Return a string representation of class."""
        return repr(self)


    def __repr__(self) -> str:
        """Return a representation string of Class."""
        return f"<diagrams.Class[{self.fullname}] object at {hex(id(self))}>"


    def mermaid(self) -> str:
        """Converts a Class object to Mermaid string representation."""
        # Initialise result
        result = f'class {self.name}{{\n'

        # Add private attributes
        for attribute in self.attributes_dunder:
            result += f'  - {attribute.type} {attribute.attribute}\n'

        # Add public attributes
        for attribute in self.attributes:
            result += f'  + {attribute.type} {attribute.attribute}\n'

        # Add constructor
        if self.constructor:
            result += f'  + {self.constructor}\n'

        # Add public methods
        for method in self.methods:
            result += f'  + {method}\n'

        # Add closing of class
        result += '}'

        # Return result
        return result


if __name__ == "__main__":
    from spacy_embeddings.embedders.word2vec import Word2vecCBOW
    import spacy
    nlp = spacy.load('en_core_web_sm')
    obj = Word2vecCBOW(nlp, 1, 5)

    tmp = Class(obj)

    print(f"{tmp.module}.{tmp.name}")

    print("\nAttributes:")
    for attribute in tmp.attributes:
        print(f"  - {attribute}")

    print("\nConstructor:")
    print(f"  - {tmp.constructor}")

    print("\nMethods:")
    for method in tmp.methods:
        print(f"  - {method}")

    print("\nMethods (static):")
    for method in tmp.methods_static:
        print(f"  - {method}")
