l = []
for i in range(2000,3201):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))
num = len(l)
print(','.join(l))
for j in range(0,num - 1):
    print(l[j],end=',')
    j += 1
    if (j % 10 == 0):
        print("\n")
print(*(i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0),sep=',')


