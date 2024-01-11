from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from models import Driver, Vehicle, Trip, Base

Base = declarative_base()
engine = create_engine("sqlite:///taxi_database.db") 
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session() 

# Function to add a new driver
def add_driver(name, contact):
    new_driver = Driver(name=name, contact=contact)
    session.add(new_driver)
    session.commit()
    print(f"Driver '{name}' with contact '{contact}' added successfully.")

# Function to list all drivers
def list_drivers():
    drivers = session.query(Driver).all()
    if drivers:
        print("List of Drivers:")
        for driver in drivers:
            print(f"Driver ID: {driver.id}, Name: {driver.name}, Contact: {driver.contact}")
    else:
        print("No drivers found.")

# Function to update driver information
def update_driver(driver_id, attribute, new_value):
    driver = session.query(Driver).filter(Driver.id == driver_id).first()
    if driver:
        setattr(driver, attribute, new_value)
        session.commit()
        print(f"Driver ID {driver_id} updated successfully.")
    else:
        print("Driver not found.")

# Function to remove a driver
def remove_driver(driver_id):
    driver = session.query(Driver).filter(Driver.id == driver_id).first()
    if driver:
        session.delete(driver)
        session.commit()
        print(f"Driver ID {driver_id} removed successfully.")
    else:
        print("Driver not found.")

# Function to add a new vehicle
def add_vehicle(model, registration_number):
    new_vehicle = Vehicle(model=model, registration_number=registration_number)
    session.add(new_vehicle)
    session.commit()
    print(f"Vehicle '{model}' with registration number '{registration_number}' added successfully.")

# Function to list all vehicles
def list_vehicles():
    vehicles = session.query(Vehicle).all()
    if vehicles:
        print("List of Vehicles:")
        for vehicle in vehicles:
            print(f"Vehicle ID: {vehicle.id}, Model: {vehicle.model}, Registration Number: {vehicle.registration_number}")
    else:
        print("No vehicles found.")

# Function to update vehicle information
def update_vehicle(vehicle_id, attribute, new_value):
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if vehicle:
        setattr(vehicle, attribute, new_value)
        session.commit()
        print(f"Vehicle ID {vehicle_id} updated successfully.")
    else:
        print("Vehicle not found.")

# Function to remove a vehicle
def remove_vehicle(vehicle_id):
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if vehicle:
        session.delete(vehicle)
        session.commit()
        print(f"Vehicle ID {vehicle_id} removed successfully.")
    else:
        print("Vehicle not found.")

# Function to start a new trip
def start_trip(driver_id, vehicle_id):
    driver = session.query(Driver).filter(Driver.id == driver_id).first()
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if driver and vehicle:
        new_trip = Trip(driver_id=driver_id, vehicle_id=vehicle_id)
        session.add(new_trip)
        session.commit()
        print(f"Trip started for Driver ID {driver_id} with Vehicle ID {vehicle_id}.")
    else:
        print("Driver or Vehicle not found.")

# Function to complete a trip
def complete_trip(trip_id):
    trip = session.query(Trip).filter(Trip.id == trip_id).first()
    if trip:
        trip.end_time = datetime.datetime.utcnow()
        session.commit()
        print(f"Trip ID {trip_id} completed successfully.")
    else:
        print("Trip not found.")

# Function to list all trips
def list_trips():
    trips = session.query(Trip).all()
    if trips:
        print("List of Trips:")
        for trip in trips:
            print(f"Trip ID: {trip.id}, Driver ID: {trip.driver_id}, Vehicle ID: {trip.vehicle_id}, Start Time: {trip.start_time}, End Time: {trip.end_time}")
    else:
        print("No trips found.")

# Function to calculate fare for a completed trip (Example: Fare calculation logic needs to be implemented)
def calculate_fare(trip_id):
    # Example fare calculation logic (dummy)
    trip = session.query(Trip).filter(Trip.id == trip_id).first()
    if trip and trip.end_time:
        duration = (trip.end_time - trip.start_time).total_seconds() / 60  # Calculate trip duration in minutes
        fare = duration * 0.1  # Dummy fare calculation (replace with your logic)
        print(f"Fare for Trip ID {trip_id}: ${fare}")
    else:
        print("Trip not found or trip is ongoing.")
