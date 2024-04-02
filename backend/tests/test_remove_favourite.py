import unittest
import sys
sys.path.append('../')
from app import app, db 
#from sqlalchemy import create_engine
from sqlalchemy import MetaData
from models import User, Recipe
import recipe

class TestRemoveFavouriteRecipe(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()
        
        # Create all database tables
        with app.app_context():
            db.drop_all()
            db.create_all()
            # Given a user exists
            test_user = User(name='Isabel', email='issy@mail.ca', password='pass1234', age=22)
            test_recipe = Recipe(name='Recipe Test', ingredients = 'flour, banana', description = 'test recipe', email='issy@mail.ca')
            db.session.add(test_user)
            db.session.add(test_recipe)
            db.session.commit()

    # Unit test 1: Remove a favourite recipe associated with a specific user
    def test_remove_favorite_recipe(self):
        
        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        r = recipes_list[0]
        id = r['id']
    
        data = {
            'email': 'issy@mail.ca',
            'id': id
        }
        self.app.post('/addFavourite', json=data)
        response = self.app.delete('/removeRecipeFromFavourites', json=data)
        self.assertEqual(response.status_code, 200)

    # Unit test 2: Fail to remove favourite recipe (recipe does not exist)
    def test_no_recipe(self):

        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        r = recipes_list[0]
        id = r['id']
    
        data = {
            'email': 'issy@mail.ca',
            'id': 787
        }
        self.app.post('/addFavourite', json=data)
        response = self.app.delete('/removeRecipeFromFavourites', json=data)
        
        self.assertEqual(response.status_code, 400)

    # Unit test 3: Fail to remove favourite recipe (no recipe Id or email)
    def test_no_email(self):

        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        r = recipes_list[0]
        id = r['id']
    
        data = {
            'email': '',
            'id': id
        }
        self.app.post('/addFavourite', json=data)
        response = self.app.delete('/removeRecipeFromFavourites', json=data)
        
        self.assertEqual(response.status_code, 400)
        
    # Unit test 4: Fail to remove favourite recipe (recipe is not in favourites)
    def test_not_favorite(self):

        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        r = recipes_list[0]
        id = r['id']
    
        data = {
            'email': 'issy@mail.ca',
            'id': id
        }
        
        response = self.app.delete('/removeRecipeFromFavourites', json=data)
        self.assertEqual(response.status_code, 400)
    

if __name__ == '__main__':
    unittest.main()