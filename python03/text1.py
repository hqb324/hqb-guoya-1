# class pareent():
#     money = "1000"
#     house = "1000"
#     car = "1000"
#
#     def shou_yi(self):
#         print("制刀")
#
# class child(pareent):
#     ai_hao = "滑铲"
#     pass
#
# c = child()
# print(c.money)
# print(c.house)
# print(c.car)
# c.shou_yi()
# print(c.ai_hao)
#
# class parent():
#     money = 1000
#     house = 1000
#     car = 1000
#
#     def __init__(self,a):
#         self.a = a
#     def shouyi(self):
#         print("制🔪")
#
# class child(parent):
#     ai_hao = "滑铲"
#     def __init__(self,*arge,**kwarge):
#         super().__init__(*arge,**kwarge)
#
# c = child(123)
# print(c.money)
# print(c.house)
# print(c.car)
# c.shouyi()
# print(c.ai_hao)
# print(c.a)


# a = "text1"
#
# def name():
#     print("我是day03")
#
# class text():
#     name = "我是text1"
# if __name__ == '__main__':
#
#     name()
#     print(text.name)

# b = "123"
# print(int(b))

# a = [1,2,3,4,5,6,7,8]
# print(tuple(a))
# print(set(a))
# b = (1,2,3,4,5,6,7)
# print(list(b))
# print(set(b))
# c = {1,2,3,4,5,6}
# print(list(c))
# print(tuple(c))

# a = open("hqb.txt","w")
# a.write("dskflewrnpo")
# a.close()

# b = open("hqb.txt","a")
# b.write("meishayong123456789")
# b.close()

# c = open("hqb.txt","w")
# c.write("good morning\n")
# c.close()
#
# d = open("hqb.txt","a")
# d.write("good afternoon\n")
# d.close()
#
# e = open("hqb.txt","a")
# e.write("good evening\n")
# e.write("good night\n")
# e.close()

# f = open("hqb.txt","r")
# print(f.read())
# f.close()
# h = open("hqb.txt","r")
# print(h.read())
# print(h.read(13))
# print(h.readline())
# print(h.readline())
# print(h.readlines())

# l = "qwer,asdf,zxcv"
# print(l.split(","))
#
# with open("hqb.txt","r") as b:
#     lines = b.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace("\n",""))
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}X{}={}".format(j,i,i*j),end = "\t")
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%dX%d=%d"%(j,i,i*j),end = "\t")
#     print()

# z = []
# z.append(10)
# z.extend({1,"8",451,5641})
# z.insert(0,2)
# print(z)

# a = [0,1,2,3,4,5,6,7,8,9]
# print(a.pop())
# print(a)
# print(a.pop(5))
# print(a)
# a.remove(1)
# print(a)
# a.remove(3)
# print(a)
# a.remove(7)
# print(a)
#
# a.sort()
# print(a)
# a.sort(reverse = True)
# print(a)

# b = {"name":"小福","age":"18","sex":"男"}
#
# b["name"] = "小胡"
# print(b)
# b["addr"] = "上海闵行"
# print(b)
#
# s = {}
# for key in b:
#     if key in ("addr"):
#         continue
#     s[key] = b[key]
# print(s)

# def div(a,b):
#     try:
#         return a / b
#     except:
#         return
# print(div(2,20))
# print(div(23,0))

# try:
#     f = open("fjj.txt","r")
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")

class CustomExcrption(Exception):
    def __init__(self,value="值不能为0"):
        self.value = value

    def __str__(self):
        return self.value

a = 998
try:
    if a == 0 :
        print("a = {}，触发异常".format(a))
        raise CustomExcrption
    print("a = {},未触发异常".format(a))
except CustomExcrption as qb:
    print(qb)