import base64
from flask import request, jsonify, session, Blueprint
from flask_cors import CORS
from models import db,Recipe, User
import array

recipe = Blueprint('recipe', __name__)

CORS(recipe)

@recipe.route('/createRecipe', methods=['POST'])
def create_recipe():
    data = request.json
    name = data.get('name')
    ingredients_list = data.get('ingredients')
    description = data.get('description')
    email = data.get('email')
    image_data_base64 = data.get('image')
   
    
    try:
        # Check for empty fields
        if not all([name, ingredients_list, description, email]):
            # Return error message
            return jsonify({'message': 'All fields are required'}), 400
        

        # Check email validity
        if '@' not in email or '.' not in email:
            return jsonify({'message': 'Invalid email address'}), 400
        
        # Decode Base64-encoded image data back to bytes
        if image_data_base64 is not None:
            image = base64.b64decode(image_data_base64)
        else:
            image = None

        #Create recipe
        ingredients = [ingredient.strip() for ingredient in ingredients_list.split(',')]
        new_recipe = Recipe(name=name, ingredients=ingredients, description=description, email=email, image=image)
        db.session.add(new_recipe)
        db.session.commit()

        return jsonify({'message': 'Recipe created successfully', 'id': new_recipe.id}), 201
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
# @recipe.route('/addImage', methods=['PUT'])
# def add_image():
#     data = request.json
#     name = data.get('name')
#     image_data_base64 = data.get('image')
    
#     try:
#         # Check for empty fields
#         if not (name):
#             # Return error message
#             return jsonify({'message': 'Name field required'}), 400
        
#         # Decode Base64-encoded image data back to bytes
#         if image_data_base64 is not None:
#             image = base64.b64decode(image_data_base64)
#         else:
#             image = None

        
#         # Update recipe
#         recipe = Recipe.query.filter_by(name=name).first()
#         recipe.image = image
#         db.session.commit()
        
#         return jsonify({'message': 'Image added successfully'}), 200
    
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500

    
@recipe.route('/getRecipes', methods=['GET'])
def get_recipes():
    try:
        # Check if the request is for a specific user's recipes
        user_email = request.args.get('user_email')
        if user_email:
            recipes = Recipe.query.filter_by(email=user_email).all()
        else:
            recipes = Recipe.query.all()
            
        recipe_list = []
        for recipe in recipes:
            # Encode the image data as Base64
            if recipe.image:
                image_base64 = base64.b64encode(recipe.image).decode('utf-8')
            else:
                image_base64 = None
                
            recipe_list.append({
                'id': recipe.id,
                'name': recipe.name,
                'ingredients': recipe.ingredients,
                'description': recipe.description,
                'email': recipe.email,
                'image': image_base64
            })
        return jsonify({'recipes': recipe_list}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    


##method to delete a recipe by id
##check if recipe id is empty
##check if db has a recipe stored with that id
##delete the recipe
@recipe.route('/deleteRecipe', methods=['DELETE'])
def delete_recipe():
    data = request.json
    id = data.get('id')
    try:
        # Check for empty fields
        if not (id):
            # Return error message
            return jsonify({'message': 'ID field required'}), 400
        
        # Delete recipe
        #if recipe exists, delete it
        recipe = Recipe.query.filter_by(id=id).first()
        if recipe is None:
            return jsonify({'message': 'No recipe exists with that ID'}), 404
        
        db.session.delete(recipe)
        db.session.commit()

        
        return jsonify({'message': 'Recipe deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@recipe.route('/removeRecipeFromFavourites', methods=['DELETE'])
def removeRecipeFromFavourites():
    #for a given user, we want to be able to remove a recipe from their favourites list
    data = request.json 
    email = data.get('email')
    recipeId = data.get('id')

    recipe = Recipe.query.filter_by(id=recipeId).first() #making sure the id is related to a recipe in our table 

    if not recipe: 
        return jsonify({'message': "The recipe you are trying to delete does not exist"}), 400

    if not email or not recipeId: 
        return jsonify({'message': "Must include a recipe to delete form the user's favourites list"}), 400
    
    user = User.query.filter_by(email=email).first()
    
    if recipeId not in user.favourites: 
        return jsonify({'message': "Recipe is not in the user's favourites"}), 400

    #IMP assuming that the user.favourites is a set, can only add a certain recipe to your favourites list once***
    user.favourites.remove(recipeId)
    new_array = array.array('i', user.favourites) #this array method is important and needed if .commit() is to refract the changes 
    user.favourites = new_array
    db.session.commit()
    return jsonify({'message': "Recipe removed from the user's favourites list succesfully"}), 200
    
@recipe.route('/addFavourite', methods=['POST'])
def add_favourite():
    try:
        data = request.json
        recipe_id = data.get('id')
        # check if signed in !!!!!!!!!!!!!!!!!!!
        #user_email = session.get('email') #is this right?
        user_email = data.get('email')
        user = User.query.filter_by(email=user_email).first()
        if not user_email:
            return jsonify({'message': 'User does not exist'}), 404
        
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return jsonify({'message': 'Recipe not found'}), 404
        
        #user.favourites.append(recipe_id) #check this
        favourite_list = [recipe_id]
        print(favourite_list)
        favourite_array = array.array('i', favourite_list)
        print(favourite_array)
        old_array = array.array('i', user.favourites)
        for i in user.favourites:
            if i == recipe_id:
                return jsonify({'message': 'Recipe already favourited'}), 200
            
        user.favourites = old_array + favourite_array
        db.session.commit()
        return jsonify({'message': 'Recipe added to favourites successfully'}), 200
    except Exception as e: 
        return jsonify({'message': "Internal server error"}), 500
        

@recipe.route('/favourites', methods=['GET'])
def get_favourites():
    try:
        user_email = request.args.get('email')
        user = User.query.filter_by(email=user_email).first()
        
        if not user_email:
            return jsonify({'message': 'User does not exist'}), 404
        
        favourite_recipes = []
        for r in user.favourites:
            recipe = Recipe.query.filter_by(id=r).first()
            if not recipe:
                continue
            # Encode the image data as Base64
            if recipe.image:
                image_base64 = base64.b64encode(recipe.image).decode('utf-8')
            else:
                image_base64 = None

            favourite_recipes.append({
                    'id': recipe.id,
                    'name': recipe.name,
                    'ingredients': recipe.ingredients,
                    'description': recipe.description,
                    'email': recipe.email,
                    'image': image_base64
                })
        return jsonify({'favourites': favourite_recipes}), 200
    except Exception as e: 
        return jsonify({'message': "Internal server error"}), 500
