from .database import SessionLocal
from .models import Patient, Doctor, Appointment
from datetime import datetime

def add_patient(name, age, gender, contact):
    session = SessionLocal()
    patient = Patient(name=name, age=age, gender=gender, contact=contact)
    session.add(patient)
    session.commit()
    session.close()
    return patient