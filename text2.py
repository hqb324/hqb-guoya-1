# sc = 99
# if (sc>=0 and sc<60):
#     print("不及格")
# if (sc>=60 and sc<=70):
#     print("及格")
# if (sc>70 and sc<=80):
#     print("良好")
# if (sc>80 and sc<=100):
#     print("优秀")
#
# sc = 19
# if (sc >= 0 and sc<60):
#     print("不及格")
# elif (sc >= 60 and sc<=70):
#     print("及格")
# elif (sc >= 71 and sc<=80):
#     print("良好")
# else:
#     print("优秀")
#
# sc = 77
# if (sc<0):
#     print("请输入正确的成绩")
# elif (sc>=0 and sc<60):
#     print("不及格")
# elif (sc>=60 and sc<=70):
#     print("及格")
# elif (sc>70 and sc<=80):
#     print("良好")
# elif (sc>80 and sc<=100):
#     print("优秀")
# else:
#     print("请输入正确的成绩")
#
# sc_1 = [10,20,30,40,50,60,70,80,90,100]
# for sc in sc_1:
#     if (sc < 0):
#             print("请输入正确的成绩")
#     elif (sc >= 0 and sc < 60):
#             print("不及格")
#     elif (sc >= 60 and sc <= 70):
#             print("及格")
#     elif (sc > 70 and sc <= 80):
#             print("良好")
#     elif (sc > 80 and sc <= 100):
#             print("优秀")
#     else:
#             print("请输入正确的成绩")
#
# s = 1
# for i in range(10,0,-1):
#     s *= i
# print(s)
#
# s = 0
# for i in range(100,0,-1):
#     s += i
# print(s)

# flag = True
# a = 77
# while flag :
#     b = int(input("请输入数字"))
#     if b > a :
#         print("大了")
#     elif b < a :
#         print("小了")
#     else:
#         print("对了")
#         flag = False

flag = True
a = 867
while flag:
    b=int(input("请输入数字"))
    if b>a:
        print("大了")
    elif b<a:
        print("小了")
    else:
        print("对了")
        flag = False

a = "小明,小红,小张"
print(a.split(","))