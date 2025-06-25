# . Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 

def pattern(n):
    if(n==0):
        return print("Hence you entered zero so no stars are printed")
    print("*" * n)
    pattern(n-1)

p = int(input("Enter the Pattern: "))

pattern(p)