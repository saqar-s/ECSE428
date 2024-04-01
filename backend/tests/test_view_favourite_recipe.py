import unittest
import sys
import base64
sys.path.append('../')
from app import app, db 

class TestViewFavouriteRecipe(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()

    # Unit test 1: View favourite recipes associated with a specific user
    def test_view_user_favorite_recipes(self):

        user_email = 'user1@gmail.com'  # Test with a specific user's email
        response = self.app.get(f'/favourites?user_email={user_email}')
        self.assertEqual(response.status_code, 200)

    # Unit test 2: Fail to view favourite recipes because of no user with that email
    def test_wrong_email_favourite_recipe(self):

        user_email = 'noUser@gmail.com'  # Test with a specific user's email
        response = self.app.get(f'/favourites?user_email={user_email}')
        self.assertEqual(response.status_code, 404)

    # Unit test 3: View favourite recipes of a user with no favourite recipe
    def test_view_user_with_no_recipes(self):

        user_email = 'some@gmail.com'  # Test with a specific user's email
        response = self.app.get(f'/favourites?user_email={user_email}')
        self.assertEqual(response.status_code, 200)
    

if __name__ == '__main__':
    unittest.main()