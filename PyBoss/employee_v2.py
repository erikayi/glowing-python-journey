# import the dependencies 
import csv
import os

# define the employee_data.csv file that holds current employee data
employee_data = os.path.join("data/employee_data.csv")

with open(employee_data, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    firstname = [row[1].split(" ")[0] for row in reader]
    print(firstname)
       