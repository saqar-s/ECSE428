import unittest
import sys
sys.path.append('../')
from app import app, db 

class TestUserlist(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        
        # Create all database tables
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Remove all database tables
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Unit test 2: Search User list when database is empty
    def test_userlist_empty_database(self):
        dummy_data1 = {
            'name': 'Bob',
            'email': 'Bob@example.com',
            'password': 'password123',
            'age': 23
        }
        dummy_data2 = {
            'name': 'Sarah',
            'email': 'Sarah@example.com',
            'password': 'password123',
            'age': 20
        }
        self.app.post('/register', json=dummy_data1)
        self.app.post('/register', json=dummy_data2)
        #This is here as to future proof once we have tokens 
        data = {
            'email': 'rambod@example.com',
            'password': 'password123'
        }
        self.app.post('/login', json=data)
        response = self.app.get('/searchuser')
        self.assertEqual(response.status_code,203)
        self.assertEqual(response.json[0], dummy_data1["name"])
        self.assertEqual(response.json[1], dummy_data2["name"])

        # Unit test 1: Search User list Success (Normal Flow)
    def test_userlist(self):
        #This is here as to future proof once we have tokens 
        response = self.app.get('/searchuser')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.json['message'], 'There are no users in the database')


if __name__ == '__main__':
    unittest.main()
