# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

a = str(input("Enter String : "))
b = a.find("not poor")

if b >= 0: 
    a = a.replace(a[b : b+8],"good")
    print(a)