import json
import os

# LOAD FUNCTION
def load_data(filename):
    if not os.path.exists(filename):
        return []
    
    with open(filename, "r") as file:
        return json.load(file)
    

# SAVE FUNCTION
def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# REGISTER PATIENT FUNCTION
def register_patient():
    patients = load_data("patients.json")

    print("\n--- Register New Patient ---")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")

    patient = {
        "id": len(patients) + 1,
        "name": name,
        "age": age,
        "gender": gender
    }

    patients.append(patient)
    save_data("patients.json", patients)

    print("Patient registered successfully.")


# VIEW PATIENT FUNCTION
def view_patients():
    patients = load_data("patients.json")

    print("\n--- Patient List ---")

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print(patient)




# TEST CALL
# register_patient()
# view_patients()




# ADD A DOCTOR
def add_doctor():
    doctors = load_data("doctors.json")

    print("\n--- Add New Doctor ---")
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")

    doctor = {
        "id": len(doctors) + 1,
        "name": name,
        "specialization": specialization
    }

    doctors.append(doctor)
    save_data("doctors.json", doctors)

    print("Doctor added successfully.")



#VIEW DOCTORS
def view_doctors():
    doctors = load_data("doctors.json")

    print("\n--- Doctor List ---")

    if not doctors:
        print("No doctors found.")
        return

    for doctor in doctors:
        print(doctor)


# TEST CALL
# add_doctor()
# view_doctors()



# BOOK APPOINTMENT
def book_appointment():
    appointments = load_data("appointments.json")

    print("\n--- Book Appointment ---")

    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    date = input("Enter appointment date (DD-MM-YYYY): ")

    appointment = {
        "id": len(appointments) + 1,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date
    }

    appointments.append(appointment)
    save_data("appointments.json", appointments)

    print("Appointment booked successfully.")



# VIEW APPOINTMENTS
def view_appointments():
    appointments = load_data("appointments.json")

    print("\n--- Appointments List ---")

    if not appointments:
        print("No appointments found.")
        return

    for appointment in appointments:
        print(appointment)


# TEST CALL
# book_appointment()
# view_appointments()



# ADD MEDICAL REPORT
def add_medical_report():
    reports = load_data("medical_reports.json")

    print("\n--- Add Medical Report ---")

    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    diagnosis = input("Enter diagnosis: ")
    prescription = input("Enter prescription: ")
    date = input("Enter date (DD-MM-YYYY): ")

    report = {
        "id": len(reports) + 1,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": diagnosis,
        "prescription": prescription,
        "date": date
    }

    reports.append(report)
    save_data("medical_reports.json", reports)

    print("Medical report added successfully.")




# VIEW MEDICAL REPORTS
def view_medical_reports():
    reports = load_data("medical_reports.json")

    print("\n--- View Medical Reports ---")
    patient_id = input("Enter patient ID: ")

    found = False

    for report in reports:
        if report["patient_id"] == patient_id:
            print(report)
            found = True

    if not found:
        print("No medical reports found for this patient.")


# TEST CALL
# add_medical_report()
# view_medical_reports()


def main_menu():
    while True:
        print("\n==============================")
        print("  Hospital Management System")
        print("==============================")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. View Appointments")
        print("7. Add Medical Report")
        print("8. View Medical Reports")
        print("9. Exit")
        
        choice = input("Choose an option (1-9): ")

        if choice == "1":
            register_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            add_doctor()
        elif choice == "4":
            view_doctors()
        elif choice == "5":
            book_appointment()
        elif choice == "6":
            view_appointments()
        elif choice == "7":
            add_medical_report()
        elif choice == "8":
            view_medical_reports()
        elif choice == "9":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()