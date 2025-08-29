from .database import SessionLocal
from .models import Patient, Doctor, Appointment
from datetime import datetime
from sqlalchemy.orm import joinedload

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

def get_doctors_list():
    session = SessionLocal()
    doctors = session.query(Doctor).all()
    session.close()
    return [(d.id, d.name, d.specialty, d.phone) for d in doctors]

def schedule_appointment(patient_id, doctor_id, date_str, reason):
    session = SessionLocal()
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    appointment = Appointment(
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_date=date_obj,
        reason=reason
    )
    session.add(appointment)
    session.commit()
    session.close()
    return appointment


def get_appointments_list():
    session = SessionLocal()
    appointments = session.query(Appointment)\
        .options(joinedload(Appointment.patient), joinedload(Appointment.doctor))\
        .all()

    result = []
    for a in appointments:
        patient_name = a.patient.name if a.patient else "Unknown Patient"
        doctor_name = a.doctor.name if a.doctor else "Unknown Doctor"

        result.append({
            "id": a.id,
            "patient": patient_name,
            "doctor": doctor_name,
            "date": a.appointment_date,
            "reason": a.reason,
            "status": a.status
        })

    session.close()
    return result
