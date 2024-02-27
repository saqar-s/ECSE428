from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,Recipe

recipe = Blueprint('recipe', __name__)

CORS(recipe)
def format_recipe(recipe):
    return {
        "name": recipe.name,
        "servingSize": recipe.servingSize,
        "description": recipe.description,
        "origin": recipe.origin,
        "category": recipe.category
        
    }

@recipe.route('/createRecipe', methods=['POST'])
def create_recipe():
    print("ingredients_list")
    data = request.json
    name = data.get('name')
    ingredients_list = data.get('ingredients')
    description = data.get('description')
    email = data.get('email')

    
    #Create recipe
    ingredients = [ingredient.strip() for ingredient in ingredients_list.split(',')]
    new_recipe = Recipe(name=name, ingredients=ingredients, description=description, email=email)
    db.session.add(new_recipe)
    db.session.commit()

    #return format_recipe(new_recipe)