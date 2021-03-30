## Description

Implementation of a client administration application. This application creates new customers. A client is identified by the
client ID. It is also able to edit first name, last name, telephone number, email address and postal address (providing street, postal code, city and country). APIs are available to list clients which are to be queried by last name, postal code, city and/or country with pagination. Application is also backed by a persistence layer.

## Tasks accomplished

- Developed a RESTful API to handle client data using Python3, Flask and SQLAlchemy
- Implemented API to edit first name, last name, telephone number, email address and postal address (providing street, postal code, city and country)
- Implemented all CRUD functionalities
- APIs are backed by a persistence layer
- Implemented "List Clients" API to be queried with last name, postal code, city and/or country
- "List Clients" API does not return deactivated clients
- "List Clients" API returns paginated results
- Written API tests covering all the edge scenarios

## Pre requisites

* Python 3.7 or Python 3.8
* Flask
* SQLAlchemy
* Pytest

## Installation

After cloning, create a virtual environment and install the requirements.

```
$ virtualenv .env
$ source .env/Scripts/activate
(.env) $ pip install -r requirements.txt
```

## Running

* To run the server on debug mode ON, use the following command:

```
$ cd src/client/
$ export FLASK_APP=wsgi.py
$ export FLASK_ENV=development
$ flask run
```

* To run the server on debug mode OFF, use the following command:

```
$ cd src/client/
$ python -m flask run
```

## API docs

API documents available here [Postman collection](https://www.getpostman.com/collections/6c6d0e87a36c4f0681b6)

## Overview of project workflow

1. Create ClientManager API (endpoint - /api/clients)
    * API which supports all CRUD functionalities
    * Endpoints are backed by persistence layer using SQLAlchemy ORM
    * Able to activate and deactivate clients
    
2. Create ClientList API (endpoints - /api/listClients)
    * API which supports listing all active clients
	* APIs can be queried by last name, postal code, city and/or country
	* All endpoints supports pagination
    * Endpoints are backed by persistence layer using SQLAlchemy ORM
	
3. Write test cases 
    * Unit test cases written by using pytest framework which includes pytest fixtures
    * Covered all edge cases and failure cases for all the endpoints


## API usage

1. Client Manager APIs (supports all CRUD functionalities)

    * GET -- /api/clients?client_id=client-3

    ```
    response:
        {
            "client_id": "client-3",
            "first_name": "Kristina",
            "last_name": "Jeff",
            "tel_num": "+49 8902",
            "email": "kris@gmail.com",
            "street": "torstrasse",
            "postal_code": 789,
            "city": "Frankfurt",
            "country": "DE",
            "active": "True"
        }
    ```

    * POST -- /api/clients

    ```
    payload = {
        "client_id": "client-1",
        "first_name": "John",
        "last_name": "Waf",
        "tel_num": "+1 123",
        "email": "jf@abc.com",
        "street": "main street",
        "postal_code": 123,
        "city": "Texas",
        "country": "US"
    }

    response:
        {
            "Message": "Client John Waf successfully activated."
        }
    ```

    * PUT -- /api/clients?client_id=client-1

    ```
    payload = {
        "client_id": "client-1",
        "first_name": "Sir John",
        "last_name": "Collins",
        "tel_num": "+1 123",
        "email": "jc@gmail.com",
        "street": "wolf street",
        "postal_code": 123,
        "city": "Michigan",
        "country": "US",
        "active": "True"
    }

    response:
        {
            "Message": "Client Sir John Collins data modified."
        }
    ```

    * DELETE -- /api/clients?client_id=12345

    ```
    response:
        {
            "Message": "Client 12345 deleted."
        }
    ```

2. Client List APIs

    * GET clients -- /api/listClients or /api/listClients?page=1

    ```
    response:
        [
            {
                "client_id": "client-2",
                "first_name": "Sir John",
                "last_name": "Collins",
                "tel_num": "+1 123",
                "email": "jc@gmail.com",
                "street": "wolf street",
                "postal_code": 123,
                "city": "Michigan",
                "country": "US",
                "active": "True"
            },
            {
                "client_id": "client-3",
                "first_name": "Kristina",
                "last_name": "Jeff",
                "tel_num": "+49 8902",
                "email": "kris@gmail.com",
                "street": "torstrasse",
                "postal_code": 789,
                "city": "Frankfurt",
                "country": "DE",
                "active": "True"
            }
        ]
    ```

    * GET clients by last_name -- /api/listClients?last_name=Jeff

    ```
    response:
        [
            {
                "client_id": "client-3",
                "first_name": "Kristina",
                "last_name": "Jeff",
                "tel_num": "+49 8902",
                "email": "kris@gmail.com",
                "street": "torstrasse",
                "postal_code": 789,
                "city": "Frankfurt",
                "country": "DE",
                "active": "True"
            }
        ]
    ```

    * GET clients by postal_code -- /api/listClients?postal_code=123

    ```
    response:
        [
            {
                "client_id": "client-2",
                "first_name": "Sir John",
                "last_name": "Collins",
                "tel_num": "+1 123",
                "email": "jc@gmail.com",
                "street": "wolf street",
                "postal_code": 123,
                "city": "Michigan",
                "country": "US",
                "active": "True"
            },
            {
                "client_id": "dummy-client",
                "first_name": "John",
                "last_name": "Waf",
                "tel_num": "+1 123",
                "email": "abc@abc.com",
                "street": "street",
                "postal_code": 123,
                "city": "Texas",
                "country": "US",
                "active": "True"
            }
        ]
    ```

    * GET clients by city -- /api/listClients?city=Frankfurt

    ```
    response:
        [
            {
                "client_id": "client-3",
                "first_name": "Kristina",
                "last_name": "Jeff",
                "tel_num": "+49 8902",
                "email": "kris@gmail.com",
                "street": "torstrasse",
                "postal_code": 789,
                "city": "Frankfurt",
                "country": "DE",
                "active": "True"
            }
        ]
    ```

    * GET clients by country -- /api/listClients?country=DE

    ```
    response:
        [
            {
                "client_id": "client-3",
                "first_name": "Kristina",
                "last_name": "Jeff",
                "tel_num": "+49 8902",
                "email": "kris@gmail.com",
                "street": "torstrasse",
                "postal_code": 789,
                "city": "Frankfurt",
                "country": "DE",
                "active": "True"
            },
            {
                "client_id": "client-4",
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
        ]
    ```

    * GET clients by city and country -- /api/listClients?city=Berlin&country=DE

    ```
    response:
        [
            {
                "client_id": "client-4",
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
        ]
    ```

## Deployment options

Hooray! Now our Client Administration Application is ready to use. To make this application production ready, we have several options:
1. _Deploying on Heroku_
	* Create a Procfile which is used to run a web app deployed on Heroku
	* Create requirements.txt file which is used as dependency libraries for the project
	* Create an app on Heroku and connect to the GitHub where the project is created
	* Create a deployment pipeline on Heroku
	
2. _Deploying on AWS_
	* Create API gateway REST APIs for all the endpoints
	* Additionally, API keys can be created for the REST APIs to be secured
	* Create a lambda function which corresponds to API gateway (trigger to lambda function)
	* Create a CI/CD pipeline using code build, code deploy to automatically trigger the build and deploy the service
	
_AWS resources that can be used to deploy the service:_
* API gateway -- To create REST APIs
* AWS Lambda function -- To write code without having to worry about infrastructure and scale automatically
* SSM parameter store -- To secretly store the credentials, URLs and API keys
* AWS Code Pipeline -- To automate release pipelines
* AWS CodeBuild -- To compile source code, runs tests, and produces software packages that are ready to deploy
* AWS CodeDeploy -- To deploy service that automates application deployments to Amazon EC2 instances, serverless Lambda functions, or Amazon ECS services.
* AWS KMS -- Optionally we can use AWS Key Management Service to encrypt data and to automatically rotate customer master keys(CMK)
* AWS S3 -- Optionally we can use Simple Storage Service to store metadata information and to host any static web pages, sites.
* AWS DynamoDB -- Optionally we can use DynamoDB database to store items for high availability and durability and to offload the administrative burden

API Demo screenshots available here --> [API Demo](src/demo_screenshots/README.md)