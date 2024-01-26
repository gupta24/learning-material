a = [0,1,1,0,1,2,1,2,0,0,1]

i,j=0,1

while j<len(a):
    if a[i]==a[j]:
        j += 1
        i += 1
    elif a[i] > a[j]:
        a[i], a[j] = a[j], a[i]
        i += 1
    j += 1
print(a[::-1])

