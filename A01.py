def wrapper(func):
    def inner(*args,**kwargs):
        '''被装饰函数之前'''
        ret = func(*args,**kwargs)
        '''被装饰函数之后'''
        return ret
    return inner
@wrapper
def func(*args,**kwargs):
    print(args,kwargs)
    return 666
print(func())