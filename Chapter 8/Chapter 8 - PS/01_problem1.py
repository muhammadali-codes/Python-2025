# Write a program using functions to find greatest of three numbers.

def greatest_num(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1

    elif(n2>n1 and n2>n3):
        return n2

    elif(n3>n1 and n3>n2):
        return n3
    
    else:
        print("All numbers are equal:")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

print(greatest_num(n1, n2, n3))