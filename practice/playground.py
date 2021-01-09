def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

add(1, 2, 3, 4, 5)



def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value))
callable(add=5, multiply=3)