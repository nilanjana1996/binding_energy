#!/bin/bash
# Author: Nilanjana Mani 

# Output file to store the results
output_file="binding_energies.txt"

# Clear the output file if it exists
> $output_file

# Loop through all files matching the pattern
for file in IMPHY00*.pdbqt_log.log
do
    # Extract the file name without extension
    file_name=$(basename "$file" .pdbqt_log)
    
    # Extract the first binding energy using grep and awk
    binding_energy=$(grep -m 1 -oP '^\s*\d+\s+(-\d+\.\d+)' "$file" | awk '{print $2}')
    
    # Write the result to the output file
    echo "$file_name $binding_energy" >> $output_file
done
