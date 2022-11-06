def validator1(fn1,mes):
    def exam(fn2):
        def inner(*args,**kwargs):
            if fn1 < fn2(*args,**kwargs):
                print(fn2(*args,**kwargs))
            else:
                print(mes)
                print(fn2(*args,**kwargs))
        return inner
    return exam

def greater_than(x):
    return x
   


def validator2(fn1,mes):
    def exam(fn2):
        def inner(*args,**kwargs):
            if fn1.__contains__(fn2(*args,**kwargs)):
                print(fn2(*args,**kwargs))

            else:
                print(mes)
                print(fn2(*args,**kwargs))
        return inner
    return exam
def arg_in(x):
    return x



def validator3(fn1,mes):
    def exam(fn2):
        def inner(*args,**kwargs):
            if fn1 > fn2(*args,**kwargs):
                print(fn2(*args,**kwargs))
            else:
                print(mes)
                print(fn2(*args,**kwargs))
        return inner
    return exam
def less_than(x):
    return x



def validator4(fn1,mes):
    def exam(fn2):
        def inner(*args,**kwargs):
            if str(fn2(*args,**kwargs)).startswith(fn1):
                print(fn2(*args,**kwargs))
            else:
                print(mes)
                print(fn2(*args,**kwargs))
        return inner
    return exam
def starts_with(x):
    return x



@validator1(greater_than(0),'error')
def example(arg):
    return arg
example(-1)