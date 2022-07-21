# Write a Python function that takes a list of words and returns the length of the longest one.


a = str(input("Enter String : "))
b = list(a.split())
print(b)
c = 0
for i in b:
    if len(i) > c:
        c = len(i)
        d = i
print("Longest word is : ",d,"and Length of the longest word is : ",c)