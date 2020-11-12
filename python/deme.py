#a=input("请输入一个数字ａ：")
#b=input("请输入另一个数字b：")
#print(int(a)+int(b))


str="bugteacher.cn"
start,end,replace=input("请输入你要替换的起始位置："),\
                  input("请输入你要替换的终止位置:"),\
                  input("请输入你要替换的字符：")

r=str[:int(start)]+replace+str[int(end):]
print(r)