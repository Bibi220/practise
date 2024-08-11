import unittest


class SortingTest(unittest.TestCase):
    def test_sort(self):
        l = [4 ,5 ,6 ,6 ,5]
        l.sort()


        for i in range(len(l) - 1):
            self.assertTrue(l[i] <= l[i+1])

        i = 0
        while i < len(l)-1:
            self.assertTrue(l[i] <= l[i + 1])
            i += 1


        print(l)

if __name__ == '__main__':
    unittest.main()
