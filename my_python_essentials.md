# My Python Essentials
The following python snippets are used frequently

## Coding
* ### String formatting
```py
age = 45
name = "abhijit"
# print("Hello {0}, your age is {1}".format(name, age))
print(f"Hello {name}, your age is {age}")     # since python v3.6
```
* ### Function definition
```py
def print_a_message():
    print("abhijit")

my_function = print_a_message 	# assigning a function with another function

my_function()		# Run this function
```

* ### Function defined within another function 
	**Correct:**
```py
def my_function():
	my_other_function()

def my_other_function():
	print("Hello world")

# this works fine, because 'my_other_function' is defined yet.
my_function()
```
	
  **Wrong:**
```py
def my_function():
	my_other_function()

# this gives error, because 'my_other_function' is not defined yet.
my_function()

def my_other_function():
	print("Hello world")
```
* ### Function assignment
```py
def func_a():
	print("Function a")

func_a()
"""
  NOTE: b is a variable & it has been assigned with a function
"""
b = func_a
b()
``` 
* #### Convert a list of `string` into `float` or `int`
```py
>>> x = ["545.0", "545.6", "999.2"]
>>> map(float, x)
[545.0, 545.60000000000002, 999.20000000000005]
>>>
```
* #### dictionary
```py
>>> dict(name="abhijit", age=26)
{'name': 'abhijit', 'age': 26}
```	
* #### binary representaion
```py
>>> print("{0:b}".format(45))
101101
```
## Code Optimization
* #### `Map`
```py
items = [1, 2, 3, 4, 5]

# M-1
squared = []
for i in items:
    squared.append(i**2)
print(squared)

# M-2
squared2 = list(map(lambda x: x**2, items))
print(squared2)
```
[More](./coding/map.py)
