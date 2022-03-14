# Import flask
from flask     import Flask, render_template
from threading import Timer
from typing    import Optional
import webbrowser

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
            diagram  : str,
            classname: Optional[str] = None,
            port     : int           = 5000,
        ):
        """Display a specific diagram.

            Parameters
            ----------
            diagram : string
                Mermaid diagram to display.

            classname : string, optional
                Classname to use as title.

            port : int, default=5000
                Port on which to display diagram.
            """
        # Set values
        self.classname = classname or self.classname
        self.diagram   = diagram
        self.port      = port

        # Automatically open browser after starting the app
        Timer(0.5, self.open_browser).start();

        # Serve app
        self.app.run(port=self.port)


    def open_browser(self):
        """Open webbrowser"""
        webbrowser.open_new_tab(f'http://127.0.0.1:{self.port}/')
