from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from models import User
from app import db, app

def format_user(user):
    return {
        "id": user. id,
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "age": user.age
    }

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')

    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400

    # Create a new user
    new_user = User(name=name, email=email, password=password, age=age)
    db.session.add(new_user)
    db.session.commit()

    return format_user(new_user)

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.password == password:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Store user ID in session
    session['user_id'] = user.id

    return format_user(user)

@app.route('/logout', methods=['GET'])
def logout_user():
    # Clear the session
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200