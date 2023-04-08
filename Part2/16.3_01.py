'''Напишите функцию concat(), принимающую переменное количество аргументов и
объединяющую их в одну строку через разделитель (sep).
Если разделитель не задан, им служит пробел.

Примечание 1. Обратите внимание, что функция concat() должна принимать не список,
а именно переменное количество аргументов.
Примечание 2. Приведенный ниже код, при условии, что функция concat() написана правильно

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

должен выводить:

hello python and stepik
hello*python*and*stepik
hello()()()python
hello
1$$2$$3$$4$$5$$6$$7$$8$$9

Примечание 3. Вызывать функцию concat() не нужно, требуется только реализовать.'''

def concat(*args, **kwargs):
    sargs = [str(i) for i in args]
    if kwargs:
        return kwargs['sep'].join(sargs)
    else:
        return ' '.join(sargs)


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

'''ВДРУГ ПРОБЛЕМЫ будут

def concat(*args, **kwargs):
    sargs = [str(i) for i in args]
    if kwargs:
        for key, value in kwargs.items():
            if key == 'sep':
                return value.join(sargs)
            elif key == 'end':
                return ' '.join(sargs)
    else:
        return ' '.join(sargs)

'''