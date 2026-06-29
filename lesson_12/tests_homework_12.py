class TestHomeworks(unittest.TestCase):

    # 1
    def test_sum_positive(self):
        self.assertEqual(calculate_string_sum("1,2,3,4"), 10)

    def test_sum_with_large_numbers(self):
        self.assertEqual(calculate_string_sum("1,2,3,4,50"), 60)

    def test_sum_negative_with_letters(self):
        self.assertEqual(calculate_string_sum("qwerty1,2,3"), "Не можу це зробити!")

    def test_sum_empty_string(self):
        self.assertEqual(calculate_string_sum(""), "Не можу це зробити!")

    # 2
    def test_angle_positive_60(self):
        self.assertEqual(get_rhombus_angle_b(60), 120)

    def test_angle_positive_90(self):
        self.assertEqual(get_rhombus_angle_b(90), 90)

    def test_angle_error_negative(self):
        with self.assertRaises(ValueError):
            get_rhombus_angle_b(-10)

    # 3
    def test_score_positive(self):
        self.assertEqual(get_student_score(95.5), 95.5)

    def test_score_too_high(self):
        self.assertEqual(get_student_score(150), "Некоректний бал")

    def test_score_negative_value(self):
        self.assertEqual(get_student_score(-5), "Некоректний бал")

if __name__ == '__main__':
    unittest.main()
