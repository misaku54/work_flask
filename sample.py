def func_args(*args,**kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)

def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)

# func_kwargs(key1=1, key2=2, key3=3)
func_args(key1=1, key2=2, key3=3)
func_args(1,2)
print(__name__)
print(__file__)