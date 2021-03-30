from flask import Flask
from flask_restful import Api

import flask_jwt_extended

from src.client.utils import create_logger

from src.client.clients import resources as client_resources


def create_app(config):
    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['JWT_SECRET_KEY'] = config.JWT_SECRET

    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from src.client.db import db as sqldb
    sqldb.init_app(app)

    from src.client.clients.dao.sql_dao import ClientSQLDAO

    api = Api(app)
    flask_jwt_extended.JWTManager(app)

    app_logger = create_logger(__name__)

    clients_dao = ClientSQLDAO()

    # Client manager resources
    api.add_resource(client_resources.ClientManager,
                     '/api/clients',
                     resource_class_kwargs={
                         'logger': app_logger,
                         'clients_dao': clients_dao
                     })

    # List Client resources
    api.add_resource(client_resources.ClientList,
                     '/api/listClients',
                     resource_class_kwargs={
                         'logger': app_logger,
                         'clients_dao': clients_dao
                     })

    return app