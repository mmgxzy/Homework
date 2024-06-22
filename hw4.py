# class MagicCalcultor:
#     def __init__(self, number_1, number_2):
#         self.number_1 = number_1
#         self.number_2 = number_2

#     def __str__(self):
#         return f'Первое значение:  {self.number_1} \nВторое значение:  {self.number_1}  '
    
#     def __add__(self, other):
#         result = self.number_1 + other.number_1
#         return f"Результат сложения: {result}"

    
#     def __sub__(self, other):
#         result = self.number_1 - other.number_1
#         return f"Результат вычетания: {result}"
    
#     def __mul__(self, other):
#         result = self.number_1 * other.number_1
#         return f"Результат умножения: {result}"

    
#     def __truediv__(self, other):
#         result = self.number_1 / other.number_1
#         return f"Результат деления: {result}"

#     def __floordiv__(self, other):
#         result = self.number_1 // other.number_1
#         return f"Результат деления без остатка: {result}"


# num1 = MagicCalcultor(8, 0)
# num2 = MagicCalcultor(2, 0)
# print(num1)
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"Названия: {self.title}, Автор: {self.author}, год выпуска: {self.year}"

    def info(self):
        print(f"Названия: {self.title}, Автор: {self.author}, год выпуска: {self.year}")

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __str__(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год: {self.year}"

book1 = Book("Последния миссия ангела любовь", "Чхве Юнге", 2021)
book2 = Book("Лето в пионерском галстуке", "Елена Малисова", 2020)

book1.info()
book2.info()

print(book1 < book2) 
print(book1 > book2)  
print(book1 == book2)

