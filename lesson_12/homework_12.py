#1
def calculate_string_sum(data_string):

    try:
        parts = data_string.split(',')
        total = 0
        for item in parts:
            total += int(item)
        return total
    except ValueError:
        return "Не можу це зробити!"

#2
def get_rhombus_angle_b(angle_a):
    if angle_a <= 0 or angle_a >= 180:
        raise ValueError("Кут повинен бути між 0 та 180 градусами")
    return 180 - angle_a

#3
def get_student_score(score):
    if score < 0 or score > 100:
        return "Некоректний бал"
    return score
