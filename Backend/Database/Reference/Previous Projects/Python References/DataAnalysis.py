# Lab 5 - Data Analysis
# Author: Dan Beck
# Date: April 19, 2020
# This file allows a user to load one of two CSV files and then perform 
# histogram analysis and plots for select variables on the datasets. The first
# dataset represents the population change for specific dates for U.S. 
# regions. The second dataset represents Housing data over an extended period 
# of time describing home age, number of bedrooms and oconther variables.

import pandas as pd
import matplotlib.pyplot as plt

#***************Variables****************
pop_changes = pd.read_csv('PopChange.csv')
#Listing of the column headings in the pop change file
pop_changes.columns = ['ID', 'Geo', 'GeoID1', 'GeoID2', 'Pop1', 'Pop2',
                        'ChangePop']

housing = pd.read_csv('Housing.csv')
#Listing of the column headings in the housing file
housing.columns = ['Age', 'Bedrooms', 'Year Built', 'Units', 'Rooms', 'Weight',
                       'Utility'] 
        
#**********Functions for the code********** 
#**********5th Level**********
def histogram_set(values):
    """Generates the histogram"""
    new_list = values.tolist()
    n, bins, patches = plt.hist(new_list, 500)
    
    # Save Figure for Download
    plt.savefig('HISTOGRAM.svg')
    
#**********4th Level**********      
def scan_column(file, col):
    """
    Scans the selected file and prints data

    Parameters
    ----------
    file : Datafrmae
        Sets the filename to be scanned.
    col : Integer
        Sets the column in the file to be scanned
    """
    print(f'\tCount = {file.iloc[:,col].count()}')
    print(f'\tMean = {file.iloc[:,col].mean():.1f}')
    print(f'\tStandard Deviation = {file.iloc[:,col].std():.1f}')
    print(f'\tMin = {file.iloc[:,col].min():.1f}')
    print(f'\tMax = {file.iloc[:,col].max():.1f}')
    histogram_set(file.iloc[:,col])
    print('\nThe History of this column can be downloaded now')

#**********3rd Level**********
def read_pop_changes_file(choice):
    """Reads the CSV file for population change"""
    if choice == "A":
        scan_column(pop_changes, 4)
    elif choice == "B":
        scan_column(pop_changes, 5)
    elif choice == "C":
        scan_column(pop_changes, 6)
        
def read_housing_file(choice):
    """Reads the CSV file for housing data"""
    if choice == "A":
        scan_column(housing, 0)
    elif choice == "B":
        scan_column(housing, 1)
    elif choice == "C":
        scan_column(housing, 2)
    elif choice == "D":
        scan_column(housing, 4)
    elif choice == "E":
        scan_column(housing, 6)

#**********2nd Level (for Population)**********
def selected_pop_apr():
    """Runs though statistics if user selects pop apr 1"""
    print("\nYou have selected Pop Apr 1")
    read_pop_changes_file('A')
    
def selected_pop_jul():
    """Runs though statistics if user selects pop jul 1"""
    print("\nYou have selected Pop Jul 1")
    read_pop_changes_file('B')
    
def selected_change_pop():
    """Runs though statistics if user selects change pop"""
    print("\nYou have selected Change Pop")
    read_pop_changes_file('C')
    
#**********2nd Level (for Housing)**********
def selected_age():
    """Runs though statistics if user selects age"""
    print("\nYou have selected Age\n")
    read_housing_file('A')
    
def selected_bedrooms():
    """Runs though statistics if user selects bedroom"""
    print("\nYou have selected Bedrooms\n")
    read_housing_file('B')

def selected_year_built():
    """Runs though statistics if user selects year built"""
    print("\nYou have selected Year Built\n")
    read_housing_file('C')
    
def selected_rooms():
    """Runs though statistics if user selects room"""
    print("\nYou have selected Rooms\n")
    read_housing_file('D')

def selected_utility():
    """Runs though statistics if user selects utility"""
    print("\nYou have selected Utility\n")
    read_housing_file('E')

#**********1st Level**********
def selected_population():
    """Brings up columns to analyze if user selects population"""
    print("\nYou have selected Population Data")
    while True:
        try:
            selectedChoice = str(input("Select the column you want to "
                                        "analyze: "
                                        "\n\tA. Pop Apr 1"
                                        "\n\tB. Pop Jul 1"
                                        "\n\tC. Change Pop"
                                        "\n\tD. Exit Column\n")).capitalize()
            if selectedChoice == "A":
                selected_pop_apr()
            elif selectedChoice == "B":
                selected_pop_jul()
            elif selectedChoice == "C":
                selected_change_pop()
            elif selectedChoice == "D":
                break
            else:
                print("\nPlease enter A, B, C, or D")
        except:
            print("\nERROR - Please enter A, B, C, or D")

def selected_housing():
    """Brings up columns to analyze if user selects population"""
    print("\nYou have selected Housing Data")
    while True:
        try:
            selectedChoice = str(input("Select the column you want to "
                                        "analyze: "
                                        "\n\tA. Age"
                                        "\n\tB. Bedrooms"
                                        "\n\tC. Year Built"
                                        "\n\tD. Rooms"
                                        "\n\tE. Utility"
                                        "\n\tF. Exit Column\n")).capitalize()
            if selectedChoice == "A":
                selected_age()
            elif selectedChoice == "B":
                selected_bedrooms()
            elif selectedChoice == "C":
                selected_year_built()
            elif selectedChoice == "D":
                selected_rooms()
            elif selectedChoice == "E":
                selected_utility()
            elif selectedChoice == "F":
                break
            else:
                print("\nPlease enter A, B, C, D, E or F")
        except:
            print("\nPlease enter A, B, C, D, E or F")

def selected_exit():
    """Exits the program"""
    print("\nThank you for using the Data Analysis Application")
    print("\n***************************************************************")
    
#*********Executes the code**********

#Start of the program printout
print("****Welcome to the Data Analysis Application.****")
        
#Main body of the code that calls the first level of functions
while True:#Main
    try:
        selectedChoice = int(input("\nSelect the file you would like to "
                                   "analyze: "
                                   "\n\t1. Population Data"
                                   "\n\t2. Housing Data"
                                   "\n\t3. Exit the Program\n"))
        if selectedChoice == 1:
            selected_population()
        elif selectedChoice == 2:
            selected_housing()
        elif selectedChoice == 3:
            selected_exit()
            break
        else:
            print("\nPlease enter 1, 2, or 3")
    except:
        print("\nError Occured")