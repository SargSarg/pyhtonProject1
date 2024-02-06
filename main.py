print(round(11*2.5/3, 2))
pi=3.14159
print(round(pi**2/2))

person = {'name' : 'Ivan Petrov'}  # словари делают так ключ:объект
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'
print(person)
print(person.keys()) # просим показать КЛЮЧИ
print(person.values()) # или значения(оъекты)
person.pop('phone') # удаляем не по индексу а по имени ключа

string=("1 1 2 3 5 8 13 21 34 55")
L = string.split()
L = list(map(int, string.split())) #спомощью мапа завернутого в лист превращаем все строки в числа
L[0], L[-1] = L[-1], L[0] # меняем местами первое и последнее число
L.append(sum(L)) # к списку L добавить в конец SUM(L)
print(L)
