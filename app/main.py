from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from models import *
import click

Base = declarative_base()
engine = create_engine("sqlite:///taxi_database.db") 
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session() 

@click.group()
def main():
    """Taxi CLI Application."""
    pass


@main.command()
def add_driver():
    """Add a new driver."""
    name = click.prompt('Enter driver name', type=str)
    contact = click.prompt('Enter driver contact', type=str)

    new_driver = Driver(name=name, contact=contact)
    session.add(new_driver)
    session.commit()
    click.echo(f"Driver '{name}' with contact '{contact}' added successfully.")


@main.command()
def list_drivers():
    """List all drivers."""
    drivers = session.query(Driver).all()
    if drivers:
        click.echo("List of Drivers:")
        for driver in drivers:
            click.echo(f"Driver ID: {driver.id}, Name: {driver.name}, Contact: {driver.contact}")
    else:
        click.echo("No drivers found.")


@main.command()
def add_vehicle():
    """Add a new vehicle."""
    model = click.prompt('Enter vehicle model', type=str)
    registration_number = click.prompt('Enter registration number', type=str)

    new_vehicle = Vehicle(model=model, registration_number=registration_number)
    session.add(new_vehicle)
    session.commit()
    click.echo(f"Vehicle '{model}' with registration number '{registration_number}' added successfully.")


@main.command()
def list_vehicles():
    """List all vehicles."""
    vehicles = session.query(Vehicle).all()
    if vehicles:
        click.echo("List of Vehicles:")
        for vehicle in vehicles:
            click.echo(f"Vehicle ID: {vehicle.id}, Model: {vehicle.model}, Registration Number: {vehicle.registration_number}")
    else:
        click.echo("No vehicles found.")


@main.command()
def start_trip():
    """Start a new trip."""
    driver_id = click.prompt('Enter driver ID', type=int)
    vehicle_id = click.prompt('Enter vehicle ID', type=int)

    driver = session.query(Driver).filter(Driver.id == driver_id).first()
    vehicle = session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if driver and vehicle:
        new_trip = Trip(driver_id=driver_id, vehicle_id=vehicle_id)
        session.add(new_trip)
        session.commit()
        click.echo(f"Trip started for Driver ID {driver_id} with Vehicle ID {vehicle_id}.")
    else:
        click.echo("Driver or Vehicle not found.")


@main.command()
def complete_trip():
    """Complete an ongoing trip."""
    trip_id = click.prompt('Enter trip ID', type=int)
    trip = session.query(Trip).filter(Trip.id == trip_id).first()

    if trip and not trip.end_time:
        trip.end_time = datetime.datetime.utcnow()
        session.commit()
        click.echo(f"Trip ID {trip_id} completed successfully.")
    elif not trip:
        click.echo("Trip not found.")
    else:
        click.echo("Trip has already been completed.")


@main.command()
def calculate_fare():
    """Calculate fare for a completed trip."""
    trip_id = click.prompt('Enter trip ID', type=int)
    trip = session.query(Trip).filter(Trip.id == trip_id).first()

    if trip and trip.end_time:
        duration = (trip.end_time - trip.start_time).total_seconds() / 60  # Calculate trip duration in minutes
        fare = duration * 0.2  # Placeholder for fare calculation (replace with your logic)
        click.echo(f"Fare for Trip ID {trip_id}: ${fare}")
    elif not trip:
        click.echo("Trip not found.")
    else:
        click.echo("Trip is still ongoing.")


@main.command()
def list_trips():
    """List all trips."""
    trips = session.query(Trip).all()
    if trips:
        click.echo("List of Trips:")
        for trip in trips:
            click.echo(f"Trip ID: {trip.id}, Driver ID: {trip.driver_id}, Vehicle ID: {trip.vehicle_id}, Start Time: {trip.start_time}, End Time: {trip.end_time}")
    else:
        click.echo("No trips found.")


if __name__ == '__main__':
    main()