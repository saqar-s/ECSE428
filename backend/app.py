from flask import Flask
from flask_cors import CORS
from account import account
from recipe import recipe
from calendar_event import calendar_event
from models import db, migrate

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'some string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe_database_gp57_user:zKPQLZ5Al0DI2lE3y5z8yPfcdZTr9Scn@dpg-cn42fb7109ks73eskttg-a.oregon-postgres.render.com/recipe_database_gp57'
CORS(app, supports_credentials=True, methods=["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"])

db.init_app(app)
migrate.init_app(app, db)

# Create all database tables
with app.app_context():
    db.create_all()

app.register_blueprint(account)
app.register_blueprint(recipe)
app.register_blueprint(calendar_event)


if __name__ == '__main__':
    app.run(debug=True , port=8000, use_reloader=False)