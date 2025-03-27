ID: ST_SORT  
Title: As a user, I want to sort products by price I can find affordable items  
Test data: username: standard_user; password: secret_sauce  
Preconditions: User logged in with username and password and is on the inventory page (/inventory.html).  
Acceptance criteria:  
AC1: When sort dropdown is pressed Then the dropdown contains options: "Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)".  
AC2: Given dropdown is pressed When selecting "Price (low to high)" Then products are sorted by price, lowest first.  
AC3: Given dropdown is pressed When selecting "Price (high to low)" Then products are sorted by price, highest first.  

