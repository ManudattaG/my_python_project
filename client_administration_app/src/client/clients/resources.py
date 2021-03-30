from flask import jsonify
from flask_restful import Resource, fields, marshal_with, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlalchemy

from .dao.sql_dao import Clients
from src.client.db import db


class BaseResource(Resource):
    def __init__(self, **kwargs):
        self.logger = kwargs['logger']
        self.clients_dao = kwargs['clients_dao']


class ClientList(BaseResource):
    """
    Resource for all the clients
    """
    def get(self):
        """
        Return a JSON array of all clients
        """
        # Search by last_name
        args = request.args
        if 'last_name' in args:
            self.logger.info('GET /listClients?last_name={}'.format(args['last_name']))
            client, status_code = self.clients_dao.find_client_by_last_name(args['last_name'])
            return client, status_code

        # Search by postal_code
        args = request.args
        if 'postal_code' in args:
            self.logger.info('GET /listClients?postal_code={}'.format(args['postal_code']))
            client, status_code = self.clients_dao.find_client_by_postal_code(args['postal_code'])
            return client, status_code

        # Search by city
        args = request.args
        if 'city' in args and 'country' not in args:
            self.logger.info('GET /listClients?city={}'.format(args['city']))
            client, status_code = self.clients_dao.find_client_by_city(args['city'])
            return client, status_code

        # Search by country
        args = request.args
        if 'country' in args and 'city' not in args:
            self.logger.info('GET /listClients?country={}'.format(args['country']))
            client, status_code = self.clients_dao.find_client_by_country(args['country'])
            return client, status_code

        # Search by city and country
        args = request.args
        if 'city' in args and 'country' in args:
            self.logger.info('GET /listClients?city={}&country={}'.format(args['city'], args['country']))
            client, status_code = self.clients_dao.find_client_by_cityandcountry(args['city'], args['country'])
            return client, status_code

        self.logger.info('GET /listClients')
        client, status_code = self.clients_dao.get_all_clients()
        return client, status_code


class ClientManager(BaseResource):
    """
    Create, Get, Update and Delete resources
    """
    @staticmethod
    def get():
        try: client_id = request.args['client_id']
        except Exception as _: client_id = None

        if not client_id:
            clients = Clients.query.filter_by(active="True").all()
            return list(map(lambda client: client.as_dict(), clients)), 200
        client = Clients.query.get(client_id)
        if(client is not None):
            if(client.active == "True"):
                return json_result(client), 200
            elif(client.active == "False"):
                return {
                    'Message': f'Client {client_id} is deactivated.'
                }, 200
        else:
            return {
                'Message': f'Client {client_id} not found.'
            }, 404


    @staticmethod
    def post():
        client_id = request.json['client_id']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        tel_num = request.json['tel_num']
        email = request.json['email']
        street = request.json['street']
        postal_code = request.json['postal_code']
        city = request.json['city']
        country = request.json['country']
        active = "True"

        client = Clients(client_id, first_name, last_name, tel_num, email, street, postal_code, city, country, active)
        db.create_all()
        db.session.add(client)
        db.session.commit()
        return {
            'Message': f'Client {first_name} {last_name} successfully activated.'
        }, 200

    @staticmethod
    def put():
        try: client_id = request.args['client_id']
        except Exception as _: client_id = None
        if not client_id:
            return { 'Message': 'Must provide the client ID' }
        client = Clients.query.get(client_id)
        if(client is not None):
            if(client.active == "True"):
                pass
            elif(client.active == "False"):
                return {
                    'Message': f'Client {client_id} is deactivated. Re-activate to update the client data.'
                }, 200
        else:
            return {
                'Message': f'Client {client_id} not found to update the data. Please check the client_id.'
            }, 404

        first_name = request.json['first_name']
        last_name = request.json['last_name']
        tel_num = request.json['tel_num']
        email = request.json['email']
        street = request.json['street']
        postal_code = request.json['postal_code']
        city = request.json['city']
        country = request.json['country']
        active = request.json['active']

        client.first_name = first_name 
        client.last_name = last_name 
        client.tel_num = tel_num
        client.email = email 
        client.street = street
        client.postal_code = postal_code
        client.city = city
        client.country = country
        client.active = active

        db.session.commit()
        return {
            'Message': f'Client {first_name} {last_name} data modified.'
        }, 200

    @staticmethod
    def delete():
        try: client_id = request.args['client_id']
        except Exception as _: client_id = None
        if not client_id:
            return { 'Message': 'Must provide the client ID' }
        client = Clients.query.get(client_id)

        if(client is not None):
            db.session.delete(client)
            db.session.commit()
            
            return {
                'Message': f'Client {str(client_id)} deleted.'
            }, 200
        else:
            return {
                'Message': f'Client {client_id} not found to delete. Please check the client_id.'
            }, 404

def json_result(client):
    client_dict = {}
    client_dict["client_id"] = client.client_id
    client_dict["first_name"] = client.first_name
    client_dict["last_name"] = client.last_name
    client_dict["tel_num"] = client.tel_num
    client_dict["email"] = client.email
    client_dict["street"] = client.street
    client_dict["postal_code"] = client.postal_code
    client_dict["city"] = client.city
    client_dict["country"] = client.country
    client_dict["active"] = client.active
    return(client_dict)