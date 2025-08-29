import click

from .crud import (
  add_patient, get_patients_list, get_patients_dict,
    add_doctor, get_doctors_list,
    schedule_appointment, get_appointments_list
)

@click.group()
def cli():
  """Clinic Appointment Scheduler CLI"""
  pass

