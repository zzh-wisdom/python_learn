
name = "zhangsan"
sex = "男"
print("人员信息：" + name + "，性别：" + sex)

# python不能隐形类型转换
tel = 6668888
# print("电话号码是：" + tel)

# 字符串格式化
year_num = 2023
month = 9
float_pi = 3.14
date_str = "现在是：%s年%s月" % (year_num, month)
pi_str = "圆周率是：%s" % float_pi
print(date_str)
print(pi_str)
print("整数打印前导0测试，9打印：%02d" % month)

# 字符串快速格式化
name = "张三"
age = 18
# 精度有限，并不能把所有的小数保存
pi = 03.144444444444444464756546435467656544000
f_6 = 6.00
print(f"{name}今年年龄是{age}")
# 对浮点数有效的位数进行输出
print(f"pi是{pi}, 6.0:{f_6}")

print(f"1+1的结果为{1+1}")
print("1+1的结果为%d" % (1 + 1))

