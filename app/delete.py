from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Driver, Vehicle, Trip, Base

# Create the SQLAlchemy Engine and establish a connection to the database
engine = create_engine('sqlite:///taxi_database.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Delete all data from the tables
session.query(Driver).delete()
session.query(Vehicle).delete()
session.query(Trip).delete()

# Commit the changes
session.commit()

print("All data deleted successfully.")
