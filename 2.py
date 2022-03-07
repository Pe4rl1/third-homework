
people = [ {'name': 'Anna', 'age': 25, 'gender': 'female'},
    {'name': 'Lena', 'age': 12, 'gender': 'female'},
    {'name': 'Nastya', 'age': 33, 'gender': 'female'},
    {'name': 'Angelina', 'age': 30, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Anna', 'age': 40, 'gender': 'female'},
    {'name': 'Ira', 'age': 11, 'gender': 'female'},
    {'name': 'Polina', 'age': 17, 'gender': 'female'},
    {'name': 'Oksana', 'age': 18, 'gender': 'female'},
    {'name': 'Anna', 'age': 8, 'gender': 'female'},
    {'name': 'Yana', 'age': 43, 'gender': 'female'},
    {'name': 'Kira', 'age': 18, 'gender': 'female'},
    {'name': 'Nastya', 'age': 25, 'gender': 'female'},
    {'name': 'Tamara', 'age': 31, 'gender': 'female'},
    {'name': 'Rita', 'age': 39, 'gender': 'female'},
    {'name': 'Sveta', 'age': 25, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Nastya', 'age': 28, 'gender': 'female'},
    {'name': 'Lera', 'age': 19, 'gender': 'female'},
    {'name': 'Sara', 'age': 10, 'gender': 'female'},
    {'name': 'Alex', 'age': 44, 'gender': 'male'},
    {'name': 'Dima', 'age': 33, 'gender': 'male'},
    {'name': 'Fedor', 'age': 38, 'gender': 'male'},
    {'name': 'Nikita', 'age': 32, 'gender': 'male'},
    {'name': 'Alex', 'age': 25, 'gender': 'male'},
    {'name': 'Foma', 'age': 70, 'gender': 'male'},
    {'name': 'Evgeniy', 'age': 25, 'gender': 'male'},
    {'name': 'Alex', 'age': 12, 'gender': 'male'},
    {'name': 'Kiril', 'age': 27, 'gender': 'male'},
    {'name': 'Mihail', 'age': 30, 'gender': 'male'}
    ]
my_dict_length = len (people)
print(f'Всего людей {my_dict_length}')


print()


girls = 0
for i in range(0,30):
    if people[i]['gender'] == 'female':
        girls += 1
print(f"Женщин {girls}")

print()

males = 0
for a in range(0,30):
    if people[a]['gender'] == 'male':
        males += 1
print(f'Мужчин {males}')

print()

adult = 0
for a in range(0,30):
    if people[a]['age'] >= 18:
        adult += 1
print(f'Совершеннолетних {adult}')

print()

names = []
for a in range(0,30):
    names.append(people[a]['name'])
print(*names, sep='\n')

print()

ages = []
for a in range(0,30):
    if people[a]['age'] in ages:
        pass
    else:
        ages.append(people[a]['age'])
print(*ages, sep='\n')

print()


popularname = []
checked = []
count = {}
for a in range(0,30):
    if names[a] in checked:
        pass
    else:
        repeats = names.count(names[a])
        checked.append(names[a])
        count[names[a]] = repeats

for a in range(0,30):
    if names[a] in popularname:
        pass
    else:
        if count[names[a]] >= 3:
            popularname.append(names[a])
print(*popularname , sep='\n')

print()

for a in range(0,30):
    if people[a]['age'] >= 35 and people[a]['gender'] == 'male' and people[a]['name'][0] == 'F':
        print(people[a]['name'])




    






