
               
list1 =[2,7,7,11,15,9] 

target = 14
#new_list = list(map(lambda x : x*2, list1))


new_dict = {}
for i in list1:
    if i not in new_dict.keys():
        new_dict[i] = 1
    else:
        new_dict[i] += 1


print(new_dict)
res = []
index = 0
new_target = target
for i in list1:
    diff = target - i
    if diff == 0:
        res.append(index)
        target = target - 1
    
    if diff in new_dict.keys():
        new_dict[i] -= 1

    if diff in new_dict.keys() and new_dict[diff] != 0:
        target = target - i
        res.append(index)

    if target == 0:
        break
    index += 1

print(res)



''' find common number of element from two string
s1 --> aabcc
s2 --> adcaa

sol -: 
    s1 - {a: 2, b: 1, c: 2}
    s2 - {a: 3, c: 1, d: 1}

    check s2 string value available in s1 string and reduce the count from s1 string
    and make the total count wheneven count is reduce from s1 string;
    so return the result as the total count.
''' 