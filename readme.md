# Data for paper AI-Driven Testing Tools in Modern Quality Assurance: Benefits, Challenges, and Future Directions


## User stories used in coverage

User stories below are covering sample e-commerse application called [https://www.saucedemo.com/] [Swag Labs]

## User login

*ID*: ST_LOGIN  
*Title*: As a user I want to login into the system to see product list  
*Test data*: correct_username: standard_user; correct_password: secret_sauce  ; incorrect_password: password01  
*Preconditions*: User open main page  
*Acceptance criteria*:
AC1: Given correct login data After entering correct_username and correct_password in form Then user is reditected to product list page  
AC2: Given incorrect login data After entering correct_username and incorrect_password in form Then user stays on login page And user is show error message "Username and password do not match any user in this service"  

## Sorting products

*ID*: ST_SORT  
*Title*: As a user, I want to sort products by price I can find affordable items  
*Test data*: username: standard_user; password: secret_sauce  
*Preconditions*: User logged in with username and password and is on the inventory page (/inventory.html).  
*Acceptance criteria*:  
AC1: When sort dropdown is pressed Then the dropdown contains options: "Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)".  
AC2: Given dropdown is pressed When selecting "Price (low to high)" Then products are sorted by price, lowest first.  
AC3: Given dropdown is pressed When selecting "Price (high to low)" Then products are sorted by price, highest first.  

## Adding item to cart

*ID*: ST_CART  
*Title*: As a user, I want to add an item to my shopping cart directly from the product list so that I can collect items I intend to purchase.  
*Test data*: username: standard_user; password: secret_sauce  
*Preconditions*: User logged in with username and password and is on the inventory page (/inventory.html).  
*Acceptance criteria*:  
AC1: Given each product item listed on the inventory page Then product has a visible "Add to cart" button.  
AC2: When user clicks the "Add to cart" button for a specific product Then single item is added to the shopping cart And the shopping cart icon in the header updates to display a badge indicating the total number of items currently in the cart (e.g., shows '1' after adding the first item).  
AC3: Given product is added to the shopping card When user clickes on cart icon Then user can see selected item  

## Checkout

*ID*: ST_CHECKOUT
*Title*: As a user, I want to complete the checkout process so that I can purchase the items I have added to my cart.  
*Test data*: username: standard_user; password: secret_sauce; First Name: Jane; Last *Name*: Doe; Postal Code: 12345  
*Preconditions*: User logged in with username and password. User has at least one item added to the shopping cart. User is on the shopping cart page (/cart.html)  
*Acceptance criteria*:  
AC1: Given product in cart When user clics on "Checkout" button Then User is navigated to the 'Checkout: Your Information' page (/checkout-step-one.html).  
AC2: Given User input First Name, Last Name, and Postal Code into the respective fields When User clicks "Continue" Then user navigates to the 'Checkout: Overview' page (/checkout-step-two.html) And The 'Checkout: Overview' page correctly displays the item(s) from the cart, Item total (subtotal), Tax, and Total price.
AC3: When user clicks 'Finish' on the 'Checkout: Overview' Then user navigates to the 'Checkout: Complete!' page (/checkout-complete.html) And The 'Checkout: Complete!' page displays a success message (e.g., "THANK YOU FOR YOUR ORDER")
AC4: Given user stays on "Checkout: Complete!" page When user clicks "Back home" button Then user is redirected to product list page And the shopping cart is empty after successfully completing the order.

## Item preview

*ID*: ST_PREVIEW  
*Title*: As a user I want to see preview picture on product list to be able to select product  
*Test data*: username: standard_user; password: secret_sauce  
*Preconditions*: User logged in with username and password  
*Acceptance criteria*:  
AC1: Each product in product list has a distinctive product picture
AC2: Given product in the list When user clicks on this product Then same picture as on preview is shown
