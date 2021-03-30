import pytest

from src.client.config import config
from src.client.db import db as sqldb
from src.client.clients.dao.sql_dao import Clients
from src.client.app import create_app


@pytest.fixture
def test_client_with_db():
    test_app = create_app(config=config['testing'])

    with test_app.app_context():
        # delete existing db
        sqldb.drop_all()

        # create new db
        sqldb.create_all()
        sqldb.session.commit()

        # create Clients
        client_1 = Clients(client_id="client-1", first_name="John", last_name="Waf", 
                                tel_num="+1 123", email="jf@abc.com", street="wolf street", 
                                postal_code="123", city="Texas", country="US", active="False")
        sqldb.session.add(client_1)
        sqldb.session.commit()

        client_2 = Clients(client_id="client-2", first_name="Tom", last_name="Schneider", 
                                tel_num="+49 567", email="tsc@abc.com", street="bierstrasse", 
                                postal_code="367", city="Berlin", country="DE", active="True")
        sqldb.session.add(client_2)
        sqldb.session.commit()

        client_3 = Clients(client_id="client-3", first_name="Kristina", last_name="Jeff", 
                                tel_num="+49 8902", email="kris@gmail.com", street="torstrasse", 
                                postal_code="789", city="Frankfurt", country="DE", active="True")
        sqldb.session.add(client_3)
        sqldb.session.commit()

    return test_app.test_client()

@pytest.fixture
def test_delete_client_with_db():
    test_app = create_app(config=config['testing'])

    with test_app.app_context():

        # create Client
        client = Clients(client_id="client-4", first_name="Thomas", last_name="Hill", 
                                tel_num="+1 456", email="thomas@gmail.com", street="spiderman street", 
                                postal_code="7844", city="Madrid", country="Spain", active="True")
        sqldb.session.add(client)
        sqldb.session.commit()

    return test_app.test_client()
