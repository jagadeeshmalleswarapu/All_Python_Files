
a = input("Enter a name: ")
d={}

for i in a.lower():
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1

# print(d)
for i in d:
    print(i,":",d[i])