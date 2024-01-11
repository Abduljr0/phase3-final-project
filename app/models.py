from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import sessionmaker
from main import Base , datetime,engine

 #Driver Model
class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship("Vehicle", back_populates="drivers")
    
    def __repr__(self) :
        return super().__repr__()

# Vehicle Model
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    registration_number = Column(String)
    drivers = relationship("Driver", back_populates="vehicle")

    def __repr__(self) :
        return super().__repr__()

# Trip Model
class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime)

    def __repr__(self) :
        return super().__repr__()

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

