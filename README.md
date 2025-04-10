# Income & Expense Tracker

This application helps you to track your income and expenses. Each user can add, view, and delete their own transactions securely. Data is stored locally in separate CSV files based on each user's unique username.

## Features

- **Login**: Users must log in using a username (e.g., email address) to access their own transaction history.
- **Add Transaction**: Users can add new transactions with details such as date, type (Income/Expense), category, amount, and an optional description.
- **View Transaction History**: Users can view a list of their previous transactions with the option to delete any transaction.
- **Summary**: The app provides a summary of total income, total expense, and the current balance.

## How It Works

1. **Login**: When you first visit the app, you'll be prompted to log in using a unique username. This could be your email address or any identifier of your choice. Your transaction data will be stored in a file named `user_data_<username>.csv`.
2. **Add Transaction**: Once logged in, you can add a new income or expense by specifying the transaction details in the provided form.
3. **View & Delete Transactions**: All your previous transactions will be displayed with an option to delete any unwanted entries.
4. **View Summary**: The app will calculate and display your total income, expenses, and current balance.

## How To Run Locally

1. **Install the necessary dependencies**:
   Make sure you have Python installed. Then, you can install the required dependencies using `pip`:

   ```bash
   pip install streamlit pandas

If you want to customize the application to your needs or for other users, you can edit the following parts of the code:

Update User Login Mechanism
If you want to add more security (e.g., email/password login), you will need to:

Implement authentication (using libraries like streamlit_authenticator or Firebase for user registration).

Modify the username input logic to accept more secure credentials (such as email/password).

Update the Data Storage
Currently, the app stores data in CSV files for each user. You can modify this to:

Store data in a database (e.g., SQLite, MySQL, or MongoDB) for better scalability.

Implement user authentication via Google Firebase or similar platforms to allow multi-device access and data persistence.
