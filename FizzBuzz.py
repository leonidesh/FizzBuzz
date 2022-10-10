def FizzBuzzCheck(num1):
    if(num1 %15 ==0):
        print("FizzBuzz")
    elif(num1 %3 ==0):
        print("Fizz")
    elif(num1 %5 ==0):
        print("Buzz")
    else:print(num1)

for num in range(1,100):
    FizzBuzzCheck(num)