x = 10
y = 50
 
temp = x
x = y
y = temp
 
print("Value of x:", x)
print("Value of y:", y)


#******* Without temp ************


x = 10
y = 50
 
x, y = y, x
 
print("Value of x:", x)
print("Value of y:", y)
