from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,Recipe

recipe = Blueprint('recipe', __name__)

CORS(recipe)

@recipe.route('/createRecipe', methods=['POST'])

def create_recipe():
    data = request.json
    name = data.get('name')
    ingredients_list = data.get('ingredients')
    description = data.get('description')
    email = data.get('email')
    
    try:
        # Check for empty fields
        if not all([name, ingredients_list, description, email]):
            return jsonify({'message': 'All fields are required'}), 400
        
        # Check email validity
        if '@' not in email or '.' not in email:
            return jsonify({'message': 'Invalid email address'}), 400

        #Create recipe
        ingredients = [ingredient.strip() for ingredient in ingredients_list.split(',')]
        new_recipe = Recipe(name=name, ingredients=ingredients, description=description, email=email)
        db.session.add(new_recipe)
        db.session.commit()

        return jsonify({'message': 'Recipe created successfully'}), 201
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500