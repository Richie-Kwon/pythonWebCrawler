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







