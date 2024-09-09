import unittest
from lib import count_common_elements

class TestCountCommonElements(unittest.TestCase):

    def test_no_lists(self):
        self.assertEqual(count_common_elements(), 0)

    def test_one_list(self):
        self.assertEqual(count_common_elements([1, 2, 3]), 3)

    def test_no_common_elements(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(count_common_elements(list1, list2), 0)

    def test_all_common_elements(self):
        list1 = [1, 2, 3, 4]
        list2 = [2, 3, 4, 5]
        list3 = [3, 4, 6, 7]
        self.assertEqual(count_common_elements(list1, list2, list3), 2)  # 3 and 4 are common

    def test_partial_common_elements(self):
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        list3 = [3, 4, 5]
        self.assertEqual(count_common_elements(list1, list2, list3), 1)  # Only 3 is common

    def test_empty_lists(self):
        list1 = []
        list2 = []
        list3 = []
        self.assertEqual(count_common_elements(list1, list2, list3), 0)

    def test_mixed_data_types(self):
        list1 = [1, 'a', 2.5]
        list2 = ['a', 2.5, 3]
        list3 = [2.5, 'b', 'a']
        self.assertEqual(count_common_elements(list1, list2, list3), 2)  # 'a' and 2.5 are common

if __name__ == "__main__":
    unittest.main()
