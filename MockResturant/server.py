from flask_app import app
from flask_app.controllers import main

if __name__ == "__main__":
    app.run(debug=True)


# shortcuts for the terminal
# python -m pip install flask - installs flask
# python -m pipenv shell - creates dev environment
# py server.py - runs on local host
