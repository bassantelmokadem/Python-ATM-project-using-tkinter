# Python-ATM-project-using-tkinter

This project is a simple user login system implemented using Python and Tkinter GUI library. It allows users to log in with their account number and password. The project uses a predefined dictionary named "users" to store user information, including their name, account number, and balance.

Upon successful login, the user is presented with a main window that offers several options:
1. Cash Withdraw: Allows the user to withdraw a desired amount of money from their account, subject to certain conditions such as withdrawal limit and available balance.
2. Balance Inquiry: Displays the user's account name and current balance.
3. Password Change: Enables the user to change their account password by entering a new password twice.
4. Fawry Service: Simulates a service for charging mobile phone credit. It prompts the user to enter the phone number and the desired charge amount, deducting the amount from the user's balance.

The project also includes error handling for scenarios such as entering an incorrect account number or password. Additionally, there is a mechanism to lock an account if the wrong password is entered multiple times.

Overall, this project demonstrates the basic functionality of a user login system with some banking operations using Python and Tkinter.
