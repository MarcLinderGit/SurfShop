import datetime

class TooManyBoardsError(Exception):
    def __str__(self):
        msg = 'Cart cannot have more than 4 surfboards in it!'
        return msg

class CheckoutDateError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        # Initialize the shopping cart with default values.
        self.num_surfboards = 0
        self.checkout_date = None
        self.rental_days = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        # Check if adding 'quantity' surfboards would exceed the limit of 4.
        if self.num_surfboards + quantity > 4:
            # Raise a custom exception if the limit is exceeded.
            raise TooManyBoardsError
        else:
            # If not exceeding the limit, add the surfboards to the cart.
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
        # Check if the provided checkout date is in the past.
        if date <= datetime.datetime.now():
            # Raise a custom exception if the date is invalid.
            raise CheckoutDateError
        else:
            # Set the checkout date if it's valid.
            self.checkout_date = date

    def apply_locals_discount(self):
        # Apply a locals discount to the shopping cart.
        self.locals_discount = True
