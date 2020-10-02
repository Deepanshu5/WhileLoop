n=int(input())   # taking input from user
i=2              # initialising i with 2
while i<n:
    if n%i==0:
        break     # if condition true then break
    i+=1    
else:              # else print it's prime
    print("It's a prime number")
    
