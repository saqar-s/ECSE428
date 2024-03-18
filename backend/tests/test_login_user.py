import unittest
import sys
sys.path.append('../')
from app import app, db 

class TestLoginUser(unittest.TestCase):
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

    # Unit test 1: Success User Login (Normal Flow)
    def test_login_user(self):

        # create a dummy user when running each unit test
        dummy_data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        self.app.post('/register', json=dummy_data)

        data = {
            'email': 'rambod@example.com',
            'password': 'password123'
        }
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Login successful')


    # Unit test 2: User Attempts to Login with Invalid Password
    def test_login_user_invalid_password(self):
        
        # create a dummy user when running each unit test
        dummy_data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        self.app.post('/register', json=dummy_data)

        data = {
            'email': 'rambod@example.com',
            'password': 'invalid' # invalid password
        }
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], 'Invalid password')


    # Unit test 3: User Attempts to Login with Invalid Email
    def test_login_user_invalid_email(self):
        
        # create a dummy user when running each unit test
        dummy_data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        self.app.post('/register', json=dummy_data)

        data = {
            'email': 'invalid@example.com', # invalid email
            'password': 'password123'
        }
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'User does not exist')


    # Unit test 4: User Attempts to Login with missing password
    def test_login_user_empty_password(self):
        
        # create a dummy user when running each unit test
        dummy_data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        self.app.post('/register', json=dummy_data)

        data = {
            'email': 'rambod@example.com',
            'password': '' # missing password
        }
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], 'Invalid password')


    # Unit test 5: User Attempts to Login with missing Email
    def test_login_user_empty_email(self):
        
        # create a dummy user when running each unit test
        dummy_data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        self.app.post('/register', json=dummy_data)

        data = {
            'email': '', # empty email
            'password': 'password123'
        }
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'User does not exist')

        
if __name__ == '__main__':
    unittest.main()