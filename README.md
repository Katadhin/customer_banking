#### Project Title
**Customer Banking System with Login**

#### Introduction
Welcome to the Customer Banking System, a Python-based application designed for educational purposes. This project simulates a basic banking system allowing users to create savings and CD accounts, calculate interest, and update balances. It features a simple login mechanism for user authentication.

#### Features
- **User Authentication**: Basic login system with username and password.
- **Create Savings and CD Accounts**: Users can open new savings and CD accounts.
- **Calculate Interest**: Automatically calculate interest over a given period.
- **Update Account Balances**: Reflect interest earnings in updated account balances.
- **User-friendly Interaction**: Easy-to-navigate command-line interface for all banking operations.

#### Technologies Used
- **Python**: The entire application is written in Python.
- No external libraries or frameworks are used.

#### Setup and Installation
1. **Prerequisites**: Ensure you have Python 3.x installed on your computer.
2. **Download**: Clone the repository or download the source code.
   ```
   git clone 
   ```
3. **Navigate to the Project Directory**:
   ```
   cd customer-banking
   ```

#### How to Run the Program
1. **Start the Program**:
   ```
   python main.py
   ```
2. **Login**: Use one of the following credentials:
   - Username: `user1`, Password: `password1`
   - Username: `user2`, Password: `password2`
3. **Follow On-screen Instructions**: Navigate through the menu to create accounts and perform other operations.

#### Example Usage
```python
# After logging in successfully, choose to create a Savings or CD Account.
# Enter the required account details when prompted.
```

#### Contributing
This project is primarily for educational purposes. However, suggestions and improvements are welcome. Feel free to fork the repository and submit pull requests.

#### License
This project is open-sourced under the [MIT License](LICENSE).

#### Contact Information
For support or queries, please contact me at [john@katadhin.net](mailto:john@katadhin.net).

#### Acknowledgements
Special thanks to the instructors and peers at UNC AI Bootcamp for their guidance and support throughout this project.

Note: Original Pseudocode and codeset by John Andrews
Edits by Visual Studio Code Codepilot
Refactors by ChatGPT 4.0


Original Instructions
# customer_banking - instructions

## Call the create_cd_account function and pass the variables to the function used to prompt the user from the user.

# Print out the interest earned and updated CD account balance with interest earned for the given months.

# Call the main function.

# Hints and Considerations

# Consider what you've learned so far. You’ve learned how to create and import functions, pass arguments and variables into functions, refactor code, create and import class, create class methods, and instances.

# If you're struggling with how to start, consider creating one Python file that has all the functions first, then separate the functions into different files. Also, look back on some of the activities you did in class. Finally, you can use pseudocoding to help you write out the steps.

# Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed README.md file.

# Requirements

# Create the Savings Account Function (35 points)

# The Account class from the Accounts.py file is imported. (4 points)

# In the create_savings_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)

# The interest earned is calculated and assigned to a variable. (4 points)

# The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)

# The updated balance is passed to the set balance method using the instance of the Account class. (6 points)

# The interest earned is passed to the set balance method using the instance of the Account class. (6 points)

# The updated balance and interest earned are returned by the function. (5 points)

# Create the CD Account Function (35 points)

# The Account class from the Accounts.py file is imported. (4 points)

# In the create_cd_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)

# The interest earned is calculated and assigned to a variable. (4 points)

# The CD account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)

# The updated balance is passed to the set balance method using the instance of the Account class. (6 points)

# The interest earned is passed to the set balance method using the instance of the Account class. (6 points)

# The updated balance and interest earned are returned by the function. (5 points)

# Create the Main Function (30 points)

# The user is prompted to set the savings balance, interest rate, and months for the savings account. (8 points)

# Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)

# The user is prompted to set the savings balance, interest rate, and months for the CD account. (8 points)

# Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)

# The main function is called to run the program. (2 points)