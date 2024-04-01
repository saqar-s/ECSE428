import unittest
import sys
sys.path.append('../')
from app import app, db 
#from sqlalchemy import create_engine
from sqlalchemy import MetaData
from models import User, Recipe
import recipe


class TestAddToFavourites(unittest.TestCase):
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
            
    def tearDown(self):
        # Remove all database tables
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Unit test 1: Success Add to Favourites (Normal Flow)
    def test_add_to_favourites(self):
        # I havent tested this out yet --> I though it would be simpler to have the same recipe and user for every test
        
        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        r = recipes_list[0]
        id = r['id'] 
        """
        for r in recipes_list:
            if r['name'] == 'Test Recipe 500':
                id = r['id']
        """
        # Add recipe to favourites
        data = {
            'email': 'issy@mail.ca',
            'id': id
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Recipe added to favourites successfully')

 
    # Unit test 2: Recipe doesn't exist (Failure)
    def test_add_to_favourites_no_recipe(self):
        # Add non-existant recipe to favourites
        data = {
            'email': 'issy@mail.com',
            'id': 7000
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Recipe not found')  

    # Unit test 3: Not sending user (Failure)
    def test_add_to_favourites_no_user(self):
        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        r = recipes_list[0]
        id = r['id']
        
        data = {
            'email': '',
            'id': id
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'User does not exist') 
    """
    # Unit test 4: Trying to favourite a recipe that is already favourited (Alternate)
    def test_add_recipe_again(self):
        # getting a recipe to favourite
        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        r = recipes_list[0]
        id = r['id']
        
        data = {
            'email': 'issy@mail.com',
            'id': id
        }
        response1 = self.app.post('/addFavourite', json=data)
        response2 = self.app.post('/addFavourite', json=data)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.json['message'], 'Recipe added to favourites successfully')
        """


if __name__ == '__main__':
    unittest.main()