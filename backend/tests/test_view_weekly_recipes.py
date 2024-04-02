import unittest
import sys
import base64
sys.path.append('../')
from app import app, db 

class TestViewWeeklyRecipes(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()


    # Unit test 1: View weekly recipes without any email
    def test_view_weekly_recipes_without_email(self):

        response = self.app.get('/viewWeeklyRecipes')
        self.assertEqual(response.json['error'], 'Email parameter is required')

        self.assertEqual(response.status_code, 400) # bad request status code


    # Unit test 2: View recipes weekly recipes with an invalid email address
    def test_view_weekly_recipes_invalid_email(self):

        user_email = 'invalidemailgmail.com'  # invalid email address without @
        response = self.app.get(f'/viewWeeklyRecipes?user_email={user_email}')
        self.assertEqual(response.json['error'], 'Email parameter is required')

        self.assertEqual(response.status_code, 400)

    # Unit test 3: View recipes weekly recipes with an email address without any recipes
    def test_view_weekly_recipes_no_recipes(self):

        user_email = 'sampleemail@gmmail.com'  # invalid email address without @
        response = self.app.get(f'/viewWeeklyRecipes?user_email={user_email}')
        self.assertEqual(response.json['message'], 'No recipes found for the user')

        self.assertEqual(response.status_code, 404) # not found status code

    # Unit test 4: View recipes weekly recipes (success scenario)
    def test_view_weekly_recipes_success(self):

        user_email = 'r@gmail.com'  # invalid email address without @
        response = self.app.get(f'/viewWeeklyRecipes?user_email={user_email}')

        self.assertEqual(response.status_code, 200) # OK status code

        self.assertTrue(response.text.__contains__("Monday"))
        self.assertTrue(response.text.__contains__("Tuesday"))
        self.assertTrue(response.text.__contains__("Wednesday"))
        self.assertTrue(response.text.__contains__("Thursday"))
        self.assertTrue(response.text.__contains__("Friday"))
        self.assertTrue(response.text.__contains__("Saturday"))
        self.assertTrue(response.text.__contains__("Sunday"))


if __name__ == '__main__':
    unittest.main()
