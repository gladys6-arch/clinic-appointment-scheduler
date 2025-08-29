from .crud import (
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

        elif choice == "3":
            name = input("Doctor Name: ")
            specialty = input("Specialty: ")
            phone = input("Phone Number: ")
            add_doctor(name, specialty, phone)
            print("Doctor added successfully!")

        elif choice == "4":
            doctors = get_doctors_list()
            print("\nDoctors:")
            for d in doctors:
                print(d)

        elif choice == "5":
            patient_id = int(input("Patient ID: "))
            doctor_id = int(input("Doctor ID: "))
            date = input("Appointment Date (YYYY-MM-DD): ")
            reason = input("Reason: ")
            schedule_appointment(patient_id, doctor_id, date, reason)
            print("Appointment scheduled!")

        elif choice == "6":
            appointments = get_appointments_list()
            print("\nAppointments:")
            for a in appointments:
                print(a)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()











