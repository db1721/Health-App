# Lab 4 - Data Munging
# Author: Dan Beck
# Date: April 10, 2020
# This file uses Python Panda, Regular Expressions, .map() and other functions
# as appropriate to format existing address records and eliminate records with 
# missing critical fields. Critical fields include FirstName, Lastname, 
# Zipcode+4, and Phone number for customers. For this exercise, create an array 
# to hold data with these 4 fields containing at least 25 records.

import pandas as pd
import re

#**********1st Level functions**********

def get_formatted_first_name(value):
    """Formats the first name"""
    if re.fullmatch(r'([A-Z][a-z]+)',value):
        new_val = re.fullmatch(r'([A-Z][a-z]+)',value)
        return ''.join(new_val.groups())
    else:
        return ""

def get_formatted_last_name(value):
    """Formats the last name"""
    if re.fullmatch(r'([A-Z][a-z]+)',value):
        new_val = re.fullmatch(r'([A-Z][a-z]+)',value)
        return ''.join(new_val.groups())
    else:
        return ""

def get_formatted_zip(value):
    """Formats the zip code"""
    if re.fullmatch(r'(\d{5})(\d{4})',value):
        new_val = re.fullmatch(r'(\d{5})(\d{4})',value)
        return '-'.join(new_val.groups())
    if re.fullmatch(r'(\d{5})-(\d{4})',value):
        return value
    elif re.fullmatch(r'(\d{5})',value):
        return value
    else:
        return ""

def get_formatted_phone(value):
    """Formats the phone number"""
    if re.fullmatch(r'(\d{3})(\d{3})(\d{4})',value):
        new_val = re.fullmatch(r'(\d{3})(\d{3})(\d{4})',value)
        return '-'.join(new_val.groups())
    elif re.fullmatch(r'(\d{3})-(\d{3})-(\d{4})',value):
        return value
    else:
        return ""

#*********Formats the array**********
#List of contacts
contacts = [['Jim', 'Robertson', '21801', '555-555-5555'],
            ['John', 'Adams', '223211143', '4444444444'],
            ['Helen', 'Cooper', 'edskd-2134', '323232'],
            ['', 'Franklin', '234511' , '323-333-2211'],
            ['Tom', 'Brady', '12121', '2322143423'],
            ['Lamar', 'Jackson', '983466740', '42423533333'],
            ['Joe', 'Flacco', '34694', '343-433-g321'],
            ['Giannis', 'Antemaohdgsbgo', '76363-2822', '234-432-3457'],
            ['LeBron', 'James', '25226', '336-346-3433'],
            ['Pam', 'B3asley', '23262', '235739624'],
            ['Jim', 'Halpert', '235472721', '1346272789'],
            ['Michael', 'Scott', '23624', '2346620000'],
            ['Dwight', 'Schrute', '15153', '2352354624'],
            ['Bob', 'Vance', 'ser443', '235n252526'],
            ['Phillip', 'Rivers', '23525', '234-744-4747'],
            ['Josh', 'Allen', '25225-3244', '3246368765'],
            ['Drew', 'Brees', '23525', '3463986363'], 
            ['Cam', 'Newton', 'st34t', '252-256-2623'],
            ['Teddy', 'Bridgewater', '23526', '234-2334-523'],
            ['Jameis', 'Winston', '23525', '2347631567'],
            ['Andrew', 'Luck', '24672', '9087235323'],
            ['Drew', 'Lock', '34634', '246363-3473'],
            ['baker', 'Mayfeild', '345d3', '2324663213'],
            ['Patrick', 'Mahomes', '234636644', 'r45-535-8790'],
            ['Jared', 'Goff', '34636', '4567651902'],
            ['Garner', 'Minshew', '42352', '457-653-6376']]

#Creates the column names
contactsdf = pd.DataFrame(contacts, columns=['First Name','Last Name', 
                                            'Zip Code','Phone Number'])
#Format the first name
formatted_first_name = contactsdf['First Name'].map(get_formatted_first_name)
contactsdf['First Name'] = formatted_first_name

#Format the last name
formatted_last_name = contactsdf['Last Name'].map(get_formatted_last_name)
contactsdf['Last Name'] = formatted_last_name

#Format the zip code
formatted_zip = contactsdf['Zip Code'].map(get_formatted_zip)
contactsdf['Zip Code'] = formatted_zip

#Format the phone number
formatted_phone = contactsdf['Phone Number'].map(get_formatted_phone)
contactsdf['Phone Number'] = formatted_phone

#*********Executes the code**********
print(contactsdf)