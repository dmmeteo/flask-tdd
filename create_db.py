from app import db
from models import Flaskr


# Create the database and db table
db.create_all()

# commit the changes
db.session.commit()