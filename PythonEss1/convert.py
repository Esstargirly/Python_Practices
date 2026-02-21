kilometers = 12.25
miles = 7.38

miles_to_kilometers = 1.60934 * miles
kilometers_to_miles = 0.621371 * kilometers

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


usd = 1000
naira = 1000000

usd_to_naira = 1420 * usd
naira_to_usd = 1 / 1420 * naira

print(usd, "USD is", round(usd_to_naira, 2), "Naira")
print(naira, "Naira is", round(naira_to_usd, 2), "USD")


celsius = 37
fahrenheit = 98.6

celsius_to_fahrenheit = (celsius * 9/5) + 32
fahrenheit_to_celsius = (fahrenheit - 32) * 5/9

print(celsius, "Celsius is", round(celsius_to_fahrenheit, 2), "Fahrenheit")
print(fahrenheit, "Fahrenheit is", round(fahrenheit_to_celsius, 2), "Celsius")