# Write a Python program to create a text file having names of ten Indian cities.

cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Lucknow"]

file_name = "indian_cities.txt"

with open(file_name, 'w') as file:
    for city in cities:
        file.write(city + '\n')

print(f"The file '{file_name}' has been created with the names of ten Indian cities.")
