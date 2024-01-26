"""
basic concept
"""
# abc = "111011110"

# max_size = -1
# count = 0
# for i in abc:
#     if i != '1':
#         if max_size < count:
#             max_size = count
#             count = 0
#             continue
#     count +=1

# print(max_size)

"""
regex concept
"""
# import re

# inp = input("give input : ")

# "958 977 3999"
# obj = re.match(r'^[\d+]{3}(\s|\-?[\d+]){4}(\s|\-?[\d+]){5}$', inp, re.M|re.I)
# #obj = re.match(r'^[a-z0-9](\.|\_|\-?[a-z0-9]){2,}@g(oogle)?mail\.com$', inp, re.M|re.I)

# if obj:
#     print(obj.group())
# else:
#     print("no Match!")


# import re

# inp = input("give input : ")

# obj = re.search(r'dogs', inp, re.M|re.I)
# #obj = re.match(r'^[a-z0-9](\.|\_|\-?[a-z0-9]){2,}@g(oogle)?mail\.com$', inp, re.M|re.I)
# if obj:
#     print(obj.group())
# else:
#     print("no Match!")




"""
N=3, arr=[1, 2, 4, 3, 9]
total no  count of even sum subset:
ex: {1,3}, {1,9}, {2}, {4}, {2, 4}, {3,9} = 6
res = 3 
"""

# 1%2 == 0 ; sum += 1; count += 1

# 7-1 = 7-2, 6-2 = 7-4, 6-4, 4-4

# 19-9 = 10 , 10, 9, count = 1
# 19-3 = 17, 10-3 = 7, 19-12 = 7

# 6
# [1, 2, 4, 3, 9]
# [0, 1, 3, 7, 10]

#  i  j  k    
# [1, 2, 4, 3, 9]
# [1, 3, 7, 10, 19]

# [1, 2, 2, 3, 4, 1]
# [0, 1, 1, 0, 1, 0]


"""
arr=[15, -2, 2, -8, 1, 7, 10, 23]
find longest sub array with element summing up to 0
{-2, 2, -8, 1, 7} = 5
res=5
"""

# def maxLeng(li):

#     dict_map = {}
#     max_len = 0
#     max_sum = 0
#     inc = -1
#     for i in li:
#         max_sum = max_sum + i
#         if max_sum in dict_map.keys():
#             max_len = li.index(i)
#             inc = max_len
#         else:
#             inc += 1
#             dict_map[max_sum] = inc
        
#     return max_len


# inp_list = list(map(int, input("give the list of elements : ").split(' ')))
# print("result is : ", maxLeng(inp_list))


