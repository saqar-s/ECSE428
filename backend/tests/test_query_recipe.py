import unittest
import sys
import base64
sys.path.append('../')
from app import app, db

# Test methods for both get all recipes & get a recipe

class TestQueryRecipe(unittest.TestCase):
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
            
    # Unit test 1: Search for all recipes in empty DB
    def test_search_all_recipes_empty_db(self):

        response = self.app.get('/getRecipes')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.json['message'], 'There are no recipes in the database')
    
    
    # Unit test 2: Search for a recipe in empty DB
    def test_search_a_recipe_empty_db(self):
        data = {
            'name': 'recipe'
        }
        response = self.app.get('/getARecipe', json=data)
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.json['message'], 'There are no recipes in the database')
    

    # Unit test 3: Successfully search for all recipes (Normal Flow)
    def test_search_all_recipes(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')

        data1 = {
            'name': 'recipe 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'rambod@email.com',
            'image': image_data,
        }
        
        data2 = {
            'name': 'recipe 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'rambod@email.com',
            'image': image_data,
        }
        
        data3 = {
            'name': 'recipe 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'rambod@email.com',
            'image': image_data,
        }
        response1 = self.app.post('/createRecipe', json=data1)
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response1.json['message'], 'Recipe created successfully')
        
        response2 = self.app.post('/createRecipe', json=data2)
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(response2.json['message'], 'Recipe created successfully')
        
        response3 = self.app.post('/createRecipe', json=data3)
        self.assertEqual(response3.status_code, 201)
        self.assertEqual(response3.json['message'], 'Recipe created successfully')
        
        response4 = self.app.get('/getRecipe')
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response4.json['recipes'][0]['name'], 'recipe 1')
        


    # Unit test 4: Successfully search for a specifc recipe
    def test_search_recipe(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')
        data = {
            'name': 'recipe 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'rambod@email.com',
            'image': image_data,
        }
        
        data1 = {
            'name': 'recipe 1'
        }
        response = self.app.post('/createRecipe', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Recipe created successfully')
        
        response2 =self.app.get('/getARecipe', json=data1)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.json['recipes'], 'Recipe created successfully')


    # Unit test 5: Empty search for a specific recipe
    def test_search_recipe_missing_name(self):
        
        data = {
            'name': ''
        }
        response = self.app.post('/getARecipe', json=data)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json['message'], 'Name field required')

if __name__ == '__main__':
    unittest.main()