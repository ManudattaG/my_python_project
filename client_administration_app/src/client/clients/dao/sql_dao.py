from src.client.clients.dao import abstract_dao
from src.client.db import db
from flask_restful import Resource, fields, marshal_with, request

ROWS_PER_PAGE = 2


class Clients(db.Model):
    client_id = db.Column(db.String(10), primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    tel_num = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    street = db.Column(db.String(80), unique=False, nullable=False)
    postal_code = db.Column(db.Integer, unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    country = db.Column(db.String(80), unique=False, nullable=False)
    active = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, client_id, first_name, last_name, tel_num, email, street, postal_code, city, country, active):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.tel_num = tel_num
        self.email = email
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.active = active

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ClientSQLDAO(abstract_dao.AbstractClientsDAO):
    """
    Implements the in sql data access object for the Clients
    """
    def find_client_by_last_name(self, last_name):
        page = request.args.get('page', 1, type=int)
        clients = Clients.query.filter_by(last_name=last_name, active="True").paginate(page=page, per_page=ROWS_PER_PAGE).items
        if not clients:
            msg = {'Message': f'Clients with last_name {last_name} not found.'}
            status_code = 404
            return msg, status_code
        return list(map(lambda client: client.as_dict(), clients)), 200

    def find_client_by_postal_code(self, postal_code):
        page = request.args.get('page', 1, type=int)
        clients = Clients.query.filter_by(postal_code=postal_code, active="True").paginate(page=page, per_page=ROWS_PER_PAGE).items
        if not clients:
            msg = {'Message': f'Clients with postal_code {postal_code} not found.'}
            status_code = 404
            return msg, status_code
        return list(map(lambda client: client.as_dict(), clients)), 200

    def find_client_by_city(self, city):
        page = request.args.get('page', 1, type=int)
        clients = Clients.query.filter_by(city=city, active="True").paginate(page=page, per_page=ROWS_PER_PAGE).items
        if not clients:
            msg = {'Message': f'Clients with city {city} not found.'}
            status_code = 404
            return msg, status_code
        return list(map(lambda client: client.as_dict(), clients)), 200

    def find_client_by_country(self, country):
        page = request.args.get('page', 1, type=int)
        clients = Clients.query.filter_by(country=country, active="True").paginate(page=page, per_page=ROWS_PER_PAGE).items
        if not clients:
            msg = {'Message': f'Clients with country {country} not found.'}
            status_code = 404
            return msg, status_code
        return list(map(lambda client: client.as_dict(), clients)), 200

    def find_client_by_cityandcountry(self, city, country):
        page = request.args.get('page', 1, type=int)
        clients = Clients.query.filter_by(city=city, country=country, active="True").paginate(page=page, per_page=ROWS_PER_PAGE).items
        if not clients:
            msg = {'Message': f'Clients with city {city} and country {country} not found.'}
            status_code = 404
            return msg, status_code
        return list(map(lambda client: client.as_dict(), clients)), 200

    def get_all_clients(self):
        page = request.args.get('page', 1, type=int)
        clients = Clients.query.filter_by(active="True").paginate(page=page, per_page=ROWS_PER_PAGE).items
        return list(map(lambda client: client.as_dict(), clients)), 200