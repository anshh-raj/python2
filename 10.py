# Write a Python program to count the number of vowels in a file and write the vowel: count in a
# dictionary.

def count_vowels(file_path):
    vowels = "aeiouAEIOU"
    vowel_count = {vowel: 0 for vowel in vowels}

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for char in content:
                if char in vowels:
                    vowel_count[char] += 1
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

    return vowel_count

file_path = "vowel.txt"

vowel_count_dict = count_vowels(file_path)

if vowel_count_dict is not None:
    print("Vowel Count Dictionary:")
    for vowel, count in vowel_count_dict.items():
        print(f"{vowel}: {count}")
