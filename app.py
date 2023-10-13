from flask import Flask

from src.configs.database import Configs, db
from src.routes.movies_route import movie_router


# Create the application instance.
# __name__ is the name of the current Python module.
app = Flask(__name__)

app.register_blueprint(movie_router, url_prefix='/movies')

app.config.from_object(Configs)

db.init_app(app)

# If app.py is run directly, start the server.
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()