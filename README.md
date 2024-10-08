# Codetown General Hospital Diet Selection System

## Programming Task 2 of UNE's COSC110 Introduction to Programming and the UNIX Environment

### Program Guide

This small, shell-based, Python program was an individual programming task for COSC110 at the University of New England (UNE).

While the exact requirements of the program remain the IP of UNE, the aim of the program is as following:
* Allows a hospital staff member choose the best standardised diet for a patient, based on the patient's nutrional needs. I.e. To choose among the available diets already within the hospital, that themselves have been set by international guidelines on what is needed for different health conditions.
* Firstly, the patient is selected by the staff member, based on their Patient ID.
* The staff member then enters the individual nutrional needs of the patient, i.e. their optimal daily protein, carbohydrates, and fat.
* Based on these individual needs, the program then runs a function over the internationally-provided diet guidelines. It finds which of the six set diets has the lowest absolute value error against the patient's individual dietary needs. This allows the system to select the best standardised diet that is available in the hospital.
* After selecting the best diet, the program performs two (2) actions:
  
  | No. | Action |
  | ----------- | ------ |
  | 1 | It prints to the screen the selected diet for the patient, so the hospital staff member is aware |
  | 2 | It generates or adds to a CSV file that includes (a) Patient ID (b) Diet Selected, so the hospital kitchen can later be sent the CSV for meal planning and prep |

* The program will then close.
---

### Instructions to use the program:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm meals.py is in directory with ls command.
4. Run program via the following command
   4.1 For Python 3 machines: python3 meals.py
   4.2 For machines with earlier Python versions: python meals.py
5. (Optional) To close program prior to completion of script
   5.1 Press Ctrl + Z on Unix systems

### Instructions to access the README.md in shell:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm README.md is in directory with ls command.
4. Run and Open README.md via the following command
   4.1 For Python 3 machines: pydoc3 ./meals.py
   4.2 For machines with earlier Python versions: pydoc meals.py
