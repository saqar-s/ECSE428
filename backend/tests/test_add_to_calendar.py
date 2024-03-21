import unittest
import sys
sys.path.append('../')
from app import app, db 

class TestAddToCalendar(unittest.TestCase):
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
    def test_add_to_calendar(self):
        data_recipe = {
            'name': 'recipe 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)

        data_calendar = {
            'name': 'recipe 1',
            'date': '2024-04-12'
        }
        response = self.app.post('/addToCalendar', json=data_calendar)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Recipe added to calendar successfully')

    # Unit test 2: Add to calendar with missing name
    def test_add_to_calendar_missing_name(self):
        data_recipe = {
            'name': 'recipe 2',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)
        data = {
            'date': '2024-04-12'
        }
        response = self.app.post('/addToCalendar', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')

    # Unit test 3: Add to calendar with missing date
    def test_add_to_calendar_missing_date(self):
        data_recipe = {
            'name': 'recipe 3',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)
        data_recipe = {
            'name': 'recipe 3'
        }
        response = self.app.post('/addToCalendar', json=data_recipe)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')

    # Unit test 4: Add to calendar with non existing recipe
    def test_add_to_calendar_non_existing_recipe(self):
        data_calendar = {
            'name': 'non-existent',
            'date': '2024-04-12'
        }
        response = self.app.post('/addToCalendar', json=data_calendar)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Recipe not found')

    # Unit test 5: Add to calendar with existing recipe for the same date
    def test_add_to_calendar_already_existing(self):
        data_recipe = {
            'name': 'recipe 4',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)
        data_first = {
            'name': 'recipe 4',
            'date': '2024-04-12'
        }
        self.app.post('/addToCalendar', json=data_first)
        response = self.app.post('/addToCalendar', json=data_first)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Recipe already added to the calendar for this date')

if __name__ == '__main__':
    unittest.main()
