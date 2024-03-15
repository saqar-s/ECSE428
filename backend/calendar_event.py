from flask import request, jsonify, Blueprint
from flask_cors import CORS
from models import db, Recipe, CalendarEvent

from datetime import datetime

calendar_event = Blueprint('calendar', __name__)

CORS(calendar_event)

@calendar_event.route('/addToCalendar', methods=['POST'])
def addToCalendar():
    data = request.json
    recipeName = data.get('name')
    date_str = data.get('date')

    try:
        # Check for empty fields
        if not all([recipeName, date_str]):
            return jsonify({'message': 'All fields are required'}), 400

        # Check date validity
        date = datetime.strptime(date_str, '%Y-%m-%d')

        # Check if recipe exists
        recipe = Recipe.query.filter_by(name=recipeName).first()
        if recipe is None:
            return jsonify({'error': 'Recipe not found'}), 404

        existing_event = CalendarEvent.query.filter_by(recipeName=recipeName, date=date).first()
        if existing_event:
            return jsonify({'error': 'Recipe already added to the calendar for this date'}), 400
        # Add to calendar
        new_event = CalendarEvent(date=date, recipe=recipe)
        db.session.add(new_event)
        db.session.commit()

        return jsonify({'message': 'Added to calendar successfully'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500