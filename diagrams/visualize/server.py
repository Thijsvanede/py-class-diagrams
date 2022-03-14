# Import flask
from flask import Flask, render_template
import os
import pathlib

# Create App
app = Flask(__name__)

@app.route('/')
def index():

    # diagram = """
    # classDiagram
    # Animal <|-- Duck
    # Animal <|-- Fish
    # Animal <|-- Zebra
    # Animal : +int age
    # Animal : +String gender
    # Animal: +isMammal()
    # Animal: +mate()
    # class Duck{
    #   +String beakColor
    #   +swim()
    #   +quack()
    # }
    # class Fish{
    #   -int sizeInFeet
    #   -canEat()
    # }
    # class Zebra{
    #   +bool is_wild
    #   +run()
    # }
    #
    # """

    print(diagram)

    return render_template(
        'tree.html',
        classname = 'test',
        diagram   = diagram,
    )

if __name__ == "__main__":

    # from spacy_embeddings.embedders.word2vec import Word2vecCBOW
    # import spacy
    # nlp = spacy.load('en_core_web_sm')
    # embedder = Word2vecCBOW(nlp, 1, 5)

    from sklearn.svm import OneClassSVM

    embedder = OneClassSVM()

    from diagrams.analyzer            import Analyzer
    from diagrams.visualize.converter import Converter
    analyzer  = Analyzer()
    converter = Converter()
    diagram = converter.mermaid(
        analyzer.analyze(embedder)
    )

    print(diagram)

    app.run()
