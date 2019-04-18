class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score in range(0,61):
            return "C"

        elif self.score in range(61,81):
            return "B"
        elif self.score not in range(0,101):
            raise ValueError

        else:
            return "C"


import unittest


class TestStudent(unittest.TestCase): # it must be a subclass of unittest.TestCase
    def test_grade(self):  # the function name must start with "test"
        s1 = Student("Tommy", -1)
        with self.assertRaises(ValueError):   # how does the keyword "with" work?
            s1.get_grade()


# what if i have several test class
class Test(unittest.TestCase):
    def test_grade(self):  # the function name must start with "test"
        s1 = Student("Tommy", -1)
        with self.assertRaises(ValueError):   # how does the keyword "with" work?
            s1.get_grade()


if __name__ == '__main__':
    unittest.main()    # must run test in this way



