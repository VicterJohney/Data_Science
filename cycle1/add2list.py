lt1 = [5, 10, 15, 20, 25, 30]
lt2 = [2, 4, 6, 8, 10, 12]
print("List1: " + str(lt1))
print("List2: " + str(lt2))
res_lt = []
for x in range(0, len(lt1)):
    res_lt.append(lt1[x] + lt2[x])
print("List1 + List2 is: " + str(res_lt))
