a = str(input("Enter String : "))
b = 0
for i in a:
    if i.isalnum():
        b += 1

print(b)