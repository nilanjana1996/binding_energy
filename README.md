# binding_energy
Extracting binding energy from virtual screening results
#Description
This code extracts the binding energies for thousands of molecules docked using Autodock vina. In Autodock vina, generally the binding energies, docking scores are stored in a "logfile.txt" file, and the docked ligand (with the docked pose) is stores as *_out.pdbqt. This code sorts the output, extracts the binding energy from each of them, and save the output file as "binding_energies.txt" where binding energy, and their corresponding ligand names can be found.
   

#Usage (for the python script):

Create a directory, "output_file"
Cd to the directory.
Then run,
python3 binding_energy.py


#Usage (for the bash script):

Change the name of the files to loop through at line 11 depending on the filenames you are working with.
Make it executable using the following command, chmod +x scriptname.sh
If you are using WSL, run sed -i 's/\r$//' scriptname.sh (not needed if you are on cygwin)
Pull all the autodock vina output files (only the log files) in a sub directory and copy the script file in the same directory.
Run it using ./scripname.sh
Output will be saved as binding_energies.txt in your current working directory.

