from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'
db = SQLAlchemy(app)
CORS(app)

class Event (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    def __repr__(self) :
        return f"Event: {self.description}"
    def __init__ (self, description):
        self. description = description

def format_event (event):
    return {
        "description": event.description,
        "id": event. id,
        "created_at": event.created_at
        }

@app.route('/event', methods = ['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    #this part is to grab the information and format it into an object to be able to use it in the frontend later on 
    return format_event(event)

@app.route('/event', methods=['GET'])
def get_event():
    events= Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {'events': event_list}

if __name__ == '__main__':
    app.run(port=8000)