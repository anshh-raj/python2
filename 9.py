# Write a Python program which reads the data from three input files having Employee Names and
# merges them into one output file.

input_files = ["input1.txt", "input2.txt", "input3.txt"]

output_file = "merged_output.txt"

def merge_files(input_files, output_file):
    with open(output_file, 'w') as output:
        for input_file in input_files:
            with open(input_file, 'r') as input_data:
                output.write(input_data.read())
                output.write('\n')  # Add a newline between data from different files

merge_files(input_files, output_file)

print(f"The data from {len(input_files)} input files has been merged into '{output_file}'.")
