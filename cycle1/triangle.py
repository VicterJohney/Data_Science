s1 = int(input("Enter side-1:"))
s2 = int(input("Enter side-2:"))
s3 = int(input("Enter side-3:"))
if s1 == s2 == s3:
    print("Triangle is Equilateral")
elif s1 == s2 or s2 == s3 or s3 == s1:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")