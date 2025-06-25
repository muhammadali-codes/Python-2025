# Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n-1 + n
sum(n) = sum(n-1) + n
''' 

def sum(n):
    if (n==1):
        return 1
    elif(n==0):
        return 0
    return sum(n-1) + n 

num = int(input("Enter the number: "))
print(sum(num))
