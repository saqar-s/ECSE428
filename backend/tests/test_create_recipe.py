import unittest
import sys
import base64
sys.path.append('../')
from app import app, db 


class TestCreateRecipe(unittest.TestCase):
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

    # Unit test 1: Success recipe creation (Normal Flow)
    def test_create_recipe(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')

        data = {
            'name': 'recipe 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'rambod@email.com',
            'image': image_data,
        }
        response = self.app.post('/createRecipe', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Recipe created successfully')


    # Unit test 2: Recipe creation with missing name
    def test_create_recipe_missing_name(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')
        data = {
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'rambod@email.com',
            'image': image_data
        }
        response = self.app.post('/createRecipe', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')


    # Unit test 3: Recipe creation with missing ingredients
    def test_create_recipe_missing_ingredient(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')
        data = {
            'name': 'recipe 1',
            'description': 'test description',
            'email': 'rambod@email.com',
            'image': image_data

        }
        response = self.app.post('/createRecipe', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')


    # Unit test 4: Recipe creation with missing email
    def test_create_recipe_missing_email(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')
        data = {
            'name': 'recipe',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'image': image_data
        }
        response = self.app.post('/createRecipe', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')


    # Unit test 5: Recipe creation with missing description
    def test_create_recipe_missing_description(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')
        data = {
            'name': 'recipe',
            'ingredients': 'egg, sugar, milk',
            'email': 'rambod@email.com',
            'image': image_data
        }
        response = self.app.post('/createRecipe', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')


    # Unit test 6: Recipe creation with invalid email
    def test_create_recipe_invalid_email(self):
        with open ('../picture/image1.png', 'rb') as image:
            image_data = base64.b64encode(image.read()).decode('utf-8')

        data = {
            'name': 'recipe',
            'ingredients': 'egg, sugar, milk',
            'description': 'test',
            'email': 'rambodemail.com',
            'image': image_data
        }
        response = self.app.post('/createRecipe', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid email address')

if __name__ == '__main__':
    unittest.main()