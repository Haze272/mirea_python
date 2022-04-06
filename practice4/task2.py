import math


class MyClass:
    a = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sumsqrt(self):
        return math.sqrt(self.x**2 + self.y**2)

    def howdyho(self):
        return 'Hello World!'

obj = MyClass(1, 2)
print('Переменные класса %s:' % obj.__class__.__name__)
print(vars(obj))

while True:
    print('Введите метод для вызова. Для выхода нажмите 0')
    s = input()
    if s == '0':
        break
    print(getattr(obj, s)())