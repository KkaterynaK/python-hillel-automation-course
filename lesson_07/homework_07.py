# task 1

def multiplication_table(number):
    multiplier = 1
    while multiplier <= number:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(5)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2

def sum_two_numbers(a, b):
    result = a +b
    return result
print(sum_two_numbers(3, 4))

# task 3

def calculate_average(number_list):
    average = sum(number_list) / len(number_list)
    return average
print(calculate_average([10, 20, 30, 40, 50]))

# task 4

def reverse_string(user_string):
    return user_string[::-1]
print(reverse_string("перевірка"))

# task 5

def find_longest_word(words_list):
    longest = words_list[0]
    for word in words_list:
        if len(word) > (len(longest)):
            longest = word

    return(longest)

words = ["QA", "Python", "Automation", "Task"]
print(find_longest_word(words))

# task 6

def find_substring(str1, str2):
    return str1.find(str2)
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))


str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7

def check_unique_characters(text_to_check):

    unique_count = len(set(text_to_check))
    return unique_count > 10
print(check_unique_characters("Python"))

# task 8

def has_letter_h(word):
    return "h" in word.lower()
while True:
    user_word = input("Введіть слово з літерою 'h': ")
    if has_letter_h(user_word):
        print("Чудово, буква є!")
        break
    print("Немає такої букви, спробуй ще раз.")

# task 9

def filter_only_strings(mixed_list):
    strings_only = []
    for item in mixed_list:
        if type(item) == str:
            strings_only.append(item)
    return strings_only

test_list = [1, "QA", 3, True, "Automation"]
print(filter_only_strings(test_list))

# task 10

def sum_even_numbers(numbers_list):
    total_sum = 0
    for number in numbers_list:
        if number % 2 == 0:
            total_sum += number
    return total_sum
print(sum_even_numbers(list(range(10))))
