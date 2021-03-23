import unittest
from random import randrange

from task import task


def create_rand_data(amount: int) -> dict[str, int]:
    data = {}
    for i in range(0, amount):
        ones_length = randrange(1, 25)
        zeros_length = randrange(1, 25)
        ones = '1' * ones_length
        zeros = '0' * zeros_length
        data[ones + zeros] = ones_length

    print(data)
    return data


class TestTask1(unittest.TestCase):

    def setUp(self):
        self.TEST_DATA = create_rand_data(50)

    def test_task(self):
        for item, res in self.TEST_DATA.items():
            self.assertTrue(task(item), res)


if __name__ == '__main__':
    unittest.main()
