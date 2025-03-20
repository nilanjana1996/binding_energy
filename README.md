# binding_energy
Extracting binding energy from virtual screening results
#Description
This code extracts the binding energies for thousands of molecules docked using Autodock vina. In Autodock vina, generally the binding energies, docking scores are stored in a "logfile.txt" file, and the docked ligand (with the docked pose) is stores as *_out.pdbqt. This code sorts the output, extracts the binding energy from each of them, and save the output file as "binding_energies.txt" where binding energy, and their corresponding ligand names can be found.
   
