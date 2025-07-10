# Tim Lucas
# Lab 15-1
# 2025-07-10

import employee

'''
    CREATING EMPLOYEES
    Do not edit this section of code. Your classes should work with these tests.
    If these tests do not work, you must modify/fix the classes you developed.
'''

employee1 = employee.Employee('George Jetson', 35.50, 22.75)
employee2 = employee.Employee('Jane Jetson', 40, 30.00)
sales1 = employee.Salesperson('Leroy Jetson', 25, 15.00, 2550.50, .03)
sales2 = employee.Salesperson('Judy Jetson', 30, 22.50, 4750.00, .05)

'''
    POLYMORPHISM
    In the area below, create a single list to hold all of the people created 
    above. Use a single loop to to print the data from each object and the
    results of the calc_pay method for each of them.
'''

employee_list = [employee1, employee2, sales1, sales2]

for employee in employee_list:
    print(employee)
    print(f"Total pay for {employee.name} is ${employee.calc_pay():.2f}")
    print("-" * 8)