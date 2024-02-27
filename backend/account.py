from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,User


account = Blueprint('account', __name__)

CORS(account)
"""
def format_user(user):
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age
    }
"""


@account.route('/register', methods=['POST'])
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

    return jsonify({'message': 'Registration successful'}), 201


@account.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            return jsonify({'message': 'User does not exist'}), 404

        if user.password != password:
            return jsonify({'message': 'Invalid password'}), 401

        session['user_email'] = user.email

        return jsonify({'message': 'Login successful'}), 201

    except Exception as e:
        return jsonify({'message': str(e)}), 500



@account.route('/logout', methods=['GET'])
def logout_user():
    # Clear the session
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200


@account.route('/modify', methods=['PUT'])
def modify_user():
    try:
        data = request.json
        email = data.get('email')
        name = data.get('name')
        age = data.get('age')

        user = User.query.filter_by(email=email).first()

        if not user:
            return jsonify({'message': 'User does not exist'}), 404

        session['user_email'] = user.email
        user.name = name
        user.age = age
        db.session.commit()
        return jsonify({'message': 'User update successful'}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500
