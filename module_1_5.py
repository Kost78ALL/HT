immutable_var=1,'a',2,'b',3,'c' # создание кортежа
print(immutable_var,'- Объявленный кортеж')
mutable_list=[1,'a',2,'b',3,'c'] # создание списка
print(mutable_list,'- объявленный список')
mutable_list[3]='x'
print(mutable_list,'- изменённый список')
print('ошибка в восьмой линии втом что элементы кортежа не могут быть изменены')
immutable_var[2]='x'
print(immutable_var)