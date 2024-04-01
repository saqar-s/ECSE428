from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

#favourites = db.Table('favourites', db.Column('user_email', db.String(100), db.ForeignKey('user.email'), primary_key=True), db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True))

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
    favourites = db.Column(db.ARRAY(db.Integer), nullable=True, default=[]) # a list of favourite recipe id's
    #favourite_recipes = db.relationship('Recipe', secondary=favourites, lazy='subquery', backref=db.backref('favourited_by', lazy=True))

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
    name = db.Column(db.String(100), unique= True, nullable=False)
    ingredients = db.Column(db.ARRAY(db.String(100)), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)  # Changed to LargeBinary to store binary data


    def __repr__(self):
        return f"Recipe('{self.name}')"

class CalendarEvent(db.Model):
    """
    Relation Name: Calendar

    Attributes:
        - id: Integer Primary Key
        - date: Date NOT NULL
        - recipe: Recipe NOT NULL

    Routes:
        - addToCalendar() --> POST (/addToCalendar)
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    recipeName = db.Column(db.String(100), db.ForeignKey('recipe.name'), nullable=False)
    recipe = db.relationship('Recipe', backref=db.backref('calendar_events', lazy=True))
    email = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f"Calendar Event('{self.date}')"