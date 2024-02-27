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
        "category": recipe.category,
        "image_url": recipe.image_url 
        
    }

@recipe.route('/createRecipe', methods=['POST'])
def create_recipe():
    print("ingredients_list")
    data = request.json
    name = data.get('name')
    ingredients_list = data.get('ingredients')
    description = data.get('description')

    # Find the user
    # user = User.query.filter_by(email=email).first()
    
    # if (not (name and not name.isspace())):
    #     return jsonify({'message': 'The recipe must have a name'}), 400
    
    #Create recipe
    ingredients = [ingredient.strip() for ingredient in ingredients_list.split(',')]
    new_recipe = Recipe(name=name, ingredients=ingredients, description=description)
    db.session.add(new_recipe)
    db.session.commit()

    #return format_recipe(new_recipe)

# Add picture to recipe
#https://healthyfitnessmeals.com/wp-content/uploads/2021/02/Honey-garlic-chicken-meal-prep-9.jpg 
@recipe.route('/addPicture', methods=['PUT'])
def add_picture_to_recipe(recipe_id):
    try:
        #Add picture to recipe based on the name given to the recipe
        data = request.json
        name = data.get("name") 
        
        updated_recipe = Recipe.query.filter_by(name=name).first()
        #will only add picture recipe from db if a recipe is found by the name
        if updated_recipe:
            data = request.json
            image_url = data.get('image_url')
            recipe.image_url = image_url
            db.session.commit()
        else: 
            return jsonify({'message': 'The recipe with the given name cannot be found'}), 400

    except Exception as e: 
        return jsonify({'message': str(e)}), 500
