''' Alvaro is new to this '''

import os
import pathlib
from tracemalloc import start
import AlvaroQuinteroGonzalez_utils

base_directory = ("datafun-02-projects")

def create_folders_for_range(start_year, end_year):
    # Range will be in years
    start_year = 2020
    end_year = 2023
    for i in range(start_year, end_year + 1):
        folder_name = f"folder_{i}"
    folder_path = os.path.join(base_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

def create_folders_from_list(folder_list):
    # From list of names
    folder_names = ['data-csv', 'data-excel', 'data-json']
    for folder_name in folder_names:
        folder_path = os.path.join(base_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

def create_prefixed_folders(folder_list, prefixed):
    # Create prefixed folders from a list of names
    folder_names = ['data-csv', 'data-excel', 'data-json']
    prefix = 'data-'
    for folder_name in folder_names:
        prefixed_folder_name = prefix + folder_name
    folder_path = os.path.join(base_directory, prefixed_folder_name)
    os.makedirs(folder_path, exist_ok=True)

def main():
    '''Main function to demonstrate module capabilities'''

    # Pring byline from imported module
    print(f"byline:{AlvaroQuinteroGonzalez_utils}")

    # Call fuction 1 to create folder for a range (years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

# Call main function to execute the code
if __name__ == '__main__':
    main()
