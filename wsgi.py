from flask import Flask
from markupsafe import escape

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/<name>")
def hello_name(name):
    return f'Hello {escape(username)}'

if __name__ == "__main__":
    application.run()
