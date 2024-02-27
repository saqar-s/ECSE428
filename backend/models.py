from flask import Flask, jsonify, request
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

    Routes:
        - create_recipe() --> POST (/createRecipe)
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.ARRAY(db.String(100)), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    email = db.Column(db.String(100), nullable=False)

  

    def __repr__(self):
        return f"Recipe('{self.name}')"
    
 # View all recipes for the dashboard
@app.route('/dashboard/recipes', methods=['GET'])
def view_all_recipes():
    """
    Route to view all recipes for the dashboard
    """
    try:
        recipes = Recipe.query.all()
        recipe_list = []
        for recipe in recipes:
            recipe_data = {
                'id': recipe.id,
                'name': recipe.name,
                'ingredients': recipe.ingredients,
                'description': recipe.description,
                'email': recipe.email
            }
            recipe_list.append(recipe_data)
        return jsonify({'recipes': recipe_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to view all recipes associated with a specific user
@app.route('/user/<user_email>/recipes', methods=['GET'])
def view_user_recipes(user_email):
    try:
        user = User.query.get(user_email)
        if user:
            user_recipes = user.recipes
            recipe_list = []
            for recipe in user_recipes:
                recipe_data = {
                    'id': recipe.id,
                    'name': recipe.name,
                    'ingredients': recipe.ingredients,
                    'description': recipe.description,
                    'email': recipe.email
                }
                recipe_list.append(recipe_data)
            return jsonify({'user_recipes': recipe_list}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)