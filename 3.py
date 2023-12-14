# Write a Python program to find the sum and average of numbers of a given list.

def calculate_sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if len(numbers) > 0 else 0
    return total, average

input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in input_numbers.split() if x.replace(".", "", 1).isdigit()]

if not numbers:
    print("Please enter at least one valid number.")
else:
    sum_result, average_result = calculate_sum_and_average(numbers)
    print(f"Sum: {sum_result}")
    print(f"Average: {average_result}")
