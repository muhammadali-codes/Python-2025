# Write a program to find whether a given username contains less than 10 
# characters or not. 

username = input("Enter your username:")
if(len(username)<10):
    print("The length of username is less than 10")

else:
    print("The length of username is greater than 10")