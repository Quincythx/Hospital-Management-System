Hospital Management System (Command-Line Python Project)

Overview

This is a command-line Hospital / Clinic Management System built in Python.
It allows hospital staff to manage:
	•	Patients (register, view)
	•	Doctors (add, view)
	•	Appointments (book, view)
	•	Medical reports (add, view)

All data is stored in JSON files, making it simple to save and load records.


Features
	1.	Register new patients
	2.	View all patients
	3.	Add new doctors
	4.	View all doctors
	5.	Book appointments (linking patients and doctors)
	6.	View all appointments
	7.	Add medical reports for patients
	8.	View medical reports for a specific patient


Installation / How to Run
	1.	Make sure Python 3.10 or higher is installed.
	2.	Clone or download the repository.
	3.	Open the project folder in VS Code (or your preferred editor).
	4.	Open the terminal and run:
           python main.py
	5.	The program will display a menu with options.
	6.	Choose an option by typing its number and follow the prompts.


Project Structure

hospital_management/
│
├── main.py                # Main program file
├── patients.json          # Stores patient data
├── doctors.json           # Stores doctor data
├── appointments.json      # Stores appointments data
├── medical_reports.json   # Stores medical report data
└── README.md              # This file


Usage Example
	1.	Register a patient → Add Name, Age, Gender
	2.	Add a doctor → Add Name, Specialization
	3.	Book an appointment → Enter patient ID, doctor ID, date
	4.	Add a medical report → Enter patient ID, doctor ID, diagnosis, prescription, date
	5.	View patients, doctors, appointments, or reports at any time using the menu


Notes
	•	Patient, doctor, and appointment IDs are auto-generated.
	•	JSON files must exist in the same folder as main.py (already included).
	•	This project runs completely in the terminal; no GUI or web interface is required.
