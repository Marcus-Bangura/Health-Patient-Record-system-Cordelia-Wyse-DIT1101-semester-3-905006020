HEALTH PATIENT RECORD SYSTEM

1. Project Overview

The Health Patient Record System is a simple Python-based application developed as an Object-Oriented Programming (OOP1) assignment.

The system is designed to manage patient information by allowing new patients to register, existing patients to sign in, and users to search for and view patient records.

It uses Object-Oriented Programming concepts and file handling to organize and store patient information.

2. Objectives of the Project

The main objectives of this project are to:

* Create and manage patient records.
* Allow new patients to register.
* Allow existing patients to sign in using their Patient ID.
* Store patient information for future use.
* Search for patients using their unique IDs.
* Display all registered patient records.
* Demonstrate the application of Object-Oriented Programming concepts in Python.

3. Technologies Used

* Programming Language: Python
* Code Editor: Visual Studio Code
* Version Control: Git and GitHub
* Data Storage: JSON file
* Libraries: JSON and OS (Python standard libraries)

4. System Features

The system provides the following functionalities:

A. Patient Registration

New patients can register by providing:

* Patient ID
* Full Name
* Age
* Appointment Reason

B. Patient Sign-In

Previously registered patients can sign in using their Patient ID to retrieve their saved information.

C. Search Patient Record

The system allows users to search for a particular patient using their unique Patient ID.

D. Display All Patient Records

The system displays all registered patients and their information.

E. Data Storage

Patient information is saved in a JSON file named patient_records.json. This allows records to remain available after the program is closed.

F. Exit

Users can safely exit the application through the main menu.

5. Object-Oriented Programming Concepts Used

The project demonstrates the following OOP concepts:

1. Classes: The system contains two main classes: Patient and PatientRecordSystem.
2. Objects: Patient objects are created to represent individual patients.
3. Constructor: The __init__() method initializes patient information and system attributes.
4. Instance Methods: Methods such as display_record() perform operations on individual patient objects.
5. Class Methods: The get_total_patients() method retrieves the total number of registered patients.
6. Encapsulation: Patient information and related operations are organized within classes.
7. Dictionary: A dictionary is used to store patient objects using their unique Patient IDs.
8. File Handling: JSON is used to save and retrieve patient information.

6. How to Run the Program

Follow these steps to run the application:

1. Install Python on your computer.
2. Open Visual Studio Code.
3. Create a Python file named health_patient_record_system.py.
4. Copy and paste the project code into the file.
5. Save the file.
6. Open the terminal in Visual Studio Code.
7. Run the following command:

python health_patient_record_system.py

8. Select an option from the main menu to use the system.

7. Main Menu Options

When the program runs, the following menu is displayed:

1. Register New Patient
2. Patient Sign In
3. Search Patient Record
4. Display All Patient Records
5. Exit

Users can select an option by entering the corresponding number.

8. Data Storage

The system automatically creates a JSON file called patient_records.json when patient records are saved.

The file stores patient IDs, names, ages and appointment reasons.

The saved information can be retrieved when the application is opened again, provided the JSON file remains in the same project folder.

9. Limitations

* The system uses Patient IDs for sign-in without password authentication.
* It does not include a graphical user interface.
* Patient records are stored locally in a JSON file.
* It is a demonstration project and is not intended for storing real confidential medical information.

10. Conclusion

The Health Patient Record System demonstrates how Object-Oriented Programming can be applied to develop a simple patient management application.

It provides basic patient registration, sign-in, searching, record display and data storage functionalities.

Through this project, practical knowledge of Python classes, objects, methods, dictionaries, conditional statements, loops and file handling has been demonstrated.

The project also provides an opportunity to understand how programming can be used to simplify patient record management.

⸻

Project: Health Patient Record System
Course: Object-Oriented Programming I (OOP1)
Language: Python
Institution: Limkokwing University of Creative Technology, Sierra Leone
Data: Fictional demonstration records only
