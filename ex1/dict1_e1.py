# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
增加一项， gender  : 男
修改 2项 ， 学生编号 -》 002  学生名字 --》 甘露
删除gradeid项，并返回数据
'''
#字典
stu = {
    "studentNo": "001",
    "studentName": "陈超",
    "phone": "1212312",
    "address": "武汉",
    "bornDate": "2020/9/8",
    "gradeId": 3
}
for k,v in stu.items():#返回所有数据
    print("key == {} , value == {}".format(k,v))

for k in stu.keys():#返回可key值
    print("key == {}".format(k))
for v in stu.values():#返回value值
    print("value == {}".format(v))

logins={
    1:"张三",
    2:"李四",
    3:"王五",
    4:"赵柳",
    5:"田七"
}
for k,v in logins.items():
    print("key == {}, values == {}".format(k,v))
for id in logins.keys():
    print("key == {}".format(id))
for name in logins.values():
    print("value == {}".format(name))

# #增加一项， gender  : 男
# stu["gender"]="男"
# print(stu)
# #修改 2项 ， 学生编号 -》 002  学生名字 --》 甘露
# stu.update(
#     {
#         "studentNo":"002",
#         "studentName":"甘露"
#     }
# )
# print(stu)
# #删除gradeid项，并返回数据
# values=stu.pop("gradeId")
# # del stu["gradeId"]
#
# print("返回的数据",values)