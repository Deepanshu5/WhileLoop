y = 11
x = y // 2
while x > 1:
    if y % x == 0:
        print (y, 'is not a prime number.')
    x -= 1
else:
    print (y, 'is a prime number!')
