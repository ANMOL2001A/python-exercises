initial_balance = 1000
interest=0.05
first_year_balance=(initial_balance*interest) + initial_balance
print(first_year_balance)
second_year_balance=(first_year_balance*interest) + first_year_balance
third_year_balance=(second_year_balance*interest) + second_year_balance
print(f"Balance after 3rd year : {third_year_balance}")