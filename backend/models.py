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
        - servingSize: Integer NOT NULL
        - origin: varchar(100) NOT NULL
        - category: varchar(100) NOT NULL
        - description: varchar(10000) NOT NULL
        - foodie: User NOT NULL

    Routes:
        - create_recipe() --> POST (/createRecipe)
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    servingSize = db.Column(db.Integer, nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    # user = db.Columns(db.Integer, db.ForeignKey('user.email'))
    # user = db.relationship('User', back_populates='recipes')

  

    def __repr__(self):
        return f"Recipe('{self.name}', '{self.user}')"