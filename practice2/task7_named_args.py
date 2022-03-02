def power_of_2(object = [1, 2, 3], power = 2):
    if hasattr(object, '__iter__'):
        resulto = []
        for obj in object:
            resulto.append(pow(obj, power))
        return resulto
    return pow(2, power)

print(power_of_2(power=3))
print(power_of_2([1, 2, 3]))