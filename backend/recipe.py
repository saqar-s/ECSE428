from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,Recipe,User

recipe = Blueprint('recipe', __name__)

CORS(recipe)
def format_recipe(recipe):
    return {
        "name": recipe.name,
        "email": recipe.foodie.email,
        "servingSize": recipe.servingSize,
        "description": recipe.description,
        "origin": recipe.origin,
        "category": recipe.category
        
    }

@recipe.route('/createRecipe', methods=['POST'])
def register_user():
    data = request.json
    name = data.get('name')
    # email = data.get('email')
    servingSize = data.get('servingSize')
    description = data.get('description')
    origin = data.get('origin')
    category = data.get('category')

    # Find the user
    # user = User.query.filter_by(email=email).first()

    if (not (name and not name.isspace())):
        return jsonify({'message': 'The recipe must have a name'}), 400
    new_recipe = Recipe(name, servingSize, origin, category, description)
    db.session.add(new_recipe)
    db.session.commit()

    return format_recipe(new_recipe)