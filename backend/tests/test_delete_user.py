import unittest
import sys
sys.path.append('../')
from app import app, db 

class TestDeleteUser(unittest.TestCase):
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
        
   # Unit test 1: Successful delete recipe (Normal Flow)
    def test_delete_recipe(self):
        data = {
            "name": "Honey Garlic Chicken",
            
        }
        response = self.app.delete('/deleteRecipe', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'User deleted successfully'})

    # Unit test 2: Unsuccessful delete recipe (Error Flow)
        data = {
            "email": ""
        }
        response = self.app.delete('/deleteRecipe', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'The recipe with the given name cannot be found'})

    # Unit test 3: Unsuccessful delete recipe (Error Flow)
        
