score = input("请输入你的成绩：")
scores=int(score)
if scores>=90 and scores<100:
    print('A')
elif scores>=70 and scores<90:
    print("B")
elif scores>=60 and scores<70:
    print("C")
elif scores>=0 and scores<60:
    print("D")
else:
    print("你输入的是无效的成绩。")