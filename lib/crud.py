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



def get_patients_dict():
    session = SessionLocal()
    patients = session.query(Patient).all()
    session.close()
    return {p.id: p.name for p in patients}

def add_doctor(name, specialty, phone):
    session = SessionLocal()
    doctor = Doctor(name=name, specialty=specialty, phone=phone)
    session.add(doctor)
    session.commit()
    session.close()
    return doctor
