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

def get_patients_list():
    session = SessionLocal()
    patients = session.query(Patient).all()
    session.close()
    return [(p.id, p.name, p.age, p.gender, p.contact) for p in patients]
