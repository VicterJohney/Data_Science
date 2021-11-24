limit = int(input("Enter the limit:"))
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(1, limit - 1):
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print(n3)