# Surf Shop Application
This project employs unit testing to ensure the functionality and reliability of a Python-based surf shop application. It includes tests for adding surfboards, applying discounts, and handling exceptions to maintain a robust and error-resistant shopping experience. The project contains two Python files: `surf.py` and `test.py`. It is designed to simulate a surf shop application, allowing customers to add surfboards to their shopping cart, apply discounts, and set a checkout date. The unit tests in `test.py` are used to verify the functionality of the `surf.py` module.

## Files

- **surf.py**: This module contains the implementation of the surf shop's shopping cart and related exceptions. It provides methods for adding surfboards, setting a checkout date, and applying a locals discount. It also defines custom exceptions for handling errors related to the shopping cart.

- **test.py**: This module contains unit tests for the functionality of the `surf.py` module. The tests cover various scenarios, such as adding surfboards, applying discounts, and handling exceptions.

## How to Run Tests

To run the unit tests and verify the functionality of the surf shop application, follow these steps:

1. Make sure you have Python installed on your system.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the project files.

4. Run the unit tests by executing the following command:

   ```
   python test.py
   ```

   This will execute the test cases defined in `test.py` and display the test results, indicating whether the surf shop application functions as expected.

## Test Descriptions

- `test_add_surfboard`: This test checks if a single surfboard can be added to the cart and if the confirmation message is correct.

- `test_add_surfboards`: This test adds 2 to 4 surfboards to the cart, testing the behavior of adding multiple surfboards and the confirmation messages.

- `test_add_too_many_surfboards` (skipped): This test is skipped and expected to raise an error when attempting to add more than the allowed number of surfboards.

- `test_apply_locals_discount`: This test verifies the application of a locals discount and checks if it is correctly applied to the shopping cart.

- `test_add_invalid_checkout_date`: This test checks whether the system correctly handles attempts to set a checkout date in the past, raising the expected exception.

## Notes

- The `test_add_too_many_surfboards` test is currently skipped, but you can uncomment it and remove the `@unittest.skip` decorator to test the behavior when trying to add too many surfboards.

- The project includes custom exceptions, such as `TooManyBoardsError` and `CheckoutDateError`, to handle specific error scenarios in the surf shop application.

- The unit tests in `test.py` help ensure that the surf shop application behaves as intended and can serve as a foundation for further development or debugging.

Enjoy simulating your surf shop's shopping cart with these tests!
