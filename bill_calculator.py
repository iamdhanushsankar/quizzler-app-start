#create a program that splits the bill  based on number of people and amount paid by each person
print("Welcome to the Bill Splitter!")
user_bill = float(input("enter the bill amount? $"))
user_tip =  int(input("Enter tip percentage (10, 12 or 15): "))
people = int(input("How many people are there?: "))
tip_as_percent = user_tip / 100
total_tips = tip_as_percent + user_bill
per_person = total_tips / people
final_amount = round(per_person, 2)
print(f"the soilt amount is: ${final_amount}")