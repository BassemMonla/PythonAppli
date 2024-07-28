from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://root:bassem@127.0.0.1:3305/resume'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions (e.g., SQLAlchemy)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
