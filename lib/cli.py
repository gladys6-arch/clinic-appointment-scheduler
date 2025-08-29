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


#doctors
@click.command()
@click.option("--name", prompt="Doctor Name")
@click.option("--specialty", prompt="Specialty")
@click.option("--phone", prompt="Phone Number")
def create_doctor(name, specialty, phone):
    add_doctor(name, specialty, phone)
    click.echo("Doctor added successfully!")

@click.command()
def list_doctors():
    doctors = get_doctors_list()
    click.echo("Doctors:")
    for d in doctors:
        click.echo(f"{d}")

#Appointments
@click.command()
@click.option("--patient_id", prompt="Patient ID", type=int)
@click.option("--doctor_id", prompt="Doctor ID", type=int)
@click.option("--date", prompt="Appointment Date (YYYY-MM-DD)")
@click.option("--reason", prompt="Reason for appointment")
def create_appointment(patient_id, doctor_id, date, reason):
    schedule_appointment(patient_id, doctor_id, date, reason)
    click.echo("Appointment scheduled!")

@click.command()
def list_appointments():
    appointments = get_appointments_list()
    click.echo("Appointments:")
    for a in appointments:
        click.echo(a)


  # Add commands to CLI
cli.add_command(create_patient)
cli.add_command(list_patients)
cli.add_command(create_doctor)
cli.add_command(list_doctors)
cli.add_command(create_appointment)
cli.add_command(list_appointments)

if __name__ == "__main__":
    cli()
    
        
