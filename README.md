# Hospital Management System (Command-Line Python Project)

## Overview

This is a command-line Hospital / Clinic Management System built in Python.
It allows hospital staff to manage:\
  •	Patients: register and view\
	•	Doctors: add and view\
	•	Appointments: book and view\
	•	Medical Reports: add and view

All data is stored in JSON files, making it easy to save and retrieve records.

## Features
Feature	Description
* Register Patient	Add new patients to the system
* View Patients	List all patients
* Add Doctor	Add new doctors
* View Doctors	List all doctors
* Book Appointment	Link a patient and a doctor on a specific date
* View Appointments	See all appointments
* Add Medical Report	Add diagnosis and prescription for a patient
* View Medical Reports	View all medical reports of a patient

## Installation & Running
	1.  Install Python 3.10 or higher.
	2.	Clone or download this repository.
	3.	Open the project folder in VS Code (or your preferred editor).
	4.	Open the terminal and run:
          `python main.py`
	5.	Follow the menu prompts.

## Project Structure

hospital_management/\
├── main.py               # Main program file\
├── patients.json         # Stores patient data\
├── doctors.json          # Stores doctor data\
├── appointments.json     # Stores appointment data\
├── medical_reports.json  # Stores medical report data\
└── README.md             # Project documentation

## Usage Example
	1.	Register Patient → Enter Name, Age, Gender
	2.	Add Doctor → Enter Name, Specialization
	3.	Book Appointment → Enter Patient ID, Doctor ID, Date
	4.	Add Medical Report → Enter Patient ID, Doctor ID, Diagnosis, Prescription, Date
	5.	View patients, doctors, appointments, or reports at any time
	6.	Exit → Type 9 in the menu

## Notes
	•	IDs for patients, doctors, and appointments are auto-generated.
	•	JSON files must exist in the same folder as main.py.
	•	This project is fully command-line based; no GUI or web interface.
