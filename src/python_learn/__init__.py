# print("nice to meet you")
# print("你好啊",end="!")
# print("\n")
# input_string_var = input("输入一些数据：")
# print("输入的内容是：{}".format(input_string_var))

######################################################################
## 函数
######################################################################

#用def定义新函数
def add(x,y):
    print("x is {} and y is {}".format(x,y))
    return x + y
#调用函数
result1 = add(5,7)
print("结果是{}".format(result1))
#也可以用关键字参数来调用函数
result2 = add(y=9,x=20)
print("结果是{}".format(result2))

#定义一个可变参数函数
def varargs(*args):
    return args

array = varargs(1,2,3)
for ele in array:
    print("参数是:{}".format(ele))

#定义一个关键字可变参数函数
def keyword_args(**kwargs):
    return kwargs

kvalue = keyword_args(big="foot",loch="ness")
