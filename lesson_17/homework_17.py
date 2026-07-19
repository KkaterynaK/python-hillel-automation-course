#task_1
# Генератор 1: Парні числа від 0 до N
def even_numbers_generator(n):
    current = 0
    while current <= n:
        yield current
        current += 2


# Генератор 2: Послідовність Фібоначчі до числа N
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


#task_2
# Ітератор 1: Зворотне виведення елементів списку
class ReverseIterator:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = len(data_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        element = self.data_list[self.index]
        self.index -= 1
        return element


# Ітератор 2: Парні числа в діапазоні від 0 до N
class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


#task_3
# Декоратор 1: Логування аргументів та результатів функції
def log_arguments_and_results(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції '{func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Функція '{func.__name__}' повернула результат: {result}")
        return result
    return wrapper


# Декоратор 2: Перехоплення та обробка винятків
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Увага! У функції '{func.__name__}' стався виняток: {e}")
            return None
    return wrapper




@log_arguments_and_results
def add_numbers(a, b):
    return a + b

@handle_exceptions
def divide_numbers(a, b):
    return a / b


if __name__ == "__main__":
    print("--- Парні числа до 10 (Генератор) ---")
    for num in even_numbers_generator(10):
        print(num)

    print("\n--- Числа Фібоначчі до 50 (Генератор) ---")
    for num in fibonacci_generator(50):
        print(num)

    print("\n--- Зворотний список (Ітератор) ---")
    my_list = ['QA', 'Python', 'Hillel']
    for item in ReverseIterator(my_list):
        print(item)

    print("\n--- Парні числа до 8 (Ітератор) ---")
    for num in EvenNumbersIterator(8):
        print(num)

    print("\n--- Перевірка декоратора логування ---")
    add_numbers(5, 7)

    print("\n--- Перевірка декоратора помилок (ділення на 0) ---")
    divide_numbers(10, 0)
