import pytest


def test_get_client_by_last_name(test_client_with_db):
    """
    Call /api/listClients?last_name=last_name
    Get clients by last_name
    """

    url = '/api/listClients?last_name=Schneider'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    resp = test_client_with_db.get(url, headers=headers)

    # If client is successfully activated
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    for client in resp.json:
        assert "True" in client["active"]

    # If client not found
    url = '/api/listClients?last_name=Collins'
    resp = test_client_with_db.get(url, headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]

def test_get_client_by_postal_code(test_client_with_db):
    """
    Call /api/listClients?postal_code=postal_code
    Get clients by postal_code
    """

    url = '/api/listClients?postal_code=789'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    resp = test_client_with_db.get(url, headers=headers)

    # If client is successfully activated
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    for client in resp.json:
        assert "True" in client["active"]
        
    # If client not found
    url = '/api/listClients?postal_code=123'
    resp = test_client_with_db.get(url, headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]

def test_get_client_by_city(test_client_with_db):
    """
    Call /api/listClients?city=city
    Get clients by city
    """

    url = '/api/listClients?city=Frankfurt'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    resp = test_client_with_db.get(url, headers=headers)

    # If client is successfully activated
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    for client in resp.json:
        assert "True" in client["active"]

    # If client not found
    url = '/api/listClients?city=Munich'
    resp = test_client_with_db.get(url, headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]

def test_get_client_by_country(test_client_with_db):
    """
    Call /api/listClients?country=country
    Get clients by country
    """

    url = '/api/listClients?country=DE'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    resp = test_client_with_db.get(url, headers=headers)

    # If client is successfully activated
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    for client in resp.json:
        assert "True" in client["active"]

    # If client not found
    url = '/api/listClients?country=France'
    resp = test_client_with_db.get(url, headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]

def test_get_client_by_cityandcountry(test_client_with_db):
    """
    Call /api/listClients?city=city&country=country
    Get clients by country
    """

    url = '/api/listClients?city=Frankfurt&country=DE'
    mimetype = 'application/json'
    headers = {'Content-Type': mimetype, 'Accept': mimetype}
    resp = test_client_with_db.get(url, headers=headers)

    # If client is successfully activated
    assert resp.content_type == mimetype
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    for client in resp.json:
        assert "True" in client["active"]

    # If client not found
    url = '/api/listClients?city=Munich&country=DE'
    resp = test_client_with_db.get(url, headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]

    url = '/api/listClients?city=Madrid&country=Spain'
    resp = test_client_with_db.get(url, headers=headers)
    assert resp.content_type == mimetype
    assert resp.status_code == 404
    assert isinstance(resp.json, dict)
    assert "not found" in resp.json["Message"]