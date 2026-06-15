# task 9.1
class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError("Сторона повинна бути більше 0")
            super().__setattr__(name, value)
            
        elif name == "angle_a":
            super().__setattr__(name, value)
            angle_b_value = 180 - value
            super().__setattr__('angle_b', angle_b_value)

my_rhombus = Rhombus(10, 60)

print(f"Сторона: {my_rhombus.side_a}")
print(f"Кут А: {my_rhombus.angle_a}")
print(f"Кут Б (порахований автоматично): {my_rhombus.angle_b}")
