'''
    Problem Statement
    ================
    compute `y = 5*x + 2`

    This is about Lambda function which is used in 2 conditions:
    1. Don't want to create a separate function
    2. Used only once.

    NOTE: It is always recommended to create a function and use in the entire codebase/single file, when it is being used many times.
    
    Syntax
    ======
    lambda <input_var> : <function using input_var>

'''
# M-1
def compute_x(y):
    return 5*y + 2

print(compute_x(3))

# M-2
y = lambda x : 5*x+2
print(y(3))

