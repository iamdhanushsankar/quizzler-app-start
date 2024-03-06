target = 100 
for numer in range(1, target+1):
    if numer % 3 == 0 and numer % 5 == 0:
        print("FizzBuzz")
    elif numer % 3 == 0:
        print("fizz")
    elif numer % 5 == 0:
        print("buzz")
    else:
        print(numer)                          