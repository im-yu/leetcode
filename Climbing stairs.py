f1,f2,f3=1,2,3
for i in range(3,10):
    f1 = f2
    f2 = f3
    f3 = f1+f2
print(f3)