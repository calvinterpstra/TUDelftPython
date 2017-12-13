# -*- coding: utf-8 -*-
"""
Hello3mE.py  -- the canonical Greeting Program, to experiment with the 
                execution flow 

@author : Bart Gerritsen
"""

# EXPERIMENT: comment the different parts
# and variables (like the greetings below)
# and check what the program tells you

# EXPERIMENT: what happens if you comment the 
# variable definition below?
greetings  = 'Hello 3mE??'

# this will be printed unless we
# rewire the start to main()
print('@level(0):', greetings)

def my_func():
    print('@my_func():', greetings)

def main():
    # EXPERIMENT: comment the different parts
    # and variables (like the cgreetings below) 
    # and check what the program tells you 
    
    #EXPERIMENT: increase the indentation level
    # with 'Edit->indent' (or: Tab) and see 
    # what effects that has 
    greetings  = 'Hello 3mE!'
    print('@main():', greetings)
    my_func()

# EXPERIMENT: comment the different parts
# and variables (like the call to main() ) 
# and check what the program tells you   
main()

# EXPERIMENT: comment the different parts
# and variables (like the if and the calls 
# below) and check what the program tells you 
if __name__ == "__main__": 
    my_func()
    # main()
