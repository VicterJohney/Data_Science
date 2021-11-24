for i in range(0, 1001):
    temp = i
    sum = 0
    while temp > 0:
        d = temp % 10
        sum += d ** 3
        temp = temp // 10
    if i == sum:
        print(i)