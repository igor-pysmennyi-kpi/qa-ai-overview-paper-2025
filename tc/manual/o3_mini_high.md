**Test Case 1: Successful Login**

1.  **Test Case ID and Title**

TC_ST_LOGIN_01 -- Successful Login Redirect to Product List

2.  **Test Data**

-  Username: standard_user

-  Password: secret_sauce

3.  **Preconditions**

-  User has opened the main page

4.  **Steps**

1.  Enter "standard_user" in the username field

2.  Enter "secret_sauce" in the password field

3.  Click the "Login" button

5.  **Expected Results**

-  User is redirected to the product list page

6.  **Postconditions**

-  (Optional) Logout to revert the system to its initial state

* * * * *

**Test Case 2: Unsuccessful Login**

1.  **Test Case ID and Title**

TC_ST_LOGIN_02 -- Unsuccessful Login with Error Message

2.  **Test Data**

-  Username: standard_user

-  Password: password01

3.  **Preconditions**

-  User has opened the main page

4.  **Steps**

1.  Enter "standard_user" in the username field

2.  Enter "password01" in the password field

3.  Click the "Login" button

5.  **Expected Results**

-  User remains on the login page

-  An error message is displayed: "Username and password do not match any user in this service"

6.  **Postconditions**

-  (Optional) Clear the login fields for a subsequent test run