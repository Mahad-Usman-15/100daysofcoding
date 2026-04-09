# simple functions
def double(x):
    return x*2

print(double(5))    

# lambda functions
# function_name=lambda parameter/s: expression
double = lambda x:x*2
print(double(5))


greet=lambda name:f"Hello, {name}!"
print(greet("Mahad Usman"))