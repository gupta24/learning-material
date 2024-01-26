a = "abcdefghi"

"""
a   e   i   m
 b d f h j l
  c   g   k
"""

lev = 0
flag = 0
index = 0


for i in range(0, 3):
    index = i
    lev = i
    if i == 0:
        while lev <= len(a):
            print(lev*" "+a[index], end='')
            index += 4
            lev += 4
    else:
        print("\n")
        while lev <= len(a):
            print(lev*" "+a[index], end='')
            index += 1 + i
            lev += 1 + i
    
print("\n")