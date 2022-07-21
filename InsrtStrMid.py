# Write a Python function to insert a string in the middle of a string.


a = str(input("Enter String : "))
b = str(input("Enter String : "))
c = int(len(a)/2)
d = a[:c] + b + a[c:]
print(d)