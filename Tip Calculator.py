print("Welome to the tip calculator!")
bill = float(input("Waht was the total bill amout?$"))
tip =int( input("How much tip do you like to give? 10,12,15?"))
people = int(input("How many people do you want to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person,2)
print(f"Each person should pay ${final_amount}")
