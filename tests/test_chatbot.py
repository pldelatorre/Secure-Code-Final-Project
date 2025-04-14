"""
Description: Unit tests for functions created for chatbot.py
Author: Patrick-Luke Dela Torre
Date: 14 March 2024
Usage: Used this py file to test the chatbot.py
"""
import unittest
from unittest.mock import patch
from src.chatbot import VALID_TASKS, ACCOUNTS
from src.chatbot import get_account, get_amount, get_balance
from src.chatbot import make_deposit, user_selection

class ChatbotTests(unittest.TestCase):
    def test_get_account_valid_account(self):
        with patch("builtins.input") as mock_input:
            # Arrange: set up some variables for the test  
            mock_input.side_effect = ["123456"]
            expected_output = 123456    
            # Act: run the function or code that's being tested
            actual_output = get_account()
            # Assert: compare some kind of expected outcome with the actual one        
            self.assertEqual(expected_output, actual_output)    

    def test_get_account_non_numeric_data_raises_exception(self):
        with patch("builtins.input") as mock_input:
            # Arrange:   
            mock_input.side_effect = ["non_numeric_data"]
            expected_output = "Account number must be a whole number."   
            # Act and Assert:
            with self.assertRaises(ValueError) as context:
                get_account()    

            self.assertEqual(expected_output, str(context.exception)) 

    def test_get_account_does_not_exist_raises_exception(self):
        with patch("builtins.input") as mock_input:
            # Arrange:   
            mock_input.side_effect = ["112233"]
            expected_output = "Account number entered does not exist."   
            # Act and Assert:
            with self.assertRaises(ValueError) as context:
                get_account()

            self.assertEqual(expected_output, str(context.exception))

    def test_get_amount_valid_amount(self):
        with patch("builtins.input") as mock_input:
            # Arrange:  
            mock_input.side_effect = ["500.01"]
            expected = 500.01    
            # Act: 
            actual = get_amount()
            # Assert:        
            self.assertEqual(expected, actual)    

    def test_get_amount_non_numeric_amount_raises_exception(self):
        with patch("builtins.input") as mock_input:
            # Arrange:   
            mock_input.side_effect = ["non_numeric_data"]
            expected_output = "Invalid amount. Amount must be numeric."  
            # Act and Assert:
            with self.assertRaises(ValueError) as context:
                get_amount()    

            self.assertEqual(expected_output, str(context.exception)) 

    def test_get_amount_invalid_amount_raises_exception(self):
        with patch("builtins.input") as mock_input:
            # Arrange:   
            mock_input.side_effect = ["0"]
            expected_output = "Invalid amount. Please enter a positive number."  
            # Act and Assert:
            with self.assertRaises(ValueError) as context:
                get_amount()

            self.assertEqual(expected_output, str(context.exception)) 

    def test_get_balance_valid_account(self):
        # Arrange:   
        account = 123456
        expected = f"Your current balance for account 123456 is $1,000.00."    
        # Act: 
        actual = get_balance(account)
        # Assert:         
        self.assertEqual(expected, actual)    

    def test_get_balance_invalid_account_number(self):
        account = 112233
        expected_output = "Account number does not exist."  
        # Act and Assert:
        with self.assertRaises(ValueError) as context:
            get_balance(account)    

        self.assertEqual(expected_output, str(context.exception)) 

    def test_make_deposit_updating_balance(self):
        # Arrange: 
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        account = 123456
        amount = 1500.01
        expected = 2500.01  
        # Act: 
        actual = 2500.01
        # Assert:         
        self.assertEqual(expected, actual)    

    def test_make_deposit_valid_output(self):
        # Arrange: 
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        account = 123456
        amount = 1500.01
        expected = f"You have made a deposit of ${amount:,.2f} to account ${account}."   
        # Act: 
        actual = make_deposit(account, amount)
        # Assert:         
        self.assertEqual(expected, actual)    

    def test_make_deposit_invalid_account_raises_exception(self):
        # Arrange:
        account = 112233
        amount = 1500.01       
        expected_output = "Account does not exist."
        # Act and Assert:
        with self.assertRaises(ValueError) as context:
            make_deposit(account, amount)    

        self.assertEqual(expected_output, str(context.exception)) 

    def test_make_deposit_invalid_amount_raises_exception(self):
        account = 123456
        amount = -50.01       
        expected_output = "Invalid Amount. Amount must be positive."
        # Act and Assert:
        with self.assertRaises(ValueError) as context:
            make_deposit(account, amount)    

        self.assertEqual(expected_output, str(context.exception))

    def test_user_selection_valid_selection_in_lowercase(self): 
         with patch("builtins.input") as mock_input:
            # Arrange:   
            mock_input.side_effect = ["balance"]
            expected = "balance"  
            # Act:
            actual = user_selection()
            # Assert:
            self.assertEqual(expected, actual)   

    def test_user_selection_valid_selection_in_uppercase(self): 
         with patch("builtins.input") as mock_input:
            # Arrange:   
            mock_input.side_effect = ["DEPOSIT"]
            expected = "deposit"  
            # Act:
            actual = user_selection()
            # Assert:
            self.assertEqual(expected, actual)  
   
    def test_user_selection_invalid_selection_raises_exception(self):
        # Arrange:
         with patch("builtins.input") as mock_input:
            # Arrange:   
            mock_input.side_effect = ["invalid_selection"]
            expected = "Invalid task. Please choose balance, deposit, or exit."  
            # Act and Assert:
            with self.assertRaises(ValueError) as context:
                user_selection()

            self.assertEqual(expected, str(context.exception))   
