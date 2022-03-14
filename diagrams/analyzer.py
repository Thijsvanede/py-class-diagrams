from typing        import Optional
from diagrams.base import Class
import networkx as nx

class Analyzer(object):

    ########################################################################
    #                            Analyze method                            #
    ########################################################################

    def analyze(
            self,
            obj : object,
            tree: Optional[nx.DiGraph] = None,
        ) -> nx.DiGraph:
        """Get the class tree of an object.

            Parameters
            ----------
            obj : object
                Object for which to generate the class tree.

            tree : Optional[nx.Digraph], optional
                If given, use the tree as a basis.

            Returns
            -------
            result : nx.DiGraph
                Graph representation of class tree with the object class as
                root node (`result.nodes[0]`).
            """
        # Create tree if no tree exists
        if tree is None:
            tree = nx.DiGraph()

        # Transform object to class
        if not isinstance(obj, Class):
            obj = Class(obj)

        # Add node to tree if it does not already exists
        if not tree.has_node(obj):
            tree.add_node(obj)

        # Add super classes to tree
        for superclass in obj.superclasses:
            # Get superclass as class
            superclass = Class(superclass)

            # Add relation if it does not already exists
            if not tree.has_edge(superclass, obj):
                # Add relation
                tree.add_edge(superclass, obj, relation='superclass')
                # Add recursion
                tree = self.analyze(
                    obj  = superclass,
                    tree = tree,
                )

        # Return resulting tree
        return tree
