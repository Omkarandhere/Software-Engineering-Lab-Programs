import unittest

class StudentGrades:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_highest_grade(self):
        if not self.grades:
            return None
        return max(self.grades)

    def has_passed(self, passing_threshold=50):
        return self.get_average() >= passing_threshold

# Test Suite
class TestStudentGrades(unittest.TestCase):
    def setUp(self):
        self.student = StudentGrades("John Doe")

    def test_add_grade(self):
        self.student.add_grade(90)
        self.student.add_grade(80)
        self.assertEqual(self.student.grades, [90, 80])

    def test_add_grade_invalid(self):
        with self.assertRaises(ValueError):
            self.student.add_grade(110)
        with self.assertRaises(ValueError):
            self.student.add_grade(-10)

    def test_get_average(self):
        self.student.add_grade(70)
        self.student.add_grade(80)
        self.assertEqual(self.student.get_average(), 75)

    def test_get_average_empty(self):
        self.assertEqual(self.student.get_average(), 0)

    def test_get_highest_grade(self):
        self.student.add_grade(70)
        self.student.add_grade(85)
        self.student.add_grade(90)
        self.assertEqual(self.student.get_highest_grade(), 90)

    def test_get_highest_grade_empty(self):
        self.assertIsNone(self.student.get_highest_grade())

    def test_has_passed(self):
        self.student.add_grade(60)
        self.student.add_grade(70)
        self.assertTrue(self.student.has_passed())

    def test_has_not_passed(self):
        self.student.add_grade(40)
        self.student.add_grade(45)
        self.assertFalse(self.student.has_passed())

    def test_has_passed_custom_threshold(self):
        self.student.add_grade(40)
        self.student.add_grade(45)
        self.assertTrue(self.student.has_passed(passing_threshold=40))

if __name__ == "__main__":
    unittest.main()
