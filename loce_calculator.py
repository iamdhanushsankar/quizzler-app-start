print("Love Calculator")

male = input("Enter  the name of the first male: ")
female = input ("Enter the name of the female: ")
love = male + female

t = love.count("t")
r = love.count("r")
u = love.count("u")
e = love.count("e")

first = t + r + u + e

L = love.count("l")
o = love.count("o")
v = love.count("v")
e = love.count("e")

second= L + o + v + e

score = int(str(first) + str(second))

if (score < 10) or (score > 90) :
    print(f"Your score is {score},you go together like coke and mentos ")
elif  (score >= 40 ) and (score <= 50):
   print(f"Your score is {score} , you are alien lovers!")
else:
    print(f"your score is {score}")
