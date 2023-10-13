from flask import Flask


# Create the application instance.
# __name__ is the name of the current Python module.
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# If app.py is run directly, start the server.
if __name__ == '__main__':
    app.run()