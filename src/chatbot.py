"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Patrick-Luke Dela Torre
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account() -> int:
    """
    Ask the user for an input of their account number and return it as
    an integer.

    Returns:
        int: valid account_number of the user.

    Raises:
        ValueError: When the account number is not numeric
        ValueError: When the account number does not exist
    """
    account_number = input("Please enter your account number: ")
    try:
        account_number = int(account_number)
    except ValueError:
        raise ValueError("Account number must be a whole number.")

    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.") 

    return account_number    

def get_amount() -> float:
    """
    Ask the user for an input for the amount to deposit and return is as
    a float.

    Returns:
        float: amount to deposit must return a float.

    Raises:
        ValueError: When the amount entered is not number
        ValueError: When the amount entered is invalid (negative or zero
        amount value)    
    """
    transaction_amount = input("Enter the transaction amount: ")
    try:
        transaction_amount = float(transaction_amount)
    except ValueError:
        raise ValueError("Invalid amount. Amount must be numeric.")
    
    if transaction_amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    
    return transaction_amount

def get_balance(account: int) -> str:

    """
    This function will retrieve the balance of a specified account.

    Argument:
        int: account number should be an integer.

    Returns:
        str: returns a string that tells user the current balance for the
        account.

    Raises:
        ValueError: When the account number does not exist            
    """

    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
         
    else:
        balance = ACCOUNTS[account]["balance"]
    
    return f"Your current balance for account {account} is ${balance:,.2f}."
    
def make_deposit(account: int, amount: float) -> str:
    """
    This function will update the balance of the specific account by adding 
    the value of the amount to be depposited to the account's balance.

    Arguments:
        int: account number should be an integer.
        float: amount should be a float.

    Returns:
        str: returns a string that tells user the current balance for the
        account after making the deposit.

    Raises:
        ValueError: When the account number does not exist
        ValueError: When the amount is less than or equal to zero        
    
    """
    if account not in ACCOUNTS:
        raise ValueError("Account does not exist.")
    else:
        deposit  = float(amount)
        if deposit <= 0:
            raise ValueError("Invalid Amount. Amount must be positive.")
        else: 
            balance = ACCOUNTS[account]["balance"]
            new_balance = balance + deposit
            ACCOUNTS[account]["balance"] = new_balance
            
    return f"You have made a deposit of ${deposit:,.2f} to account ${account}."

def user_selection() -> str:
    """
    This function is to prompt the user for their selection and if valid,
    return it.

    Returns:
        str: returns a string representing the user's selected task.

    Raises:
        ValueError: When invalid user selection is chosen.        
    """
    
    select = input("What would you like to do (balance/deposit/exit)?").lower()
    
    if select not in VALID_TASKS:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")

    return select
## GIVEN CHATBOT FUNCTIONS

## REQUIRES REVISION

def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            selection = user_selection()
            


            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        account = get_account()
                        

                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        balance = get_balance(account)
                        print(balance)                     
                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            amount = get_amount()
                            


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                    result = make_deposit(account, amount) 
                    print(result)


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")

if __name__ == "__main__":
    chatbot()
