"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:
    def __init__(self, data):
        self.data = data

    # def __iter__(self):
    #     self.item = -1
    #     return self
    #
    # def __next__(self):
    #     if self.item < len(self.data):
    #         self.item += 1
    #         return self.item
    #     else:
    #         StopIteration

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")

        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс")


# код для проверки 
my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i)  # 1 2 3

print(my_list[1])  # 2
