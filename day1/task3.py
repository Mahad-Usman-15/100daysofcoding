# Reverse a given string without using built-in reverse functions (use a loop).

example_string="Mahad Usman"
expected_output = "namuU dahaM"

for i in range(-1,-len(example_string)-1,-1):
    print(example_string[i],end="")