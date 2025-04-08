import helper_funcs

# Fixed exchange rates relative to USD
# These are example rates; feel free to update them
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.91,
    'GBP': 0.78,
    'JPY': 151.2,
    'AUD': 1.52
}

# List of supported currencies
currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD']

def get_currency_choice(message):
    """
    Helper to use inq_select and return selected currency code
    """
    selection = helper_funcs.inq_select(message, *currencies)
    return currencies[selection - 1]  # selection is 1-indexed

def convert_currency(amount, from_currency, to_currency):
    """
    Convert amount from one currency to another using USD as base
    """
    usd_amount = amount / exchange_rates[from_currency]
    return usd_amount * exchange_rates[to_currency]

def main():
    print("=== Welcome to Currency Converter ===")

    # Get source currency
    from_currency = get_currency_choice("Select the currency you want to convert FROM:")

    # Get target currency
    to_currency = get_currency_choice("Select the currency you want to convert TO:")

    # Ask for the amount to convert
    try:
        amount = float(input(f"Enter amount in {from_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    # Do the conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)

    # Show the result
    print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

# Run the program
if __name__ == "__main__":
    main()
