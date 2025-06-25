# Write a program to find the sum of first n natural numbers using while loop. 

n = int(input("Enter a number: "))
i = 0
sum = 0
while(i<=n):
    if(n == 0):
        print(f"Hence you entered the number 0 so it's sum is = {n}")
        break
    sum += i 
    i += 1


print(sum)