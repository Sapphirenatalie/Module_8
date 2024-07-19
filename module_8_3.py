class Car:

    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers
        self.__is_valid_vin(vin_number)
        self.__is_valid_numbers(numbers)

    @staticmethod
    def __is_valid_vin(vin_number):
        min_val, max_val = 1000000, 9999999
        if isinstance(vin_number, str):
            raise IncorrectVinNumber('Некорректный тип vin номера:')
        if vin_number not in range(min_val, max_val):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        if isinstance(vin_number, int) and vin_number in range(min_val, max_val):
            return True

    @staticmethod
    def __is_valid_numbers(numbers):
        if isinstance(numbers, int):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if isinstance(numbers, str) and len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        if isinstance(numbers, str) and len(numbers) == 6:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(f'{exc.message}')
except IncorrectCarNumbers as exc:
    print(f'{exc.message}')
else:
    print(f'{first.model} успешно создан')

print('---------------')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

print('---------------')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

# Вывод на консоль:
# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера

# Создание исключений
# Задача "Некорректность":
# Создайте 3 класса (2 из которых будут исключениями):
# Класс Car должен обладать следующими свойствами:
# Атрибут объекта model - название автомобиля (строка).
# Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
# Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
# Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# Атрибут __numbers - номера автомобиля (строка).
# Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
# Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.

# Классы исключений IncorrectVinNumber и IncorrectCarNumbers,
# объекты которых обладают атрибутом message - сообщение,
# которое будет выводиться при выбрасывании исключения.
# Работа методов __is_valid_vin и __is_valid_numbers:
# __is_valid_vin
# Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
# если передано не целое число.
# (тип данных можно проверить функцией isinstance).
# Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
# если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
# Возвращает True, если исключения не были выброшены.
# __is_valid_numbers
# Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
# если передана не строка. (тип данных можно проверить функцией isinstance).
# Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
# переданная строка должна состоять ровно из 6 символов.
# Возвращает True, если исключения не были выброшены.

# ВАЖНО!
# Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
# (в __init__ при объявлении атрибутов __vin и __numbers).
