# Given a list of numbers, write a Python program to count the number of times an element occurs in a
# list and create a dictionary with element:count as key:value pairs.

def count_elements(lst):
    element_count_dict = {}
    
    for element in lst:
        if element in element_count_dict:
            element_count_dict[element] += 1
        else:
            element_count_dict[element] = 1
    
    return element_count_dict

numbers_list = [1, 2, 3, 1, 2, 4, 1, 3, 5]

element_count_dictionary = count_elements(numbers_list)

print("Original List:", numbers_list)
print("Element Count Dictionary:", element_count_dictionary)
