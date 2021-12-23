import csv
import pandas as pd
                
class Student:

    def __init__(self, name, score, rank):
        self.name = name
        self.score = score
        self.rank = rank
        
    @property
    def name(self):
        return self.name
    
    # @name.setter
    # def name(self):
    #     return self.name


student_list = []

with open('PopChange.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None)  # Skip the header.
    # Unpack the row directly in the head of the for loop.
    for name, score1, score2, rank, ags, asfa, asd in reader:
        # Convert the numbers to floats.
        name = str(name)
        score1 = str(score1)
        score2 = str(score2)
        rank = float(rank)
        ags = float(ags)
        asfa = float(asfa)
        asd = float(asd)
        # Now create the Student instance and append it to the list.
        student_list.append(Student(name, (score1, score2), rank))

# Then do something with the student_list.

print(Student.score1)