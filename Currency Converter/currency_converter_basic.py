# Code by amotef@gmail.com

# Currency Converter - Basic

# First : pip install forex-python
from forex_python.converter import CurrencyRates
# forex-python: Forex Python is a Free Foreign exchange rates and currency conversion.

c = CurrencyRates()
# c.get_rates('USD')
amount = int(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(amount, "", from_currency, " To ", to_currency, "is:")
result = c.convert(from_currency, to_currency, amount)
# print(result)
print(round(result, 3))


# Output:
# Enter the amount: 1
# From Currency: USD
# To Currency: EUR
# 1  USD  To  EUR is:
# 0.982
