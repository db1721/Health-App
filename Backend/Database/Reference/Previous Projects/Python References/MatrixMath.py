# Lab 4 - Matrix Math
# Author: Dan Beck
# Date: April 10, 2020
# This program allows a user to enter the values of two, 3x3 matrices and 
# then select from options including, addition, subtraction, matrix 
# multiplication, and element by element multiplication. You should use 
# numpy.matmul() for matrix multiplication (e.g. np.matmul(a, b) ). The program 
# should computer the appropriate results and return the results, the transpose 
# of the results, the mean of the rows for the results, and the mean of the 
# columns for the results.

import numpy as np

#**********Functions for the code**********

#**********4th Level**********

def printArray(array):
    """Prints values of array neatly"""
    print('\n'.join('  '.join(str(val) for val in row) for row in array))
    
#**********3rd Level**********
    
def secondaryFunctions(array):
    """Runs the second part of the programs caluclations after a math"
    " function is selected"""
    print("\nThe Transpose is: ")
    printArray(array.T)
    rows = array.mean(0)
    rows_formatted = ['{:.2f}'.format(x) for x in rows]
    columns = array.T.mean(0)
    columns_formatted = ['{:.2f}'.format(x) for x in columns]
    print("\nThe row and column mean values of the results are: ")
    print("Rows ", ', '.join(map(str,rows_formatted)))
    print("Columns: ", ', '.join(map(str,columns_formatted)))

#**********2nd Level**********
def buildMatrix():
    """Asks for user input and builds a 3x3 matrix from it"""
    n1, n2, n3 = list(map(int,input().split()))
    n4, n5, n6 = list(map(int,input().split()))
    n7, n8, n9 = list(map(int,input().split()))
    return np.array([n1, n2, n3, n4, n5 , n6, n7, n8, n9])
    
def mathFunctionInstr():
    """Instructions on how to use the program"""
    while True:
        try:
            print("\n\tSelect a Matrix Operation from the list below:")
            print("\tA. Addition")
            print("\tB. Subtraction")
            print("\tC. Matrix Multiplication")
            print("\tD. Element by element multiplication")
            a = str(input(""))
            return a
            break
        except:
            print("Please enter A, B, C, or D")

def mathFunctions(m, a, b):
    """Runs through the math function based on what user selects"""
    if m == "A":
        print("\nYou Selected Addition. The results are: ")
        added = np.add(a, b)
        printArray(added)
        secondaryFunctions(added)
    elif m == "B":
        print("\nYou Selected Subtraction. The results are: ")
        subtracted = np.subtract(a, b)
        printArray(subtracted)
        secondaryFunctions(subtracted)
    elif m == "C":
        print("\nYou Selected Matrix Multiplication. The results are: ")
        multiply = np.matmul(a, b)
        printArray(multiply)
        secondaryFunctions(multiply)
    elif m == "D":
        print("\nYou Selected Element by element multiplication."
              " The results are: ")  
        elementMultiply = np.multiply(a, b)
        printArray(elementMultiply)
        secondaryFunctions(elementMultiply)
    
#**********1st Level**********

def selectedYes():
    """Executes program if user selected yes"""
    print("\nEnter your first 3x3 Matrix: ")
    firstMatrix = buildMatrix()
    firstMatrix.resize(3, 3)
    print("\nEnter your second 3x3 Matrix: ")
    secondMatrix = buildMatrix()
    secondMatrix.resize(3, 3)
    print("\nFirst Matrix: ")
    printArray(firstMatrix)
    print("\nSecond Matrix: ")
    printArray(secondMatrix)
    m = mathFunctionInstr()
    mathFunctions(m.capitalize(), firstMatrix, secondMatrix)
        
def selectedNo():
    """Exits the program"""
    print("\nThank you for playing the Matrix Game")
    print("\n***************************************************************")
    
#*********Executes the code**********

#Start of the program printout
print("****Welcome to the Matrix Math Application.****")

#Main body of the code that calls the first level of functions

while True:
    try:
        selectedChoice = str(input("Do you want to play the Matrix Game"
                                   "\n\nEnter Y for Yes or N for "
                                   "No: ").capitalize())
        if selectedChoice == "Y":
            selectedYes()
        elif selectedChoice == "N":
            selectedNo() #Exits the application
            break
        else:
            print("\nPlease enter Y or N")
    except:
        print("\nError Occured")