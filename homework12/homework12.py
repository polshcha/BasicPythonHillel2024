# Корзина для покупок
#
# 1) Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
#
# 2) Створіть клас "Покупець".
# Як поля можна використовувати прізвище, ім'я, по батькові, мобільний телефон і т.д.
#
# 3) Створіть клас "Замовлення".
# Замовлення може містити кілька товарів, причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод __str__() для коректного виведення інформації про це замовлення.

class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.dimensions} {self.description} {self.name}"

    def full_desc(self):
        # Повний опис товару:
        desc = "\n\t" + 5 * "*".center(5) + ('''
                \tWe have a new supply of wonderful {product_name} in our store!
                Today only, make sure you get your {size} {product_desc} {product_name} for only ${price}!
                '''.format(product_name=self.name,
                           product_desc=self.description,
                           size=self.dimensions,
                           price=self.price)) + "\t" + 5 * "*".center(5)
        return desc


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        # Інформація про покупця:
        user_info = "\nUser: {user_fullname} \nPhone number: {user_phone_num}".format(
            user_fullname=self.name.title() + " " + self.surname.title(),
            user_phone_num=self.numberphone)
        return user_info


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items_output = ""

        for key in self.products.keys():
            items_output += f"{key} : {self.products[key]} pcs.\n"

        order_info = f"{self.user}\n{items_output}"
        return order_info

    def get_total(self):
        total = 0
        for key, value in self.products.items():
            total += key.price * value
        print(f"total is: ${total}")
        return total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5
print(apple.full_desc())

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40