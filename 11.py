# Write a Python program to create a CSV file having student data: Roll_No, Enrollment No, Name,
# Course, Semester.

import csv

students_data = [
    {"Roll_No": 101, "Enrollment_No": "EN12345", "Name": "John Doe", "Course": "Computer Science", "Semester": 3},
    {"Roll_No": 102, "Enrollment_No": "EN67890", "Name": "Jane Smith", "Course": "Electrical Engineering", "Semester": 2},
    {"Roll_No": 103, "Enrollment_No": "EN54321", "Name": "Alice Johnson", "Course": "Mechanical Engineering", "Semester": 4},
    {"Roll_No": 104, "Enrollment_No": "EN98765", "Name": "Bob Williams", "Course": "Civil Engineering", "Semester": 1},
]

csv_file_name = "student_data.csv"

with open(csv_file_name, mode='w', newline='') as csv_file:
    fieldnames = ["Roll_No", "Enrollment_No", "Name", "Course", "Semester"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(students_data)

print(f"The CSV file '{csv_file_name}' has been created with student data.")
