my_dict={'I':45,'bro':38}
print(my_dict,'-созданный словарь')
print(my_dict['I'],'-значение ключа I')
print(my_dict.get('Mum'),'-значение несуществующего ключа Mum')
my_dict.update({'Mum':76,'Son':9}) # Добавление в словарь
print(my_dict,'-обновлённый словарь')
del my_dict['I'],my_dict['Mum'] # Удаление пары
print(my_dict,'-словарь после удаления пары' )
my_dict.pop('bro')
print(my_dict,'- удалил пару bro popой))')
my_set={1,2,2,1,'I','I',3,4,5,5,5,'an','an','Uh',(1,2,3,4,5)} #  объявление множества
print(my_set,'-уникальные значения множества')
my_set.update([48,'New']) #   Добавление эл. множества
my_set.discard('I') # удаление элемента мн-ва "I"
print(my_set,'- обновлённое множество уникальных значений')
