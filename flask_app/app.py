# flask packages
from flask import Flask, app
from flask_cors import CORS
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# local packages
from api.routes import create_routes

# external packages
import os

#project resources
from models.users import Users

# default configuration
default_config = {'JWT_SECRET_KEY': '${JWT_SECRET_KEY_VAR}'
                  }

default_admin = {
    'nym': '%s'%os.environ.get('ADMIN_NYM'),
    'password': '%s'%os.environ.get('ADMIN_PASSWORD'),
    'access':
    {
        'admin': 'True'
    }
}


def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)

    #configure CORS
    CORS(app=flask_app)

    # load config variables
    if 'MONGODB_URI' in os.environ:
        flask_app.config['MONGODB_SETTINGS'] = {'host': os.environ['MONGODB_URI'],
                                                'retryWrites': False}
    if 'JWT_SECRET_KEY' in os.environ:
        flask_app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
        
    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)

    # init mongoengine
    db = MongoEngine(app=flask_app)

    # init jwt manager
    jwt = JWTManager(app=flask_app)

    #create admin user
    if Users.objects(nym="%s"%os.environ.get('ADMIN_NYM')).count() == 0:
        print("creating admin user")
        admin_user = Users(**default_admin)
        admin_user.save()
    
    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    app.run(host="127.0.0.1", port=8888, debug=True)
