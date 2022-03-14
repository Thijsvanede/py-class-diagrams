# Import flask
from flask import Flask, render_template

# Create App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'tree.html',
        classname = 'test',
        diagram   = diagram,
    )

if __name__ == "__main__":
    # Example with OneClassSVM
    from sklearn.svm import OneClassSVM

    # Create object
    obj = OneClassSVM()

    from diagrams.analyzer            import Analyzer
    from diagrams.visualize.converter import Converter
    analyzer  = Analyzer()
    converter = Converter()
    diagram = converter.mermaid(
        analyzer.analyze(obj)
    )

    app.run()
