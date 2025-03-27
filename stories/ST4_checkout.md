ID: ST_CHECKOUT
Title: As a user, I want to complete the checkout process so that I can purchase the items I have added to my cart.  
Test data: username: standard_user; password: secret_sauce; First Name: Jane; Last Name: Doe; Postal Code: 12345  
Preconditions: User logged in with username and password. User has at least one item added to the shopping cart. User is on the shopping cart page (/cart.html)  
Acceptance criteria:  
AC1: Given product in cart When user clics on "Checkout" button Then User is navigated to the 'Checkout: Your Information' page (/checkout-step-one.html).  
AC2: Given User input First Name, Last Name, and Postal Code into the respective fields When User clicks "Continue" Then user navigates to the 'Checkout: Overview' page (/checkout-step-two.html) And The 'Checkout: Overview' page correctly displays the item(s) from the cart, Item total (subtotal), Tax, and Total price.
AC3: When user clicks 'Finish' on the 'Checkout: Overview' Then user navigates to the 'Checkout: Complete!' page (/checkout-complete.html) And The 'Checkout: Complete!' page displays a success message (e.g., "THANK YOU FOR YOUR ORDER")
AC4: Given user stays on "Checkout: Complete!" page When user clicks "Back home" button Then user is redirected to product list page And the shopping cart is empty after successfully completing the order.
