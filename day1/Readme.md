Day 1 :- 
How to take input from user in Python ?
In  Python  input() is used to take data from a keyboard. 
input() method returns data in string type. we can type cast the data that is returned from input() as per our need.
For Example how to use the input() method refer the day1.py.
Python stops executing when it comes to the input() function, and continues when the user has given some input.


eval() :- The eval() method parses the expression passed to this method and runs python expression (code) within the program.
The syntax of eval() is: eval(expression, globals=None, locals=None)
eval() Parameters
The eval() function takes three parameters:
expression - the string parsed and evaluated as a Python expression
globals (optional) - a dictionary
locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.
x = 1
print(eval('x + 1'))
o/p= 2
x = eval(“10+20+30”)
print(x)
o/p= 60
eval() can evaluate the Input to list, tuple, set, etc based the provided Input.

Command line arguments:- Python Command line arguments are input parameters passed to the script when executing them. 
The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
One such variable is sys.argv which is a simple list structure. It’s main purpose are.
1.It is a list of command line arguments. 
2.len(sys.argv) provides the number of command line arguments. 
3.sys.argv[0] is the name of the current Python script. 
3.sys.argv[1] will be the first input from user.
4.sys.argv return string type only.
5.Space is Separator of Command line arguments.
6.If we need space in our command line argument we must enclose that part in double quotes.
How to pass arguments using command line - python script_name.py argument1 argument2.







