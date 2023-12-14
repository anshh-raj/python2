# Write a Python program to swap the first two and last two characters of a given string.

def swap_first_and_last_two_chars(input_str):
    if len(input_str) < 2:
        return input_str 
    
    first_two_chars = input_str[:2]
    last_two_chars = input_str[-2:]
    middle_chars = input_str[2:-2]
    
    swapped_str = last_two_chars + middle_chars + first_two_chars
    return swapped_str

input_string = input("Enter a string: ")

result_string = swap_first_and_last_two_chars(input_string)

print("Original String:", input_string)
print("Swapped String:", result_string)
