# # # # a = "小明,小红,小张"
# # # # print(a.split(","))
# # # #
# # # # a = 86
# # # # while True:
# # # #     b=int(input("请输入数字"))
# # # #     if b>a:
# # # #         print("大了")
# # # #     elif b<a:
# # # #         print("小了")
# # # #     else:
# # # #         print("对了")
# # # #         break
# # #
# # # # for i in range(1,100,1):
# # # #     if (i % 3 != 0):
# # # #         continue
# # # #     print(i)
# # #
# # # # for i in range(100,0,-1):
# # # #     if(i % 3 != 0):
# # # #         continue
# # # #     print(i)
# # #
# # # def jisuan(a,b):
# # #     print(a // b )
# # #     print(a % b)
# # # jisuan(37,20)
# # #
# # # def js(a , b):
# # #     quyu = a % b
# # #     print(quyu)
# # #     quzheng = a // b
# # #     print(quzheng)
# # # js(78 ,24)
# # #
# # # def js(a , b):
# # #     print("商：",a // b ,"，余数：", a % b)
# # # js(45,23)
# # #
# # def js(a , b):
# #     if (b == 0):
# #         return None
# #     else:
# #         return (a // b , a % b)
# #
# # hq = js (998,13)
# # hq = js (998,0)
# #
# # if hq is None:
# #     print("输入参数错误")
# # else:
# #     print("商为：",hq[0],"，余数为：",hq[1])
# #
# # def sm(a , b = 2):
# #     return a + b
# # print(sm(7))
# #
# # def c(name , *args ):
# #     print(name)
# #     s = 1
# #     for i in args:
# #         s *= i
# #     return s
# # print(c(1,2,3,4,5,6,7,8,9))
# # print(c(name="王大锤"))
# # a = 10
# # print(a)
# #
# # def aaa():
# #     global a
# #     a = 12
# #
# # aaa()
# # print(a)
# #
# #
# # class calc():
# #     a=None
# #     b=None
# #     res=None
# #     def input(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def sum(self):
# #         self.res = self.a + self.b
# #     def div(self):
# #         self.res = self.a / self.b
# #     def get_result(self):
# #         print(self.res)
# #
# # c = calc()
# # c.input(34,23)
# # c.sum()
# # c.get_result()
# # c.div()
# # c.get_result()
# #
# # g=10
# # print(g)
# #
# # def var():
# #     global g
# #     g=20
# # var()
# # print(g)
#
# # class qwe():
# #     res = None
# #     def __init__(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def sum(self):
# #         self.res = self.a + self.b
# #     def div(self):
# #         self.res = self.a / self.b
# #     def get_result(self):
# #         print(self.res)
# #
# # c = qwe(57457,456)
# # c.sum()
# # c.get_result()
# # c.div()
# # c.get_result()
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print(j,"X",i,"=",i*j,end="\t")
# #     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",j*i,end="\t")
#     print()
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print(j,"X",i,"=",j*i,end="\t")
#     print()


# for i in range(length-1,0,-1):
#     for j in range(i):
#         if(l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="\t")
#     print()


# l = [717,23,45,66,7,343,746,87,32,435,78,234,658,5647,556,55,854]
#
# length = len(l)
# c=len(l)
# print(c)
#
# for i in range(0,c-1):
#     for j in range(0,c-1-i):
#         if(l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)
#
# def lever(a , b):
#     print(a // b)
#     print(a % b)
# lever(33 , 8)
# lever(20 , 8)
# def shang_yu(a,b):
#     if(b==0):
#         return  None
#     else:
#         return  (a // b,a % b)
#
# res = shang_yu(20,3)
# res = shang_yu(25,b=3)
#
# if res is None:
#     print("参数错误")
# else:
#     print("商为：",res[0],"余数为：",res[1])
#
# def sm(a,b=2):
#     return (a+b)
# print(sm(3))
#
# a,*b = (1,2,3,4)
# print(b)
#
# def sum1(name,*args,**kwargs):
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum1(1,2,3,4,6,1,511,1,1851,55))
# print(1,2,3,4,6,1,511,1,1851,55)
# print(sum1(name="薛潇"))

from python03 import text1
from python03.text1 import a as b

a = "text"

def name():
    print("我是day2")

class text():
    name = "我是text"


print(b)

