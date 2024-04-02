from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,User


account = Blueprint('account', __name__)

CORS(account)

def format_user(user):
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age
    }


@account.route('/register', methods=['POST'])
def register_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')

    # Check for empty fields
    if not all([name, email, password, age]):
        return jsonify({'message': 'All fields are required'}), 400

    # Check email validity
    if '@' not in email or '.' not in email:
        return jsonify({'message': 'Invalid email address'}), 400
    
    # Check age validity
    if age < 0 or age > 1000:
        return jsonify({'message': 'Invalid age'}), 400
    
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
        user_data = {
            'email': user.email,
            'name': user.name,
            'age': user.age
        }

        return jsonify({'message': 'Login successful','data':user_data},), 201

    except Exception as e:
        return jsonify({'message': str(e)}), 500



@account.route('/logout', methods=['GET'])
def logout_user():
    # Clear the session
    session.clear()
    return jsonify({'message': 'Logout successful', }), 200


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
        
        if '@' not in email or '.' not in email:
            return jsonify({'message': 'Invalid email address'}), 400
        
        if int(age) < 0 or int(age) > 1000:
            return jsonify({'message': 'Invalid age'}), 400
        
        if name == '':
            return jsonify({'message': 'Name cannot be blank'}), 400
        
        if int(age) != age:
            return jsonify({'message': 'Age must be an integer'}), 400

        session['user_email'] = user.email

        db.session.commit()
        return jsonify({'message': 'User update successful' }), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Due to current testing issues, the current delete function requires the email and password.
@account.route('/delete', methods=['DELETE'])
def delete_account():
    try:
        #Get email and password
        email = request.args.get('email')
        
        user = User.query.filter_by(email=email).first()
        # Check if email does not exist
        if not user:
            return jsonify({'message': 'Not an active account'}), 400
        
        session['user_email'] = user.email
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deletion successful'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@account.route('/searchuser', methods=['GET'])
def search_user():
    # email = session['user_email']
    # existing_user = User.query.filter_by(email = session['user_email']).first()
    # if not existing_user:
    #     session.clear()
    #     return jsonify({'message': 'Please log In again'}), 405
    users = User.query.all()
    if not users:
        return jsonify({'message': 'There are no users in the database'}), 406
    newlist = []

    for user in users:
        newlist.append(user.name)

    tup = tuple(newlist)

    return jsonify(tup),203