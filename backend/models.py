from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

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
    email = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"