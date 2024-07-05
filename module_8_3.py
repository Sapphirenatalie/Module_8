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
