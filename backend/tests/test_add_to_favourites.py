import unittest
import sys
sys.path.append('../')
from app import app, db 
#from sqlalchemy import create_engine


class TestRegisterUser(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()
        
        # Create all database tables
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Remove all database tables
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Unit test 1: Success Add to Favourites (Normal Flow)
    def test_add_to_favourites(self):
        # Create dummy user
        dummy_user_data = {
            'name': 'Isabel',
            'email': 'isabel@mail.com',
            'password': 'password123',
            'age': 23
        }
        self.app.post('/register', json=dummy_user_data)
        self.app.post('/login', json=dummy_user_data)

        # Create dummy recipe
        dummy_recipe_data = {
            'name': 'Sushi',
            'ingredients': 'rice, tuna, avocado',
            'description': 'This is my sushi recipe',
            'email': 'isabel@mail.com',
            'image': None
        }
        response_recipe = self.app.post('/createRecipe', json=dummy_recipe_data)
        self.assertEqual(response_recipe.status_code, 201)

        # Add recipe to favourites
        data = {
            'recipe_id': response_recipe.json['id']
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Recipe added to favourites successfully')

if __name__ == '__main__':
    unittest.main()