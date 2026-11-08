"""
OOP1 Assignment: Health Patient Record System
A simple patient registration and record management system.
Uses fictional sample data for demonstration.
"""

import json
import os


# CLASS 1: PATIENT
class Patient:
    """Represents a patient's personal and appointment information."""

    total_patients = 0

    def __init__(self, patient_id, name, age, appointment_reason):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.appointment_reason = appointment_reason

    # Instance method
    def display_record(self):
        print("\n========== PATIENT INFORMATION ==========")
        print(f"Patient ID: {self.patient_id}")
        print(f"Full Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Appointment Reason: {self.appointment_reason}")
        print("=========================================")

    # Convert patient information into a dictionary
    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "appointment_reason": self.appointment_reason
        }

    # Class method to create a patient from saved data
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["patient_id"],
            data["name"],
            data["age"],
            data["appointment_reason"]
        )

    # Class method
    @classmethod
    def get_total_patients(cls):
        return cls.total_patients


# CLASS 2: PATIENT RECORD SYSTEM
class PatientRecordSystem:
    """Manages patient registration, sign-in and records."""

    def __init__(self):
        self.records = {}
        self.filename = "patient_records.json"
        self.load_records()

    # Load previously saved patient records
    def load_records(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                for patient_id, details in data.items():
                    self.records[patient_id] = Patient.from_dict(details)

            except (json.JSONDecodeError, KeyError, TypeError):
                print("Warning: Saved records could not be loaded.")
        else:
            print("Welcome! No previous patient records found.")

        Patient.total_patients = len(self.records)

    # Save patient records
    def save_records(self):
        data = {
            patient_id: patient.to_dict()
            for patient_id, patient in self.records.items()
        }

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Register a new patient
    def register_patient(self):

        print("\n========== PATIENT REGISTRATION ==========")

        patient_id = input("Enter Patient ID: ").strip().upper()

        if not patient_id:
            print("Patient ID cannot be empty.")
            return

        if patient_id in self.records:
            print("Error: This Patient ID already exists.")
            print("Please sign in instead.")
            return

        name = input("Enter Full Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than zero.")
                return

        except ValueError:
            print("Invalid age. Please enter a number.")
            return

        appointment_reason = input(
            "Enter Appointment Reason: "
        ).strip()

        if not appointment_reason:
            print("Appointment reason cannot be empty.")
            return

        # Create a Patient object
        patient = Patient(
            patient_id,
            name,
            age,
            appointment_reason
        )

        # Store the patient in the dictionary
        self.records[patient_id] = patient

        Patient.total_patients = len(self.records)

        # Save the information
        self.save_records()

        print("\nRegistration successful!")
        print("Your patient record has been saved.")

        patient.display_record()

    # Existing patient sign-in
    def patient_sign_in(self):

        print("\n========== PATIENT SIGN IN ==========")

        patient_id = input(
            "Enter your Patient ID: "
        ).strip().upper()

        patient = self.records.get(patient_id)

        if patient is not None:
            print("\nSign-in successful!")
            print("Welcome back, " + patient.name)

            # Display previously saved information
            patient.display_record()

        else:
            print("\nPatient record not found.")
            print("Please check your Patient ID or register.")

    # Display all patient records
    def display_all_patients(self):

        print("\n========== ALL PATIENT RECORDS ==========")

        if not self.records:
            print("No patient records available.")
            return

        for patient in self.records.values():
            patient.display_record()

        print(
            f"\nTotal Registered Patients: "
            f"{Patient.get_total_patients()}"
        )

    # Search for a patient
    def search_patient(self):

        print("\n========== SEARCH PATIENT ==========")

        patient_id = input(
            "Enter Patient ID to search: "
        ).strip().upper()

        patient = self.records.get(patient_id)

        if patient:
            print("\nPatient found!")
            patient.display_record()

        else:
            print("Patient not found.")


# MAIN PROGRAM
def main():

    system = PatientRecordSystem()

    while True:

        print("\n")
        print("========================================")
        print("     HEALTH PATIENT RECORD SYSTEM")
        print("========================================")
        print("1. Register New Patient")
        print("2. Patient Sign In")
        print("3. View All Patient Records")
        print("4. Search Patient")
        print("5. Exit")
        print("========================================")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            system.register_patient()

        elif choice == "2":
            system.patient_sign_in()

        elif choice == "3":
            system.display_all_patients()

        elif choice == "4":
            system.search_patient()

        elif choice == "5":
            print("\nThank you for using the Health Patient Record System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid option. Please select between 1 and 5.")


# PROGRAM EXECUTION
if __name__ == "__main__":
    main()