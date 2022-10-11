# Create a function that calculate the number are multiples of 3, multiples of 5 or both.(check Fizz, Buzz or FizzBuzz)
# 
def FizzBuzzCheck(num1):
    if(num1 %15 ==0):
        # check the number if it is FizzBuzz first
        print("FizzBuzz")
        # output FizzBuzz
    elif(num1 %3 ==0):
        # check the number if it is Fizz
        print("Fizz")
        # output Fizz
    elif(num1 %5 ==0):
        # check the number if it is Buzz
        print("Buzz")
        # output Buzz
    else:print(num1)
        # if none of above,then out the number

for num in range(1,101):
    # Creat a loop from 1 to 100, in this case we include 100, so I set from 1 to 101, it will stop in 101 
    FizzBuzzCheck(num)
    # push the number into the function, then check and print the result
