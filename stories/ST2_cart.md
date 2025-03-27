ID: ST_CART  
Title: As a user, I want to add an item to my shopping cart directly from the product list so that I can collect items I intend to purchase.  
Test data: username: standard_user; password: secret_sauce  
Preconditions: User logged in with username and password and is on the inventory page (/inventory.html).  
Acceptance criteria:  
AC1: Given each product item listed on the inventory page Then product has a visible "Add to cart" button.  
AC2: When user clicks the "Add to cart" button for a specific product Then single item is added to the shopping cart And the shopping cart icon in the header updates to display a badge indicating the total number of items currently in the cart (e.g., shows '1' after adding the first item).  
AC3: Given product is added to the shopping card When user clickes on cart icon Then user can see selected item  
