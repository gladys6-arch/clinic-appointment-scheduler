from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import date

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String)
    contact = Column(String)
    join_date = Column(Date, default=date.today)
    appointments = relationship("Appointment", back_populates="patient")

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    specialty = Column(String)
    hire_date = Column(Date, default=date.today)
    phone = Column(String)
    appointments = relationship("Appointment", back_populates="doctor")
