#                                                          Система заказа еды by Alex


import time
import json


class Menu:
    def __init__(self, filename="menu.json"):
        self.load_menu(filename)
        self.order_list = []  
        self.total_price = 0  


    def load_menu(self, filename): 
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.food_menu = data.get("food", {})
                self.drink_menu = data.get("drinks", {})

        except FileNotFoundError:
            print(f"Ошибка: Файл {filename} не найден.")
            self.food_menu = {}
            self.drink_menu = {}


    def order_food(self):
        while True:
            print("\n" + "-" * 40)
            print(f"\nПожалуйста, выберите блюдо:")
            display_menu_columns("Меню блюд", self.food_menu, 3)

            request = input("Ваш выбор (или 'назад' (или 'н') для выхода): ").strip()

            if request.lower() in ["назад", "н", "exit"]:
                break

            if request in self.food_menu:
                self.add_to_order(request, self.food_menu[request])
            else:
                self.check_availability(request)


    def order_drinks(self):
        while True:
            print("\n" + "-" * 40)
            print(f"\nВыберите напиток:")
            display_menu_columns("Меню блюд", self.drink_menu, 3)

            request = input("Ваш выбор (или 'назад' (или 'н') для выхода): ").strip()

            if request.lower() in ["назад", 'н', "exit"]:
                break

            if request in self.drink_menu:
                self.add_to_order(request, self.drink_menu[request])
            else:
                self.check_availability(request)


    def add_to_order(self, item, price):
        while True:
            try:
                print("\n" + "-" * 40)
                quantity = int(input(f"Сколько порций {item} вам нужно? ").strip())
                if quantity <= 0:
                    print("Количество должно быть больше 0!")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите число!")

        total_item_price = price * quantity
        print(f"{item} ({quantity} шт.) добавлен в заказ ({total_item_price} руб.).")
        self.order_list.append((item, quantity, total_item_price))
        self.total_price += total_item_price


    def check_availability(self, item):
        print(f"Кажется, {item} нет в наличии, сейчас уточню!")
        for _ in range(3):
            time.sleep(1)
            print(".", end='', flush=True)
        time.sleep(1)
        print(f"\n{item} действительно нет в наличии, попробуйте что-то другое.")


    def show_order(self):
        if self.order_list:
            print("\n" + "-" * 40 + "Заказ" + "-" * 40)
            print("\nВаш заказ:")
            for item, quantity, total_item_price in self.order_list:
                print(f"- {item} ({quantity} шт.) — {total_item_price} руб.")
            print(f"\nИтого: {self.total_price} руб.")
            print("\n" + "-" * 40)
        else:
            print("\nВы ничего не заказали.")

    
    def display_menu(self, items):
        print("-" * 30)
        for name, price in items.items():
            print(f"{name:<20} {price} руб.")
        print("-" * 30)


def display_menu_columns(title, items, columns=3):
    print(f"\n{title}")
    print("-" * len(title))
    items_list = list(items.items())  

    for i in range(0, len(items_list), columns):
        row = [f"{items_list[j][0]:<20} {items_list[j][1]} руб." for j in range(i, min(i + columns, len(items_list)))]
        print(" | ".join(row))


def hello_message():
    print("Добро пожаловать в кафе!")


hello_message()
menu = Menu("menu.json") 

while True:
    print("\nЧто вы хотите сделать?")
    print("1. Заказать еду")
    print("2. Заказать напиток")
    print("3. Показать текущий заказ")
    print("4. Завершить заказ")

    choice = input("Введите номер действия: ").strip()

    if choice == "1":
        menu.order_food()
    elif choice == "2":
        menu.order_drinks()
    elif choice == "3":
        menu.show_order()
    elif choice == "4":
        menu.show_order()
        print("Спасибо за заказ! Хорошего дня!")
        break
    else:
        print("Некорректный ввод, попробуйте снова.")
