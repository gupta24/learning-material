"""two pointer technique"""
# def two_pointer(A, X):
#     i = 0
#     j = len(A)-1
#     while i<j:
#         if A[i]+A[j] == X:
#             return True
#         elif A[i]+A[j] < X:
#             i += 1
#         else:
#             j -= 1
#     return False


# # input data
# A = [10, 20, 35, 50, 75, 80]
# X = 20
# print(two_pointer(A, X))


"""
merge interval problem

request : {[1,3][2,6][8,10][15,18]} / {[1,4][7,9][3,6][8,10]} / [(1,9)(2,5)(19,20)(10,11)(12,20)(0,3)(0,1)(0,2)]
response : 
-  [1,3] and [2,6] are continues so merge and get [1,6]
-  [8,10] and [15,18] and any other list number are not continues after list number 10 so not merge and get only [8,10]
-  [15,18] and any other list number are not continues after or before imediately list number 18 so not merge with [15,18] and get only [15,18]

final result is : {[1,6][8,10][15,18]} / {[1,6][7,10]}

"""

# brute force approach..
# first arrange the list and then merge
"""
1,4 - 3,6 - 7,9 - 8,10
1,6 - 7,10

complexity : O(n^2)
"""

# inp = [(1,9),(2,5),(19,20),(10,11),(12,20),(0,3),(0,1),(0,2)]
# #print(sorted(inp))
# merge_inp = []
# index = 0
# for i in range(len(inp)-1):
#     min_item = inp[i]
#     index = i
#     for j in range(i+1, len(inp)):
#         if  min_item[0] > inp[j][0]:
#             min_item = inp[j]
#             index = j
#         elif min_item[0] == inp[j][0]:
#             if min_item[1] > inp[j][1]:
#                 min_item = inp[j]
#                 index = j
            
#     inp[index] = inp[i]
#     inp[i] = min_item 

# print(inp)
# item1, item2 = 0, 0
# for item in inp: 
#     if len(merge_inp) == 0 or merge_inp[-1][1] < item[0]:
#         merge_inp.append(item)    
#     elif merge_inp[-1][1] > item[0] and merge_inp[-1][1] < item[1]:
#         item1 = merge_inp[-1][0]
#         item2 = item[1]
#         merge_inp[-1] = (item1, item2)

    
#print("merger item :", merge_inp)



# best approach..
"""
 take time : O(nlogn) + O(n) = O(nlogn)
"""
# inp = [(1,9),(2,5),(19,20),(10,11),(12,20),(0,3),(0,1),(0,2)]
# inp = sorted(inp)
# print(inp)
# merge_inp = []
# item1, item2 = 0, 0
# for item in inp:    
#     if len(merge_inp) == 0 or merge_inp[-1][1] < item[0]:
#         merge_inp.append(item)    
#     elif merge_inp[-1][1] > item[0] and merge_inp[-1][1] < item[1]:
#         item1 = merge_inp[-1][0]
#         item2 = item[1]
#         merge_inp[-1] = (item1, item2)

    
# print("merger item :", merge_inp)


# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
# import shutil
# filepath = "/home/rahul/Downloads/ApiScreenShot1.png"
# readfile = "/home/rahul/Pictures/ApiScreenShot1.png"
# r = open(readfile, 'rb')
# r.raw.decode_content = True

# with open(filepath,'wb') as f:
#     shutil.copyfileobj(r.raw, f)
            
# print('Image sucessfully Downloaded: ',filepath)

"""
from datetime import datetime, timedelta
import requests

current_data = datetime.now().strftime("%m/%d/%Y")
before_date =  (datetime.now() - timedelta(days=15)).strftime('%m/%d/%Y')
url = "https://ee.iva-api.com/api/Entertainment/Search/?Take=50&Providers=FandangoMovies&DeliveryMethods=Ticket&ProgramTypes=Movie&ReleaseTypes=Theatrical_Wide_Release&ReleaseCountries=US&OriginalReleaseDateRange_Start={}&OriginalReleaseDateRange_End={}&Includes=ExternalIds&subscription-Key=8a7c244ebdd74265afb0b2075ce1d40f".format(before_date, current_data)
res = requests.get(url, headers={"content-type": "application/json"})
    
if res.status_code == 200:
    json_data = res.json()
    if len(json_data['Hits']) > 0:
        theatrical_movie_list = json_data['Hits']
        print(len(theatrical_movie_list))
"""


# Use for create the blurhash of image
"""
import requests
import blurhash
from pymongo import MongoClient

#MONGO_DB_URL = "mongodb://fmtest:fmADC12#Test@localhost:27020/test?authSource=admin"
#mongo_client = MongoClient(MONGO_DB_URL)

response = requests.get("https://cdn.folksmedia.com/TMDB/image_repo/shows/tt0063884/poster.jpg", stream=True)
if response.status_code == 200:
    response.raw.decode_content = True
    #with open('greenland_03a.png', 'wb') as out_file:
        #shutil.copyfileobj(response.raw, out_file)
    hash = blurhash.encode(response.raw, x_components=4, y_components=3)
    print(hash)
    #print(blurhash.decode(hash, 128, 128).astype('uint8'))
"""

# convert jpg to webp formate
"""
import requests
import os
from PIL import Image
from io import BytesIO

path = os.getcwd()
def convert_jpg_to_webp(raw_data):
    im = Image.open(raw_data)
    fp = BytesIO()
    im.convert("RGB").save(fp, "WEBP")
    fp.seek(0)
    return fp

r = requests.get("https://image.tmdb.org/t/p/w200/78lPtwv72eTNqFW9COBYI0dWDJa.jpg", stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    fp = convert_jpg_to_webp(raw_data=r.raw)
    with open(path+"/abc.webp", 'wb') as wp:
        wp.write(fp)
    img = Image.open(r.raw)
    with open(path+"/abc.jpg", 'wb') as jp:
        jp.write(img)
else:
    print("give an error....")

"""


# get user geo location with ip addres
"""
import requests
## Get the ip of the client that is making the request
client_ip = "157.34.29.2"
#"171.76.83.62"
## get the location details from the ip-api (geoLocaton API)
response = requests.get(f"http://ip-api.com/json/{client_ip}").json()
print(response)
"""

"""
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
print(float(data["loc"].split(",")[0]))
"""