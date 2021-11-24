def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
GCD = gcd(n1, n2)
if GCD == 1:
    print("Numbers are co-prime")
else:
    print("Not co-prime")