import os
import re

# Author: Nilanjana Mani

# Output file to store the results
output_file = "binding_energies.txt"

# Clear the output file if it exists
with open(output_file, 'w') as f:
    f.write('')

# Loop through all files in the directory and sort them by name
for file in sorted(os.listdir()):
    if file.endswith(".pdbqt_log.log"):
        # Extract the file name without extension
        file_name = os.path.splitext(file)[0]

        # Extract the first binding energy using regex
        with open(file, 'r') as f:
            content = f.read()
            match = re.search(r'^\s*\d+\s+(-\d+\.\d+)', content, re.MULTILINE)
            if match:
                binding_energy = match.group(1)
                
                # Write the result to the output file
                with open(output_file, 'a') as out_f:
                    out_f.write(f"{file_name} {binding_energy}\n")
