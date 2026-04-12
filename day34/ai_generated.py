# 1. Store the values of the currencies in a dict
conversion_rates = {
    "USD_to_PKR": 278.50,
    "USD_to_INR": 83.30,
    "USD_to_GBP": 0.79,
    "GBP_to_USD": 1.27,
    "GBP_to_PKR": 352.40,
    "GBP_to_INR": 105.45,
    "INR_to_USD": 0.012,
    "INR_to_PKR": 3.34,
    "INR_to_GBP": 0.0095,
    "PKR_to_USD": 0.0036,
    "PKR_to_INR": 0.30,
    "PKR_to_GBP": 0.0028,
    # Self conversions
    "USD_to_USD": 1.0,
    "PKR_to_PKR": 1.0,
    "INR_to_INR": 1.0,
    "GBP_to_GBP": 1.0
}

# 2. Ask the user to give amount, from and to currency
print("--- Currency Converter ---")
try:
    amount = float(input("Enter the amount: "))
    from_curr = input("From currency (USD, PKR, GBP, INR): ").upper()
    to_curr = input("To currency (USD, PKR, GBP, INR): ").upper()

    # Create the key to look up in the dictionary
    pair = "{0}_to_{1}".format(from_curr, to_curr)

    # 3. If the pair is in the dict give the user converted amount
    if pair in conversion_rates:
        rate = conversion_rates[pair]
        converted_amount = amount * rate
        print("Converted Amount: {0} {1}".format(converted_amount, to_curr))
    
    # Otherwise return an error
    else:
        print("Error: Invalid currency selection or conversion pair not supported.")

except ValueError:
    print("Error: Please enter a valid numerical amount.")