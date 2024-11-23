def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('--end--')
    return wrapper


def test(b):
    print(b)
    print('Hello Decorator')

a = deco(test)
a("dd")