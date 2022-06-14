import unittest
from insert_sort import insertion_sort, Person, sort_person, shell_sort


class TestInsertSort(unittest.TestCase):
    def test_insert_sort(self):
        input = [-10, 10, -1000, 99, 1]
        expected = [-1000, -10, 1, 10, 99]
        self.assertEqual(expected, insertion_sort(input))  # add assertion here

    def test_insert_sort_descending(self):
        input = [-10, 10, -1000, 99, 1]
        expected = [99, 10, 1, -10, -1000]
        self.assertEqual(expected, insertion_sort(input, ascending=False))  # add assertion here

    def test_sort_person_asc(self):
        persons = [Person(name="Jack", age=21), Person(name="Uh", age=30), Person(name="Emy", age=11),
                   Person(name="Kluwin", age=12)]
        persons_ascending = [Person(name="Emy", age=11),
                             Person(name="Kluwin", age=12), Person(name="Jack", age=21), Person(name="Uh", age=30)]

        self.assertListEqual(persons_ascending, sort_person(persons))

    def test_shell_sort(self):
        input = [-10, 10, -1000, 99, 1, 20, -99, 100]
        expected = [-1000, -99, -10, 1, 10, 20, 99, 100]
        shell_sort(input)
        self.assertEqual(expected, input)  # add assertion here


if __name__ == '__main__':
    unittest.main()
