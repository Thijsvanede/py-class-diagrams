# py-class-diagrams
Python class diagram generator for class visualization of objects.
This library uses the awesome [mermaid.live](https://github.com/mermaid-js/mermaid-live-editor) tool for visualizing various diagrams.
We provide a translation from python object to a given Mermaid diagram.
See [Usage](#Usage) for a description on how to use this library.

## Installation
TODO

## Usage
To display any object as a class diagram, simply import the library and call the `class_diagram()` function:

```python
# Import library
import diagrams

# Create object to visualize, example is the sklearn OneClassSVM
from sklearn.svm import OneClassSVM
obj = OneClassSVM()

# Display object
diagrams.class_diagram(obj)
```

This code will spin up a Flask server visualizing the class diagram of the `OneClassSVM` object `obj` at `https://127.0.0.1:5000`.
