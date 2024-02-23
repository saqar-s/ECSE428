from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'
db = SQLAlchemy(app)
CORS(app)

class Event (db.Model):
    """
    Relation Name: Event

    Attributes:
        - id: Integer Primary Key
        - description: varchar(100) NOT NULL
        - created_at: DateTime NOT NULL default: now

    Routes:
        - create_event() --> POST (/event)
        - get_event() --> GET (/event)
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    def __repr__(self) :
        return f"Event: {self.description}"
    def __init__ (self, description):
        self. description = description

def format_event (event):
    return {
        "description": event.description,
        "id": event. id,
        "created_at": event.created_at
        }

@app.route('/event', methods = ['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    # this part is to grab the information and format it into an object to be able to use it in the frontend later on 
    return format_event(event)

@app.route('/event', methods=['GET'])
def get_event():
    events= Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {'events': event_list}

class User(db.Model):
    """
    Relation Name: User

    Attributes:
        - id: Integer Primary Key
        - name: varchar(100) NOT NULL
        - email: varchar(100) Unique NOT NULL
        - password: varchar(100) NOT NULL
        - age: Integer NOT NULL

    Routes:
        - register_user() --> POST (/register)
        - login_user() --> POST (/login)
        - logout_user() --> GET (/logout)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"
    
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

if __name__ == '__main__':
    app.run(port=8000)