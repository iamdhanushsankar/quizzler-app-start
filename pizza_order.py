print("Thank you for choosing Python Pzza delivery!")
size = input("what size do you want? (S, M or L): ")
add_toppins = input("do you want pepperoni ? yes or no ?")
extra_cheese = input("do you want extra cheese  ? yes or no ?")
prize = 0

if size == "L":
    prize =  15.99
elif size == "M":
    prize = 7.99
elif size == "S":
    prize = 3.99

if  add_toppins == "yes" :
    prize += 4.99

    
if  extra_cheese == "yes":
    prize += 1.99
else:
    pass

print(f"Your total cost is: {prize}" )
