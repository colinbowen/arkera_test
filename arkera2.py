import unittest


def check_largest_loss(price_list):
    if len(price_list) < 2:
        return 0

    if all(isinstance(x, int) for x in price_list):
        loss_price = max(price_list) - min(price_list)

    return loss_price


class TestLoss (unittest.TestCase):
    def test_check_largest_loss(self):
        prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test1 = check_largest_loss(prices)
        self.assertEqual(test1, 9)

        prices = [50, 40, 30, 20, 10, 0]
        test2 = check_largest_loss(prices)
        self.assertEqual(test2, 50)

        prices = [100, 80, 60, 40, 20, 0]
        test3 = check_largest_loss(prices)
        self.assertEqual(test3, 100)


unittest.main()
