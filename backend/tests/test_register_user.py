import unittest
import sys
sys.path.append('../')
from app import app, db 


class TestRegisterUser(unittest.TestCase):
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

    def test_register_new_user(self):
        data = {
            'name': 'rambod',
            'email': 'rambod@example.com',
            'password': 'password123',
            'age': 23
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()