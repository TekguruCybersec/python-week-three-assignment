import sys

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    try:
        original_price_str = input("Please enter the original price of the item: ")
        original_price = float(original_price_str)

        discount_percentage_str = input("Please enter the discount percentage: ")
        discount_percentage = float(discount_percentage_str)

        final_price = calculate_discount(original_price, discount_percentage)

        if final_price < original_price:
            print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
        else:
            print("No discount was applied because the percentage was less than 20%.")
            print(f"The original price remains: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for both the price and the discount.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
