print("Welcome to the tip calculator!")
#If the bill was $150.00, split between 5 people, with 12% tip. 
total_bill = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
tip_percentage_integer = int(tip_percentage)
split_float = float(split)

tip_total = total_bill_float * (tip_percentage_integer / 100 + 1) / split_float

#150 * (12 / 100 + 1) / 5

final_amount = round(tip_total, 2)

print(f"Each person should pay ${final_amount}.")

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

