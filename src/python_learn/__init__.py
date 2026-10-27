# print("nice to meet you")
# print("你好啊",end="!")
# print("\n")
# input_string_var = input("输入一些数据：")
# print("输入的内容是：{}".format(input_string_var))

######################################################################
## 函数
######################################################################

## 字符串操作
name = "范晓龙"
print(f"我的姓名是{name}")
print(f"{name} is {len(name)} characters long")
name = "fanxiaolong"
print(f"{name} is {len(name)} characters long")

# None,0,空字符串，空列表，空字典，空元组都算是false
# 所有其他值都是True
if(bool(None)):
    print("是真的")
else:
    print("是假的")
bool(0)
bool("")
bool([])
bool({})
bool(())

# 用列表(list)存储序列
li = []
li.append(1)
li.append(2)
li.append("我是谁")
for ele in li:
    print("列表元素：{}".format(ele))

# 用pop从列表尾部删除
li.pop()
for ele in li:
    print("删除后还剩：{}".format(ele))

li.append("a")
li.append("b")
li.append("c")
# 取出最后一个元素
var = li[-1]
print("最后一个元素：{}".format(var))
# 可以用三个参数的组合来构建切割
# li[始:终:步伐]
tmpLi = li[1:3]
print(*tmpLi)
# 取到结尾
print(*li[2:])
# 从头开始取
print(*li[:3])
# 隔一个取一个
print("隔一个取一个")
print(*li[::2])
# 倒排列表，负数代表反向走，从右向左，从尾到头。正数代表正向走，从左往右，从头到尾。
print("倒排列表")
print(*li[::-1])
# 倒着隔一个取一个
print(*li[::-2])

# 用del删除任何一个元素
del li[2]
print("删除序号为2的元素")
print(*li)
# 用remove删除第一个匹配的元素
li.remove(2)
print("使用remove删除第一个匹配的元素")
print(*li)
# insert 在指定索引处插入一个新的元素
print("在指定索引处插入一个新的元素")
li.insert(1,2)
li.insert(2,"a")
print(*li)

# index 获取列表第一个匹配的值的索引
print("2的索引是：{}".format(li.index(2)))

# 合并列表，+ 会产生一个新的列表，不会影响原有的列表
li2 = ["aa","bb","cc"]
li3 = li + li2
print("合并后的列表")
print(*li3)

# extend 拼接列表
li.extend(li2)
print(*li)

#############################################################
## 学习一下元组 tup
#############################################################
# 元组类似列表，但是不允许修改
tup1 = (1,2,3)
print("元组的第一个元素:{}".format(tup1[0]))

# 如果元组的数量为1 ，必须在元素之后加一个逗号
# 其他元素数量的元组，包括空元组都不需要
type_name1 = type((1))
print("类型是：{}".format(type_name1))
type_name2 = type(2)
print("类型是：{}".format(type_name2))

#列表允许的操作元组大多都可以
len(tup1)
tup2 = tup1 + (4,5,6)
print("新的元组是：")
print(*tup2)

if(2 in tup2):
    print("tup2 元组包含2")
else:
    print("tup2 元组不包含2")

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
# for ele in kvalue:
#     print("key是{},value是{}".)