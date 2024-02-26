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
    data = request.json
    name = data.get('name')
    servingSize = data.get('servingSize')
    origin = data.get('origin')
    category = data.get('category')
    description = data.get('description')

    # Find the user
    # user = User.query.filter_by(email=email).first()

    if (not (name and not name.isspace())):
        return jsonify({'message': 'The recipe must have a name'}), 400
    
    #Create recipe
    new_recipe = Recipe(name=name, servingSize=servingSize, origin=origin, category=category, description=description)
    db.session.add(new_recipe)
    db.session.commit()

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
    