# import the dependencies 
import csv
import os

# define the employee_data.csv file that holds current employee data
employee_data = os.path.join("data/employee_data.csv")

# open the data and split first and last name of the current data
with open(employee_data, 'r') as employeecsv:
    csvreader = csv.reader(employeecsv)
    newcsvdict = {"First Name": [], 
                  "Last Name": []}
    # next(csvreader)
    for row in csvreader:
        first_name = row[1].split()[0]
        last_name = row[1].split()[1]
        newcsvdict["First Name"].append(first_name)
        newcsvdict["Last Name"].append(last_name)

# with open(employee_data, 'r') as employeecsv:
#     csvreader = csv.reader(employeecsv)
#     next(csvreader)
#     last_name = [row[1].split(" ")[1] for row in csvreader]

# add splitted data in the new dataset

with open('new_employee_data.csv', 'w') as employeecsv:
    csvwrite = csv.DictWriter(employee_data, newcsvdict.keys())
    csvwrite.writeheader()
    csvwrite.writerows(newcsvdict)

