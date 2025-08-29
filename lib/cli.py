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


#patients
@click.command()
@click.option("--name", prompt="Patient Name")
@click.option("--age", prompt="Patient Age", type=int)
@click.option("--gender", prompt="Patient Gender")
@click.option("--contact", prompt="Patient Contact")
def create_patient(name, age, gender, contact):
    if age <= 0:
        click.echo("Error: Age must be positive")
        return
    add_patient(name, age, gender, contact)
    click.echo("Patient added successfully!")

@click.command()
def list_patients():
    patients = get_patients_list()
    click.echo("Patients:")
    for p in patients:
        click.echo(f"{p}")