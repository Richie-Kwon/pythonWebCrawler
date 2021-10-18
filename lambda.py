def function_multi(x):
    y1= x * 100
    y2= x * 100
    y3= x * 100
    return y1, y2, y3
    # return [y1, y2, y3] >> return values in list
    

val1, val2, val3 = function_multi(100)
print (val1, val2, val3)

# args >> tuple type
def args (*args):
    print (args)
    # print index and value
    for i, v in enumerate(args):
        print(i,v)

# kwargs >> dictionary type
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1 = "Kim", name2 = "Rhee")

# nested function
def nested_func(num):
    def in_func(num):
        print(">>>", num)
    print("how to work in_func")
    in_func(num + 10000)
# Hint
def function_multi(x : int) -> list:
    y1= x * 100
    y2= x * 100
    y3= x * 100
    return y1, y2, y3

# lambda
mul = lambda x: x * 10
print(mul(10))









