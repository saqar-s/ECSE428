import unittest
import sys
sys.path.append('../')
from app import app, db 
#from sqlalchemy import create_engine


class TestRegisterUser(unittest.TestCase):
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
            #db.drop_all()

    # Unit test 1: Success Add to Favourites (Normal Flow)
    def test_add_to_favourites(self):
        # Create dummy user
        dummy_user_data = {
            'name': 'Isabel',
            'email': 'isabel1@mail.com',
            'password': 'password123',
            'age': 23
        }
        self.app.post('/register', json=dummy_user_data)
        self.app.post('/login', json=dummy_user_data)

        # Create dummy recipe
        dummy_recipe_data = {
            'name': 'Sushi',
            'ingredients': 'rice, tuna, avocado',
            'description': 'This is my sushi recipe',
            'email': 'isabel@mail.com',
            'image': None,
        }
        response_recipe = self.app.post('/createRecipe', json=dummy_recipe_data)
        #self.assertEqual(response_recipe.status_code, 201)

        # Add recipe to favourites
        data = {
            'email': 'isabel@mail.com',
            'id': response_recipe.json['id']
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Recipe added to favourites successfully')

if __name__ == '__main__':
    unittest.main()
import unittest
import sys
sys.path.append('../')
from app import app, db 
#from sqlalchemy import create_engine
from sqlalchemy import MetaData
from models import User, Recipe
import recipe


class TestAddToFavourites(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()
        
        # Create all database tables
        with app.app_context():
            db.create_all()
            # Given a user exists
            test_user = User(name='Isabel', email='isabel@mail.ca', password='pass1234', age=22)
            test_recipe = Recipe(name='Test Recipe 500', ingredients = 'sugar, flour, banana', description = 'test recipe', email='isabel@mail.ca')
            db.session.add(test_user)
            db.session.add(test_recipe)
            db.session.commit()
            

    def tearDown(self):
        # Remove all database tables
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Unit test 1: Success Add to Favourites (Normal Flow)
    def test_add_to_favourites(self):
        """
        # Create dummy user
        dummy_user_data = {
            'name': 'Isabel',
            'email': 'isabel1@mail.com',
            'password': 'password123',
            'age': 23
        }
        response_user = self.app.post('/register', json=dummy_user_data)
        self.assertEqual(response_user.status_code, 201)

        # Create dummy recipe
        data_recipe = {
            'name': 'recipe test 1',
            'ingredients': 'egg, sugar, milk',
            'description': 'test description',
            'email': 'random@gmail.com'
        }
        response_recipe = self.app.post('/createRecipe', json=data_recipe)
        self.assertEqual(response_recipe.status_code, 201)
        """
        # I havent tested this out yet --> I though it would be simpler to have the same recipe and user for every test
        
        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        id = 0
        for r in recipes_list:
            if r['name'] == 'Test Recipe 500':
                id = r['id']
        
        # Add recipe to favourites
        data = {
            'email': 'isabel@mail.ca',
            'id': id
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Recipe added to favourites successfully')

    # Unit test 2: Success Add to Favourites if already in favourites (Alternate Flow)
    def test_add_to_favourites_again(self):
        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        id = 0
        for r in recipes_list:
            if r['name'] == 'Test Recipe 500':
                id = r['id']
        # Add recipe to favourites
        data = {
            'email': 'isabel@mail.com',
            'id': id
        }
        response = self.app.post('/addFavourite', json=data)

        # Add recipe again
        data = {
            'email': 'isabel@mail.com',
            'id': id
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Recipe already favourited')


    # Unit test 3: User doesn't exit
    def test_add_to_favourites_no_user(self):
        response_recipe = self.app.get('/getRecipes')
        recipes_list = response_recipe.json['recipes']
        id = 0
        for r in recipes_list:
            if r['name'] == 'Test Recipe 500':
                id = r['id']
        # Add recipe to favourites
        data = {
            'email': 'isabel1000@mail.com',
            'id': id 
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'User does not exist')

    # Unit test 4: Recipe doesn't exist
    def test_add_to_favourites_no_recipe(self):

        # Add non-existant recipe to favourites
        data = {
            'email': 'isabel@mail.com',
            'id': 7000
        }
        response = self.app.post('/addFavourite', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Recipe not found')        

if __name__ == '__main__':
    unittest.main()