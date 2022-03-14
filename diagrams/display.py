from diagrams.analyzer         import Analyzer
from diagrams.converter        import Converter
from diagrams.visualize.server import Server
from typing                    import Any

def class_diagram(obj: Any) -> None:
    """Display object as class diagram."""
    # Setup objects
    analyzer  = Analyzer()
    converter = Converter()
    server    = Server

    # Analyze object
    graph   = analyzer.analyze(obj)
    # Convert to Mermaid string
    mermaid = converter.mermaid(graph)

    # Serve mermaid file
    server = Server()
    server.display(mermaid, type(obj).__name__)
