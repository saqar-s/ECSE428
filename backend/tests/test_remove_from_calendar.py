import unittest
import sys
sys.path.append('../')
from app import app, db 

class TestRemoveFromCalendar(unittest.TestCase):
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

    # Unit test 1: Success Remove from Calendar (Normal Flow)
    def test_remove_from_calendar(self):

        data_recipe = {
            'name': 'recipe 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)

        data_calendar = {
            'name': 'recipe 1',
            'date': '2024-04-20',
            'email': 'random@gmail.com'
        }
        self.app.post('/addToCalendar', json=data_calendar)

        response = self.app.post('/removeFromCalendar', json=data_calendar)
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json['message'], 'Removed recipe from Calendar successfully')

    # Unit test 2: Remove from calendar with missing name
    def test_remove_from_calendar_missing_name(self):
        data_recipe = {
            'name': 'recipe 2',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)
        data = {
            'date': '2024-04-20',
            'email': 'random@gmail.com'
        }
        response = self.app.post('/removeFromCalendar', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')

    # Unit test 3: Remove from calendar with missing date
    def test_remove_from_calendar_missing_date(self):
        data_recipe = {
            'name': 'recipe 3',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)
        data_recipe = {
            'name': 'recipe 3',
            'email': 'random@gmail.com'
        }
        response = self.app.post('/removeFromCalendar', json=data_recipe)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'All fields are required')

    # Unit test 4: Remove from calendar with non existing recipe
    def test_remove_from_calendar_non_existing_recipe(self):
        data_calendar = {
            'name': 'non-existent',
            'date': '2024-04-20',
            'email': 'random@gmail.com'
        }
        response = self.app.post('/removeFromCalendar', json=data_calendar)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Recipe not found')

    # Unit test 5: Remove from calendar with non-existent calendar event
    def test_remove_from_calendar_already_removed(self):
        data_recipe = {
            'name': 'recipe 4',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        self.app.post('/createRecipe', json=data_recipe)
        data_first = {
            'name': 'recipe 4',
            'date': '2024-04-20',
            'email': 'random@gmail.com'
        }
        self.app.post('/removeFromCalendar', json=data_first)

        response = self.app.post('/removeFromCalendar', json=data_first)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'There is no recipe of this name and date in your Calendar')

if __name__ == '__main__':
    unittest.main()
