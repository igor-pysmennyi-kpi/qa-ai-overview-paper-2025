BASE_PROMT="""
### Prompt for QA regression agent

**Objective:**  

As a QA engineer performing regression you will make sure that all test flows listed were execued successfully. 
If test passes you will log Flow name: passed.
If test fails or you are not sure if it passes u will log Flow name: failed and step on which it failed. Add possible root cause if you can identify it.
 
**Important:**
- Mark test as passed only if u a sure that all steps were executed successfully and in accordance with AC
- Log all the selectors used throughout each test in format: step_name: action_performed: selector_used
---
*** Flow: {scenario_name} ***
---
 **Steps:**
{steps}

**Important:** Use only test data provided in test case. do not use any other extra data
**Important:** Ensure efficiency and accuracy throughout the process.
"""

class promt_e2e:
    def __init__(self, scenario_name, steps):
        self.scenario_name = scenario_name
        self.content = BASE_PROMT.format(scenario_name=scenario_name,steps=steps)
        
LOGIN_PROMT = promt_e2e("Login", """
 1.  Navigate to the [Sauce Labs Demo website](https://www.saucedemo.com/).  
 2.  Enter 'standard_user' into the Username field.  
 3.  Enter 'secret_sauce' into the Password field.  
 4.  Make sure Username and Password are filled in. If not, fill them in.  
 5.  Click the 'Login' button.  
 **Expected Result:**  
 *   The user is redirected to the product list page (e.g., `/inventory.html`).  
 *   The product list/inventory container is visible.""")


LOGIN_NEGATIVE_PROMT = promt_e2e("Login_Negative", """
 1.  Navigate to the [Sauce Labs Demo website](https://www.saucedemo.com/).  
 2.  Enter 'Blocked_User' into the Username field.  
 3.  Enter 'secret_sauce' into the Password field.  
 4.  Make sure Username and Password are filled in. If not, fill them in.  
 5.  Click the 'Login' button.  
 **Expected Result:**  
 *   The user is stays on the current page.  
 *   Error message 'Epic sadface: Username and password do not match any user in this service' is displayed.
 """)


MUTANT_LOGIN_PROMT = promt_e2e("Mutant_Login", """
 1.  Navigate to the [Sauce Labs Demo website](https://www.saucedemo.com/).  
 2.  Enter 'NOT_EXISTING_USER' into the Username field.  
 3.  Enter 'secret_sauce' into the Password field.  
 4.  Make sure Username and Password are filled in. If not, fill them in.  
 5.  Click the 'Login' button.  
 **Expected Result:**  
 *   The user is redirected to the product list page (e.g., `/inventory.html`).  
 *   The product list/inventory container is visible.
 """)


CHECKOUT_E2E_PROMT = promt_e2e("Order_and_Checkout", """
 1.  Navigate to the [Sauce Labs Demo website](https://www.saucedemo.com/).  
 2.  Enter 'standard_user' into the Username field.  
 3.  Enter 'secret_sauce' into the Password field.  
 4.  Make sure Username and Password are filled in. If not, fill them in.  
 5.  Click the 'Login' button.  
 6.  Wait for product list page to load
 7. Locate a specific product (e.g., "Sauce Labs Backpack").
 8. Click the "Add to cart" button for the "Sauce Labs Backpack".
 10. Click on the shopping cart link in the top right corner.
 11. Verify user is navigated to the shopping cart page (`/cart.html`) AND The "Sauce Labs Backpack" item is listed in the shopping cart, typically showing its name, description, price, and quantity (1).
 12. Locate and click the "Checkout" button.
 13. Verify 2.  User is on the 'Checkout: Your Information' page (`/checkout-step-one.html`) (Result of TC_CHECKOUT_001).
 14.  Enter the provided First Name (`Jane`) into the 'First Name' input field.
 15.  Enter the provided Last Name (`Doe`) into the 'Last Name' input field.
 16.  Enter the provided Postal Code (`12345`) into the 'Postal Code' input field.
 17.  Click the "Continue" button.
 18.  Verify  The current page URL is `/checkout-step-two.html`. And The page title/header indicates 'Checkout: Overview'. And  The item(s) previously added to the cart are correctly listed on the page (verify item name, quantity, price). And  The 'Item total' (subtotal before tax) is correctly calculated and displayed based on the items in the cart. And   A 'Tax' amount is calculated and displayed And  The 'Total' price (Item total + Tax) is correctly calculated and displayed.
 19.  Locate and click the "Finish" button.
 **Expected Results:**
1.  User is successfully navigated away from `/checkout-complete.html`.
2.  User is redirected to the main product list/inventory page (e.g., `/inventory.html`).
3.  The shopping cart icon/indicator shows that the cart is empty (e.g., no number badge).
4.  (Optional) The cart page (`/cart.html`) displays no items.
                               """)

SORT_PROMT = promt_e2e("Sort", """
 1.  Navigate to the [Sauce Labs Demo website](https://www.saucedemo.com/).  
 2.  Enter 'standard_user' into the Username field.  
 3.  Enter 'secret_sauce' into the Password field.  
 4.  Make sure Username and Password are filled in. If not, fill them in.  
 5.  Click the 'Login' button.
 6.  Wait for product list page to load
 4.  Click the sort dropdown.
 6.  Select "Price (low to high)".
 7.  Check if the displayed product prices are sorted from lowest to highest.

 **Expected Result:**  
 *   Price of second product is higher than the first one.
 """)

MUTANT_SORT_PROMT = promt_e2e("Mutant_Sort", """
 1.  Navigate to the [Sauce Labs Demo website](https://www.saucedemo.com/).  
 2.  Enter 'standard_user' into the Username field.  
 3.  Enter 'secret_sauce' into the Password field.  
 4.  Make sure Username and Password are filled in. If not, fill them in.  
 5.  Click the 'Login' button.
 6.  Wait for product list page to load
 4.  Click the sort dropdown.
 6.  Select "Name (A to Z)".
 7.  Check if the displayed product prices are sorted from lowest to highest.

 **Expected Result:**  
 *   Price of second product is higher than the first one.
 """)