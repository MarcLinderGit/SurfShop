import unittest
import surf  # Assuming that 'surf' is a module containing the code you want to test
import datetime

class SurfShopTests(unittest.TestCase):

    def setUp(self):
        # Create a new shopping cart before each test case to isolate them.
        self.cart = surf.ShoppingCart()

    def test_add_surfboard(self):
        # Test adding a single surfboard to the cart.
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        # Test adding 2 to 4 surfboards to the cart.
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surf.ShoppingCart()  # Create a new cart for the next iteration.

    @unittest.skip
    def test_add_too_many_surfboards(self):
        # Test adding more than the allowed number of surfboards.
        self.assertRaises(surf.TooManyBoardsError, self.cart.add_surfboards, 5)

    # This test is currently skipped and expected to fail in the old version of the code.
    # @unittest.expectedFailure
    def test_apply_locals_discount(self):
        # Test applying a locals discount and check if it's correctly applied.
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def test_add_invalid_checkout_date(self):
        # Test setting an invalid checkout date in the past.
        date = datetime.datetime.now()
        self.assertRaises(surf.CheckoutDateError, self.cart.set_checkout_date, date)

# Run the unit tests
unittest.main()
