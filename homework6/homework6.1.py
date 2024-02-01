def sort_age(my_list):  # key функуція сортування за віком
    return my_list['age']


def sort_name(my_list):  # key функуція сортування за довжиною ім'я
    return len(my_list['name'])


def av_age(my_list):  # функція для знаходження середнього віку
    age_sum = 0
    for a in range(len(my_list)):
        age_sum = age_sum + my_list[a]['age']
    return int(age_sum/len(my_list))


# list що складається зі словників (ім'я та вік)
people = [
    {
        'name': 'John',
        'age': 15
    },
    {
        'name': 'Ava',
        'age': 20
    },
    {
        'name': 'Alexander',
        'age': 15
    },
    {
        'name': 'Mykyta',
        'age': 20
    },
    {
        'name': 'Katherine',
        'age': 30
    },
    {
        'name': 'Jack',
        'age': 45
    }
]

people_copy = people.copy()  # копіюємо list про всяк випадок щоб випадково не змінити оригінальний

youngest_people = []
longest_name = []

people_copy.sort(key=sort_age)  # сорт. копію list за створ. кл. sort_age (поверне відстор. ліст за віком)
youngest_people.append(people_copy[0]['name'])  # перший ел. відсторт. list з найменшим віком, апендимо

for d in range(len(people_copy)):
    if d+1 == len(people_copy):  # уникаємо помилки index is out of range
        break
    else:
        if people_copy[0]['age'] == people_copy[d+1]['age']:  # якщо вік наступ. ел. == віку першого
            youngest_people.append(people_copy[d+1]['name'])  # додаємо елемент з однаковим віком
        else:
            continue

# сортуємо копію ліста people та вже ЗА ДОВЖИНОЮ ім'я, reverse щоб отримати найдовші імена спочатку
people_copy.sort(key=sort_name, reverse=True)
longest_name.append(people_copy[0]['name'])  # [0] ел. відсортованого list є найдовшим іменем

# аналогічний цикл до створеного вище та тепер перевіряємо вже довжину ['name']
for d in range(len(people_copy)):
    if d+1 == len(people_copy):
        break
    else:
        if len(people_copy[0]['name']) == len(people_copy[d+1]['name']):  # довж. name == найдовш?
            longest_name.append(people_copy[d+1]['name'])  # додаємо у список найдовших імен
        else:
            continue

print(f'~names of the youngest ppl: {youngest_people}', end="\n")
print(f'~ppl with the longest name: {longest_name}', end="\n")
print(f'\t~average age is: {av_age(people_copy)}')
