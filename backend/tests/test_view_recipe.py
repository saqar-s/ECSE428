import unittest
import sys
import base64
sys.path.append('../')
from app import app, db 

class TestViewRecipe(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()

        # Create all database tables
        with app.app_context():
            db.create_all()
            # Add some sample recipes for testing
            self._add_sample_recipes()

    def tearDown(self):
        # Remove all database tables
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Unit test 1: View all recipes for the dashboard
    def test_view_all_recipes(self):
        data1= {
            'name': 'recipe1',
            'ingredients': 'sugar, flour, eggs',
            'description': 'cake',
            'email': 'user1@gmail.com'
        }
        data2 = {
            'name': 'recipe2',
            'ingredients': 'sugar, milk',
            'description': 'hotm milk',
            'email': 'user2@gmail.com'
        }
        response1 = self.app.get('/getRecipes', json=data1)
        response2 = self.app.get('/getRecipes', json=data2)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(len(response1.json['recipes']), 2)  # Assuming there are two sample recipes added
        self.assertEqual(len(response2.json['recipes']), 2)  # Assuming there are two sample recipes added

    # Unit test 2: View recipes associated with a specific user
    def test_view_user_recipes(self):
        data3= {
            'name': 'recipe3',
            'ingredients': 'sugar, flour, eggs',
            'description': 'cake',
            'email': 'user3@gmail.com'
        }
        user_email = 'user3@gmail.com'  # Test with a specific user's email
        response = self.app.get(f'/getRecipes?user_email={user_email}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['recipes']), 1)  # Assuming only one recipe is associated with this user



if __name__ == '__main__':
    unittest.main()
