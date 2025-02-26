import unittest
from cart import Cart
from device import Device


class TestCart(unittest.TestCase):
    
    def setUp(self):
        self.cart = Cart()
        self.device1 = Device("iPhone 13", 999, 10)
        self.device2 = Device("MacBook Pro", 1999, 5)

    def test_add_device(self):
        self.cart.add_device(self.device1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0][1], 2)
        self.assertEqual(self.cart.total_price, 1998)

    def test_remove_device(self):
        self.cart.add_device(self.device1, 3)
        self.cart.remove_device(self.device1, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0][1], 2)
        self.assertEqual(self.cart.total_price, 1998)

    def test_remove_device_completely(self):
        self.cart.add_device(self.device1, 2)
        self.cart.remove_device(self.device1, 2)
        self.assertEqual(len(self.cart.items), 0)
        self.assertEqual(self.cart.total_price, 0)

    def test_get_total_price(self):
        self.cart.add_device(self.device1, 1)
        self.cart.add_device(self.device2, 1)
        self.assertEqual(self.cart.get_total_price(), 2998)

    def test_checkout(self):
        self.cart.add_device(self.device1, 2)
        self.cart.add_device(self.device2, 1)
        self.cart.checkout()
        self.assertEqual(self.device1.stock, 8)
        self.assertEqual(self.device2.stock, 4)

if __name__=='__main__':
    unittest.main()