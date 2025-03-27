ID: ST_LOGIN  
Title: As a user I want to login into the system to see product list   
Test data: correct_username: standard_user; correct_password: secret_sauce  ; incorrect_password: password01  
Preconditions: User open main page  
Acceptance criteria:
AC1: Given correct login data After entering correct_username and correct_password in form Then user is reditected to product list page  
AC2: Given incorrect login data After entering correct_username and incorrect_password in form Then user stays on login page And user is show error message "Username and password do not match any user in this service"  
