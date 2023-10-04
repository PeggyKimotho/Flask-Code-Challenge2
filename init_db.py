from app import app, db  # Import the Flask app object
from models import db  # Import the SQLAlchemy db object

def initialize_database():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    initialize_database()
