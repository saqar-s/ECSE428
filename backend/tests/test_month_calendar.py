import unittest
import sys
import json
sys.path.append('../')
from app import app, db 

class TestViewMonthCalendar(unittest.TestCase):
    def setUp(self):
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = 'some string'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'

        self.app = app.test_client()


    # Unit test 1: View month calendar without any fields
    def test_view_month_calendar_without_fields(self):

        response = self.app.get('/getFromCalendar')
        self.assertIn('415', response.json['error'])

        self.assertEqual(response.status_code, 500) # Internal Error status code

    # Unit test 2: View month calendar with empty year field
    def test_view_month_calendar_without_year_field(self):

        test_data = {
            'month': '02', 
            'year': '' # empty year field
            }

        # Make the GET request with the encoded JSON data
        response = self.app.get('/getFromCalendar', data=json.dumps(test_data), content_type='application/json')

        self.assertEqual(response.status_code, 400) # Bad request status code
        self.assertEqual(response.json['message'], 'Please enter a valid year and month')

    # Unit test 3: View month calendar with empty month field
    def test_view_month_calendar_without_month_field(self):

        test_data = {
            'month': '', # empty month field
            'year': '2024' 
            }

        # Make the GET request with the encoded JSON data
        response = self.app.get('/getFromCalendar', data=json.dumps(test_data), content_type='application/json')

        self.assertEqual(response.status_code, 400) # Bad request status code
        self.assertEqual(response.json['message'], 'Please enter a valid year and month')
    
    # Unit test 4: View month calendar with invalid year field
    def test_view_month_calendar_invalid_year_field(self):

        test_data = {
            'month': '', 
            'year': '23479243' # invalid year field
            }

        # Make the GET request with the encoded JSON data
        response = self.app.get('/getFromCalendar', data=json.dumps(test_data), content_type='application/json')

        self.assertEqual(response.status_code, 400) # Bad request status code
        self.assertEqual(response.json['message'], 'Please enter a valid year and month')
    
    # Unit test 5: View month calendar with invalid month field
    def test_view_month_calendar_invalid_month_field(self):

        test_data = {
            'month': '145656', # invalid month field
            'year': '2024' 
            }

        # Make the GET request with the encoded JSON data
        response = self.app.get('/getFromCalendar', data=json.dumps(test_data), content_type='application/json')

        self.assertEqual(response.status_code, 400) # Bad request status code
        self.assertEqual(response.json['message'], 'Please enter a valid year and month')

    # Unit test 6: View month calendar with correct fields (success scenario)
    def test_view_month_calendar_success(self):

        test_data = {
            'month': '01', # invalid month field
            'year': '2024' 
            }

        # Make the GET request with the encoded JSON data
        response = self.app.get('/getFromCalendar', data=json.dumps(test_data), content_type='application/json')

        self.assertEqual(response.status_code, 200) # OK
        self.assertIn("events", response.text)

if __name__ == '__main__':
    unittest.main()
