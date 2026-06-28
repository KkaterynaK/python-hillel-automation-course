def calculate_string_sum(data_string):
    try:
        parts = data_string.split(',')
        total = 0
        for item in parts:
            total += int(item)
        return total
    except ValueError:
        return "Не можу це зробити!"

my_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in my_list:
    print(calculate_string_sum(item))
