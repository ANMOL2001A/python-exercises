price_of_new_car = int(input("Enter the cost of the new car: "))
mialage_per_gallon = int(input("Enter the mialage of car: "))
estimated_miles_per_year = int(input("Enter the estimated miles driven per year: "))
estimated_gas_price = int(input("Enter the estimated gas price: "))
price_after_5_years = int(input("Enter the estimated resale value after 5 years: "))
total_gas_cost = (estimated_miles_per_year / mialage_per_gallon) * estimated_gas_price * 5
total_cost_of_owning = price_of_new_car + total_gas_cost - price_after_5_years
print(f"Money spend on car after 5 years: {total_cost_of_owning}")
