user_input = int(input("enter your height: "))
bill = 0

if user_input >= 120:
    print("You can ride ")
    age = int(input("Enter your age: "))
    if age <12:
        bill = 12
        print("Child ticket is $12")
    elif age <=18:
        bill = 20
        print("adult ticket is $20")    
    else:
        bill = 50
        print("adult tickets are $50")  
    photo_package = input("do you want to take photos? yes or no: ")  
    if photo_package == "yes":
        bill += 3
    print(f"Yor final bill is {bill}")

else:
    print("sorry you cant allow to ride :(")                     