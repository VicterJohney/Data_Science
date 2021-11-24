# a = [35, 10, 31, 11, 26]
n = int(input("Enter the cumber of elements you want to sort: "))
a = []
print("Enter the elements: ")
for i in range(n):
    a.append(int(input()))
print("Before sorting - ")
for i in a:
    print(i, end=" ")
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[j] < a[i]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print("\nAfter sorting - ")
for i in a:
    print(i, end=" ")