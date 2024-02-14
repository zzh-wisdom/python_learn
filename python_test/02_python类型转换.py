
# int() float() str()
int_v = 11
float_v = 11.11
str_int = "11"
str_float = "11.11"
tmp_f = float(str_float)
print(type(tmp_f), tmp_f)

# 浮点转整数，去掉小数部分
tmp_int = int(float_v)
print(type(tmp_int), tmp_int)

# 会转换失败
# tmp_int = int(str_float)

float = 13.12
int = 12
str = "str"
print(float, int, str)

