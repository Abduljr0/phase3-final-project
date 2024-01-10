from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
engine = create_engine("sqlite:///taxi_database.db") 
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session() 

# Driver Model
class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship("Vehicle", back_populates="drivers")

# Vehicle Model
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    registration_number = Column(String)
    drivers = relationship("Driver", back_populates="vehicle")

# Trip Model
class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

