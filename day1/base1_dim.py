#數值與字串類型

inta = 1
stra = '1'
intb = 2
strb = '2'
name = "Shawn"

print("inta = 1\nstra = '1'\nintb = 2\nstrb = '2'")


ex1 = "數值相加:inta + intb = {ans}"
print(ex1.format(ans = inta + intb))


print("字串相加:stra + strb = "+ stra + strb)


print("數值跟字串相加(字串轉型):inta + int(stra) =", str(inta +int(stra)))

print('name = "Shawn"')
print("print(inta+ int(name)) 是不行的")

