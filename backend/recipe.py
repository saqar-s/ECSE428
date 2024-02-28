from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,Recipe

recipe = Blueprint('recipe', __name__)

CORS(recipe)
def format_recipe(recipe):
    return {
        "name": recipe.name,
        "ingredients": recipe.ingredients,
        "description": recipe.description,
        "email": recipe.email

        
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

<<<<<<< HEAD
    return format_recipe(new_recipe)

@recipe.route('/deleteRecipe', methods=['DELETE'])
def delete_recipe():
    try:
        #deleting recipe based on the name given to the recipe
        data = request.json
        name = data.get("name") 
        
        deleted_recipe = Recipe.query.filter_by(name=name).first()
        #will only delete recipe from db if a recipe is found by the name
        if deleted_recipe:
            db.session.delete(deleted_recipe)
            db.session.commit()
        else: 
            return jsonify({'message': 'The recipe with the given name cannot be found'}), 400

        return format_recipe(deleted_recipe) 
    
    except Exception as e: 
        return jsonify({'message': str(e)}), 500
    
=======
    return format_recipe(new_recipe)
>>>>>>> main
