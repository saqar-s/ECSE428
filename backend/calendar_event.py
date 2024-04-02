from flask import request, jsonify, Blueprint
from flask_cors import CORS
from models import db, Recipe, CalendarEvent
from sqlalchemy import extract, and_
from models import db
from sqlalchemy import text
import base64

from datetime import datetime, timedelta

calendar_event = Blueprint('calendar', __name__)

CORS(calendar_event)

@calendar_event.route('/addToCalendar', methods=['POST'])
def addToCalendar():
    data = request.json
    recipeName = data.get('name')
    date_str = data.get('date')
    email = data.get('email')

    try:
        # Check for empty fields
        if not all([recipeName, date_str, email]):
            return jsonify({'message': 'All fields are required'}), 400

        # Check date validity
        date = datetime.strptime(date_str, '%Y-%m-%d')

        if '@' not in email or '.' not in email:
            return jsonify({'message': 'Invalid email address'}), 400

        # Check if recipe exists
        recipe = Recipe.query.filter_by(name=recipeName).first()
        if recipe is None:
            return jsonify({'error': 'Recipe not found'}), 404

        existing_event = CalendarEvent.query.filter_by(recipeName=recipeName, date=date).first()
        if existing_event:
            return jsonify({'error': 'Recipe already added to the calendar for this date'}), 400
        # Add to calendar
        new_event = CalendarEvent(date=date, recipe=recipe, email=email)
        db.session.add(new_event)
        db.session.commit()

        return jsonify({'message': 'Added to calendar successfully'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@calendar_event.route('/removeFromCalendar', methods=['POST'])
def removeFromCalendar():
    data = request.json
    recipeName = data.get('name')
    date_str = data.get('date')
    email = data.get('email')

    try:
        # Check for empty fields
        if not all([recipeName, date_str, email]):
            return jsonify({'message': 'All fields are required'}), 400

        # Check date validity
        date = datetime.strptime(date_str, '%Y-%m-%d')

        if '@' not in email or '.' not in email:
            return jsonify({'message': 'Invalid email address'}), 400

        # Check if recipe exists
        recipe = Recipe.query.filter_by(name=recipeName).first()
        if recipe is None:
            return jsonify({'error': 'Recipe not found'}), 404

        existing_event = CalendarEvent.query.filter_by(recipeName=recipeName, date=date).first()
        if not existing_event:
            return jsonify({'error': 'There is no recipe of this name and date in your Calendar'}), 400
        #Remove recipe from Calendar event
        db.session.delete(existing_event)
        db.session.commit()
        return jsonify({'message': 'Removed recipe from Calendar successfully'}), 202
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


#method should return all recipes for a given month for a given user? 
@calendar_event.route('/getFromCalendar', methods=['GET'])
def getFromCalender():
    try:
        #when getting the recipes for a given month, assuming you need: 
        #the year, ex: 2020
        #the month, in number format, ex: 04 (this means that singular number must have the 0 in front of them)
        months  = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        data = request.json
        month = data.get('month')
        year = data.get('year')

        custom_query = text('''SELECT *
            FROM calendar_event
        WHERE EXTRACT(YEAR FROM date) = :year
        AND EXTRACT(MONTH FROM date) = :month;''')

        #should possibly implement a minimum year
        if not month in months or not year: 
            return jsonify({'message': 'Please enter a valid year and month'}), 400
        else:
            #recipes is a list of all recipes for a given month

            events = db.session.execute(custom_query, {'year': year, 'month' : month})
            events_data = events.fetchall()
            results = [tuple(row) for row in events_data]

            #if there are no recipes, still want to be able to display the calendar
            event_list = [] #list of all recipe names and their dates
            for event in results: 
                event_list.append({
                    'id': event[0],
                    'date': event[1],
                    'name': event[2],
                    'email': event[3]
                })
            return jsonify({'events': event_list}), 200

    except Exception as e: 
        return jsonify({'error': str(e)}), 500

@calendar_event.route('/viewWeeklyRecipes', methods=['GET'])
def getWeeklyRecipes():
    try:
        user_email = request.args.get('user_email')
        
        if not user_email or "@" not in user_email:
            return jsonify({'error': 'Email parameter is required'}), 400

        user_recipes = CalendarEvent.query.filter_by(email=user_email).all()

        if not user_recipes:
            return jsonify({'message': 'No recipes found for the user'}), 404

        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Create a dictionary to store recipes for each day of the week
        weekly_recipes = {day: [] for day in weekday_names}

        # Populate the dictionary with recipes for each day
        for event in user_recipes:
            day_of_week = weekday_names[event.date.weekday()]
            weekly_recipes[day_of_week].append({
                'recipe_name': event.recipe.name,
                'date': event.date.strftime('%Y-%m-%d')
            })

        return jsonify({'weekly_recipes': weekly_recipes}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
