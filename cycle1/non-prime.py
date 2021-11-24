start = int(input("Enter the limit start:"))
end = int(input("Enter the limit end:"))
for i in range(start, end + 1):
    for j in range(2, i):
        if i % j == 0:
            print(i)
            break