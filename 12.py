# Write a Python program library to read the CSV file created in the above program and filter out
# records of II semester students.

import csv

def filter_semester_records(csv_file_path, target_semester):
    filtered_records = []

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if int(row["Semester"]) == target_semester:
                filtered_records.append(row)

    return filtered_records

csv_file_path = "student_data.csv"

target_semester = 2

filtered_records = filter_semester_records(csv_file_path, target_semester)

if filtered_records:
    print(f"Records for {target_semester} semester:")
    for record in filtered_records:
        print(record)
else:
    print(f"No records found for {target_semester} semester.")
