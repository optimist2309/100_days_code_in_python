"""
print() without any argument will work.
print():- It will insert newline(\n) in console.
Execute below example and see in the console.
"""
print("Hello")
print()  # After hello there will be new line before next print statement.
print("How are you ?")

"""
print(String) :-It will print the string in the console.
Execute below example and see in the console.
"""
print("Hai How are You.")
print("Harish\nTiwari")  # Escape characters also acceptable.
print("Harish " + "Tiwari")  # + will concat the string.
print("Harish " * 3)  # * repetition operator for string output will be Harish Harish Harish.

"""
The separator between the arguments to print() function in Python is space by default (softspace feature) ,
which can be modified and can be made to any character, integer or string as per our choice. 
The ‘sep’ parameter is used to achieve the same, it is found only in python 3.x or later
.It is also used for formatting the output strings.
"""
# By default example
print("hai", "hello", "How")

# code for disabling the softspace feature
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('Harish', 'Cerence', sep='@')

# another example
print(10, 20, 30, 40, sep=",")

"""
By default python’s print() function ends with a newline. 
A programmer with C/C++ background may wonder how to print without newline.
Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, 
i.e. the new line character. You can end a print statement with any character/string using this parameter.
"""
# By default example
print("Hai")  # After this newline character will be added automatically
# New print statement will start with  newline.
print("Hello")

# ends the output with a <space>
print("Welcome to", end=' ')
print("India")

# ends the output with '@'
print("Python", end='@')
print("Udemy")

# sep and end can be used together.
print(10, 20, 30, 40, 50, sep=",", end="######")
print(60, 70, 80, sep=",")
