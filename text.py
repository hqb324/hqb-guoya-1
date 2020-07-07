a = (1,2,3)
x,y,z = a
print(x)
print(y)
print(z)

a = [1,2,3]
x,y,z = a
print(x)
print(y)
print(z)

a = 1,2,3,4,5,6,7
x,y,*z = a
print(x)
print(y)
print(z)


a = {"name":'小明',"age":18}
print('a =',a)

a = {'小明',18}
x,y = a
print(x)
print(y)

a = '小明'
x,y = a
print(x)
print(y)

a = "123"
b = "456"

print(a+b)
print(a)
print(b)

a = "12345678910"
print(a[0])
print(a[1:])
print(a[:3])
print(a[3:8])
print(a[1:-1])
print(a[::2])
print(a[::-1])


h = 10
q = 20

#h = h + q
#print(h)
h //= q
print(h)

z = "789456123"
print(z[::-1])
print(7 in z)


z = "5432182"
print(z % 20)
print(z % 200)
print(z // 20)
