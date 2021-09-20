# import the dependencies 
import csv
import os

# define the employee_data.csv file that holds current employee data
employee_data = os.path.join("data/employee_data.csv")

# open the data 
with open(employee_data, 'r') as csvfile:
    reader = csv.reader(csvfile)

    # parse csv data in python
    for row in reader:
        print(row)

# with open('data/employee_data.csv', 'r') as splitnames:
#     reader = csv.reader(splitnames, delimiter=',')
#     newcsvdict = {"First Name": [], "Last Name": []}
#     for row in reader:
#         first = row[0].split(" ")[0]
#         last = row[0].split(" ")[1]
#         newcsvdict['First Name'].append(first)
#         newcsvdict['Last Name'].append(last)
#         print(row)
       