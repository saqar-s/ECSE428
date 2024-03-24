import unittest
import sys
sys.path.append('../')
from app import app, db


class TestDeleteRecipe(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()

        # Create all database tables
        with app.app_context():
            db.create_all()

    # Remove all database tables
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Unit test 1: Successful Recipe Deletion (Normal Flow)
    def test_delete_new_recipe(self):
        data = {
            'name': 'test recipe',
            'ingredients': 'sugar, flour, eggs',
            'description': 'cake',
            'email': 'yo@gmail.com'
        }
        response1 = self.app.post('/createRecipe', json=data)
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response1.json['message'], 'Recipe created successfully')

        data = {
            'id': response1.json['id']
        }
        response2 = self.app.delete('/deleteRecipe', json=data)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.json['message'], "Recipe deleted successfully")

    # Unit test 2: Recipe Delete with no data
    def test_delete_nonexist_recipe(self):
        # Delete recipe
        data = {
            
        }
        response = self.app.delete('/deleteRecipe', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'ID field required')

    # Unit test 3: Recipe Deletion with wrong data 
    def test_delete_recipe_wrong_data(self):
        # Create recipe
        data = {
            "id":2103120402184120
        }

        response = self.app.delete('/deleteRecipe', json=data)
        self.assertEqual(response.status_code, 404)  # Assuming 404 is the appropriate status code for "Not Found"
    
        # Check if response body is empty or not in JSON format
        if response.content_type == 'application/json':
            self.assertEqual(response.json.get('message'), 'No recipe exists with that ID')
        else:
            self.fail("Response body is not in JSON format or empty")   

       
if __name__ == '__main__':
    unittest.main()
