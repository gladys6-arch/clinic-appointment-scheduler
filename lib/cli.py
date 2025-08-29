

from lib.crud import (
  add_patient, get_patients_list, 
    add_doctor, get_doctors_list,
    schedule_appointment, get_appointments_list
)

from datetime import datetime

def main_menu():
    while True:
        print("\n=== Clinic Appointment Scheduler ===")
        print("1. Create Patient")
        print("2. List Patients")
        print("3. Create Doctor")
        print("4. List Doctors")
        print("5. Schedule Appointment")
        print("6. List Appointments")
        print("0. Exit")

        choice = input("Select an option: ").strip()


    if choice == "1":
            name = input("Patient Name: ")
            age = int(input("Patient Age: "))
            gender = input("Patient Gender: ")
            contact = input("Patient Contact: ")
            add_patient(name, age, gender, contact)
            print("Patient added successfully!")

    elif choice == "2":
            patients = get_patients_list()
            print("\nPatients:")
            for p in patients:
                print(p)




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


