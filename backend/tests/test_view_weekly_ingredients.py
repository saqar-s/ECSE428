import unittest
import sys
import base64
sys.path.append('../')
from app import app, db 

class TestViewWeeklyIngredients(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()


    # Unit test 1: View weekly recipes without any email
    def test_view_weekly_ingredients_valid_email_with_ingredients(self):
        # Test with an existing email that has ingredients
        response = self.app.get('/viewWeeklyIngredients?user_email=sasa@gmail.ca')
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.text.__contains__("Monday"))
        self.assertTrue(response.text.__contains__("Tuesday"))
        self.assertTrue(response.text.__contains__("Wednesday"))
        self.assertTrue(response.text.__contains__("Thursday"))
        self.assertTrue(response.text.__contains__("Friday"))
        self.assertTrue(response.text.__contains__("Saturday"))
        self.assertTrue(response.text.__contains__("Sunday"))
        self.assertTrue(response.text.__contains__('flour'))

    def test_view_weekly_ingredients_valid_email_without_ingredients(self):
        # Test with an existing email that doesn't have ingredients
        response = self.app.get('/viewWeeklyIngredients?user_email=r@gmail.com')
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'No recipes found for the user')


    def test_view_weekly_ingredients_missing_email_parameter(self):
        # Test with missing email parameter
        response = self.app.get('/viewWeeklyIngredients')
        
        self.assertEqual(response.json['error'], 'Email parameter is required')
        self.assertEqual(response.status_code, 400)

    def test_view_weekly_ingredients_invalid_email_format(self):
        # Test with invalid email format
        response = self.app.get('/viewWeeklyIngredients?user_email=invalidemail')
        self.assertEqual(response.json['error'], 'Email parameter is required')

        self.assertEqual(response.status_code, 400)


if __name__  == '__main__':
    unittest.main()