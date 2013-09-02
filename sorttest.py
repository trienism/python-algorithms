from sort import Sort

import unittest

# test class for the triangle class
class TestSort(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.items = [38, 27, 43, 3, 9, 82, 10]
        self.sort = Sort()

        
    def test_merge_sort(self):
        print '---- depth first search ----'
        print self.sort.merge_sort(self.items)


# runs the unit tests
if __name__ == '__main__':
    unittest.main()
