# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def reverse_args(**kwargs):
    result = {}
    
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

result = reverse_args(a=1.587, b='hello', c=(1, 2, 3), d=True, e=[1, 2, 3])
print(result)