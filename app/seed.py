from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Driver, Vehicle, Trip, Base
from faker import Faker
from faker_vehicle import VehicleProvider
import random
import datetime

# Create the SQLAlchemy Engine and establish a connection to the database
engine = create_engine('sqlite:///taxi_database.db', echo=True)  # Update with your database connection details
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Seed Data using Faker
fake = Faker()
fake.add_provider(VehicleProvider)
# Function to seed the vehicles table

vehicles = [
        Vehicle(
            model=fake.vehicle_make(),
            registration_number=fake.machine_model(),

        )
        for _ in range(10)
    ]

session.add_all(vehicles)
session.commit()


# Function to seed the drivers table
vehicles = session.query(Vehicle).all()

drivers = [
        Driver(
            name=fake.name(),
            contact=fake.phone_number(),
            vehicle_id=random.choice(vehicles).id,
        )
        for _ in range(12)
    ]

session.add_all(drivers)
session.commit()


# Function to seed the trips table

drivers = session.query(Driver).all()
vehicles = session.query(Vehicle).all()

trips = [
        Trip(
            driver_id=random.choice(drivers).id,
            vehicle_id=random.choice(vehicles).id,
            start_time=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
            end_time=datetime.datetime.utcnow()
        )
        for _ in range(10)
    ]

session.add_all(trips)
session.commit()
    

print(f"{10} vehicles seeded successfully.")

print(f"{12} drivers seeded successfully.")

print(f"{10} trips seeded successfully.")