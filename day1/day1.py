"""
Example_1  :- Take the two numbers input from user and perform addition and multiplication.
"""
First_Number = int(input("Enter the first number :- "))  # int() is used for typecasting the string to int type.
Second_Number = int(input("Enter the second number :- "))
print("Addition of both number is :-  ", First_Number + Second_Number)
print("Multiplication of both number is :-  ", First_Number * Second_Number)

"""
Example_2  :- Take the employee data and validate it.
"""
emp_id = int(input("Enter Employee ID :- "))
emp_name = input("Enter Employee Name :- ")
emp_salary = float(input("Enter Employee Salary :- "))
emp_city = input("Enter Employee City :- ")
emp_married_status = eval(
    input("Married [True or False]?"))  # If boolean type required from keyboard use eval function.
# bool() function will always return true for any string and false for empty string.

print("Verify the information")
print("Employee Name is ", emp_name)
print("Employee id is ", emp_id)
print("Employee city is ", emp_city)
print("Employee salary is ", emp_salary)
print("Employee is Married", emp_married_status)
