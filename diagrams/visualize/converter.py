import networkx as nx

class Converter(object):

    ########################################################################
    #                              Converters                              #
    ########################################################################

    def mermaid(self, graph : nx.DiGraph) -> str:
        """Convert a graph representation of class layout to a Mermaid string.

            Parameters
            ----------
            graph : nx.DiGraph
                Graph representation of class layout to convert to Mermaid
                string.

            Returns
            -------
            result : string
                Mermaid string representation of class layout.
            """
        # Initialise result
        result = "classDiagram\n"

        # Extract classes and relations from graph
        classes   = set(graph.nodes)
        relations = [
            (u, data.get('relation'), v)
            for u, v, data in graph.edges(data=True)
        ]

        # Add classes
        for cls in classes:
            # Get Mermaid string of class
            mermaid_string = cls.mermaid()

            # Indent mermaid_string
            mermaid_string = '\n'.join(
                f'  {line}' for line in mermaid_string.split('\n')
            )

            result += f"{mermaid_string}\n\n"

        # Add relations
        for source, relation, target in relations:
            result += f'  {source.name} <|-- {target.name}\n'

        # Return result
        return result
