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

    # Unit test 1: Successful User Deletion (Normal Flow)
    def test_delete_new_user(self):
        data = {
            'name': 'JCBEES',
            'email': 'JCBEES@gmail.com',
            'password': 'Qwerty123',
            'age': 23
        }
        response1 = self.app.post('/register', json=data)
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response1.json['message'], 'Registration successful')
        
        response2 = self.app.delete('/delete', json=data)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.json['message'], 'User deletion successful')

    # Unit test 2: User Delete with Non-Existent Email
    def test_delete_nonexist_user(self):
        # Delete user
        data = {
            'name': 'JCBEES1',
            'email': 'JCBEES@gmail.com',
            'password': 'Qwerty1234',
            'age': 24
        }
        response = self.app.delete('/delete', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Not an active account')

    # Unit test 3: User Deletion with wrong password
    def test_delete_user_wrong_password(self):
        # Create user
        data = {
            'name': 'JCBEES',
            'email': 'JCBEES@gmail.com',
            'password': 'Qwerty123',
            'age': 23
        }
        response1 = self.app.post('/register', json=data)
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response1.json['message'], 'Registration successful')
        
        # Delete user with wrong password
        badData = {
            'email': 'JCBEES@gmail.com',
            'password': 'BadBadNotGood'
        }
        response2 = self.app.delete('/delete', json=badData)
        self.assertEqual(response2.status_code, 401)
        self.assertEqual(response2.json['message'], 'Invalid password')

if __name__ == '__main__':
    unittest.main()