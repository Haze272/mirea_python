import sys


def naive_print(*object, sep=' ', end='\n', file=sys.stdout):
    if hasattr(object, '__iter__'):
        for obj in object:
            file.write(str(obj) + sep)
        file.write(end)
        return


    if type(object) == int or type(object) == float:
        file.write(str(object) + end)
    elif type(object) == str:
        file.write(object + end)

naive_print(3)
naive_print("sa")
naive_print("Lorem ipsum")
naive_print([0, 1, 7])
naive_print(1, 2, 'abc')
