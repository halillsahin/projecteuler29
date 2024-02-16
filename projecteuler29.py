a=[]
for i in range(2,101):
    for b in range(2,101):
        c=i**b
        if c in a :
            continue
        else:
            a.append(c)
print(len(a))          
