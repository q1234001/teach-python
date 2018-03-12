#集合類型與迴圈
name = "Shawn"
lista = ['a1', 'b1', 'c1']
seta = ('a1', 'b1', 'c1')
dicta = {'name': name, 'tax':'0919191911', 'age': 23}


#迴圈範例
for x in lista:
    print(x)

x = 0

while x < len(seta):
    print(seta[0])
    x+=1

    
for x in range(10):
    print(x)

#字典取值

for x in dicta:
    print(x,":",dicta[x])
