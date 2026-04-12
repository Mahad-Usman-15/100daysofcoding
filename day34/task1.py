# Currency Converter
# Write a Python program that converts an amount from one currency to another. The program should prompt the user for the amount,
# the source currency, and the target currency. Use a predefined exchange rate for the conversion.
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
    "PKR_to_GBP": 0.0028
}

currencies = ["PKR","INR","USD","GBP"]
print(f"Currencies:{currencies}")
useramount=float(input('Enter the amount:'))
source=input("Enter the currency you want to convert:").upper()
destination=input("Enter the currency you want to get:").upper()
pair=f"{source}_to_{destination}"
if pair in conversion_rates:   
 print(f"Converted Amount={conversion_rates[f"{source}_to_{destination}"]*useramount} {destination}")
else:
 print("Inavalid Currency") 
 
    
 










