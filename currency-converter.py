def currency_converter(amount, exchange_rate):
    """
    Convert an amount from one currency to another.

    Args:
    - amount (float): The amount to be converted.
    - exchange_rate (float): The exchange rate between the two currencies.

    Returns:
    - float: The converted amount.
    """
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    # Display a welcome message
    print("Welcome to the Currency Converter!")

    # Get the amount to be converted
    amount = float(input("Enter the amount to convert: "))

    # Get the exchange rate
    exchange_rate = float(input("Enter the exchange rate: "))

    # Call the currency_converter function
    result = currency_converter(amount, exchange_rate)

    # Display the result
    print(f"The converted amount is: {result}")

if __name__ == "__main__":
    # Run the main function
    main()
