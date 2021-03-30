import pytest
import json

def test_create_client(test_client_with_db):
    """
    Call /api/clients
    Create new clients
    """

    url = '/api/clients'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    data = {
        "client_id": "54321",
        "first_name": "Lucas",
        "last_name": "Schaefer",
        "tel_num": "+49 123456789",
        "email": "lucas.schaefer@gmail.com",
        "street": "GartenStrasse",
        "postal_code": "49 3462",
        "city": "Stuttgart",
        "country": "DE"
    }
    resp = test_client_with_db.post(url,
                                    data=json.dumps(data),
                                    headers=headers)

    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert "successfully activated" in resp.json["Message"] #If client is successfully activated


def test_get_client(test_client_with_db):
    """
    Call /api/clients?client_id=client_id
    Get client by id
    """

    url = '/api/clients?client_id=client-3'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    resp = test_client_with_db.get(url, headers=headers)

    # If client is successfully activated
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert "True" in resp.json["active"]

    # If client not found
    url = '/api/clients?client_id=1234'
    resp = test_client_with_db.get(url, headers=headers)

    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]

def test_update_client(test_client_with_db):
    """
    Call /api/clients?client_id=client_id
    Update existing clients
    """

    url = '/api/clients?client_id=client-2'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    data = {
        "client_id": "client-2",
        "first_name": "Tom",
        "last_name": "Schneider",
        "tel_num": "+49 567",
        "email": "tsc@abc.com",
        "street": "bierstrasse",
        "postal_code": 367,
        "city": "Berlin",
        "country": "DE",
        "active": "True"
    }
    resp = test_client_with_db.put(url,
                                    data=json.dumps(data),
                                    headers=headers)

    # If client is successfully activated
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert "data modified" in resp.json["Message"]

    # If client is deactivated
    url = '/api/clients?client_id=client-1'
    resp = test_client_with_db.get(url, headers=headers)
    assert "deactivated" in resp.json["Message"]

    # If client not found
    url = '/api/clients?client_id=1234'
    resp = test_client_with_db.put(url,
                                    data=json.dumps(data),
                                    headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]

def test_delete_client(test_delete_client_with_db):
    """
    Call /api/clients?client_id=client_id
    Delete client by id
    """

    url = '/api/clients?client_id=client-4'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    resp = test_delete_client_with_db.delete(url, headers=headers)

    # If client is successfully deleted
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert "deleted" in resp.json["Message"]

    # If client not found
    url = '/api/clients?client_id=1234'
    resp = test_delete_client_with_db.delete(url, headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]