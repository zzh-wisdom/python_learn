
# 获取字面量的类型
print(type(666))
print(type(666.66))
print(type("666.66"))

# 变量存储type返回的类型
int_type = type(666)
float_type = type(666.66)
str_type = type("666.66")
print(int_type)
print(float_type)
print(str_type)

# type查看变量中存储的数据类型
int_v = 666
float_v = 666.66
str_v = "666.66"
print(type(int_v))
print(type(float_v))
print(type(str_v))

print("type是查看变量本身存储的数据类型:")
tmp_v = 666
print(type(tmp_v))
tmp_v = 666.66
print(type(tmp_v))
tmp_v = "666.66"
print(type(tmp_v))
