import json
from pprint import pprint 

jsondata = open("路外停車資訊.json", 'r', encoding='UTF-8')

data = jsondata.read()

print(type(data))
print(data[0])

data = json.loads(data)

print(type(data))

print(data.keys())


#列出第一筆資料
print(data['parkingLots'][0].keys())
for x in data['parkingLots'][0].keys():
    print (x)
    
"""多行注解

下列程式碼是 列出多全部
pprint(data)





"""

    

