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
    
class Recipe(db.Model):
    """
    Relation Name: Recipe

    Attributes:
        - id: Integer Primary Key
        - name: varchar(100) NOT NULL
        - ingredients: Array[Strings] NOT NULL
        - description: varchar(10000) NOT NULL
        - foodie: User NOT NULL
        - image: LargeBinary NULLABLE

    Routes:
        - create_recipe() --> POST (/createRecipe)
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.ARRAY(db.String(100)), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)  # Changed to LargeBinary to store binary data

  

    def __repr__(self):
        return f"Recipe('{self.name}')"