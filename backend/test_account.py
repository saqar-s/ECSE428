from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,User
import pytest
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# python -m pytest
#Endpoint might be problematic!!
ENDPOINT = "http://localhost:3000"

def test_call_endpoint():
    response = request.get(ENDPOINT)
    assert response.status_code == 200
    

def account_payload():
    payload = {
        "name" : "JC",
        "email" : "JCB1234@gmail.com",
        "password" : "Qwerty123",
        "age" : "11"
    }
    return payload

def test_create_account1():
    #Given
    name = "JC"
    email = "JCB1234@gmail.com"
    password = "Qwerty123"
    age = 11
    new_user = User(name=name, email=email, password=password, age=age)
    #When
    db.add(new_user)
    db.commit()
    #Then
    savedUser = db.get_or_404(new_user)
    assert savedUser is not None
    assert savedUser.name == new_user.name
    assert savedUser.email == new_user.email
    assert savedUser.password == new_user.password
    assert savedUser.age == new_user.age

def test_create_account2():
    payload = account_payload()
    response = request.put(ENDPOINT + "/signup/register",json = payload)
    assert response.status_code == 200

def test_delete_account1():
    #Given
    name = "JC"
    email = "JCB1234@gmail.com"
    password = "Qwerty123"
    age = 11
    new_user = User(name=name, email=email, password=password, age=age)
    db.session.add(new_user)
    db.session.commit()
    #When
    db.session.delete(new_user)
    db.session.commit()
    #Then
    user = User.query.filter_by(new_user.email).first()
    assert user is None

def test_delete_account2():
    payload = account_payload()
    responseCreate = request.put(ENDPOINT + "/signup/register",json = payload)
    assert responseCreate.status_code == 200
    
    responseDelete = request.delete(ENDPOINT + "/signup/delete")
    assert responseDelete.status_code == 200
    

