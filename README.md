Discount Calculator
This Python script calculates an item's final price after a discount. It applies the discount only if the percentage is 20% or higher.

Usage
To use the script, run the file from your terminal and follow the prompts:

python discount_calculator.py

Example 1: Discount Applied
Please enter the original price of the item: 100
Please enter the discount percentage: 25
The final price after a 25.0% discount is: $75.00

Example 2: No Discount Applied
Please enter the original price of the item: 50
Please enter the discount percentage: 15
No discount was applied because the percentage was less than 20%.
The original price remains: $50.00

Logic
The calculate_discount function applies the discount only if it is 20% or more. Otherwise, it returns the original price. The script also includes basic error handling for invalid input.
