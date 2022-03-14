# Import flask
from flask  import Flask, render_template
from typing import Optional

class Server(object):

    def __init__(self):
        """"""
        # Create Flask app
        self.app       = Flask(__name__)
        self.classname = ""
        self.diagram   = ""

        # Add route
        self.app.add_url_rule('/', view_func=self.index)

    def index(self):
        return render_template(
            'mermaid.html',
            classname = self.classname,
            diagram   = self.diagram,
        )

    def display(
            self,
            diagram: str,
            classname: Optional[str] = None
        ):
        """Display a specific diagram.

            Parameters
            ----------
            diagram : string
                Mermaid diagram to display.

            classname : string, optional
                Classname to use as title.
            """
        # Set values
        self.classname = classname or self.classname
        self.diagram   = diagram

        # Serve app
        self.app.run()
