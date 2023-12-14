# Write a Python program to create a text file having atleast five lines about your college using
# writelines() function.

file_name = "college_description.txt"

college_description = [
    "Welcome to ARSD College!",
    "ARSD College is known for its outstanding academic programs.",
    "Our campus is equipped with state-of-the-art facilities and a vibrant student community.",
    "Dedicated faculty members strive for excellence in teaching and research.",
    "Join us at ARSD College and embark on a journey of knowledge and personal growth."
]

with open(file_name, 'w') as file:
    file.writelines(line + '\n' for line in college_description)

print(f"The file '{file_name}' has been created with a description of the college.")
