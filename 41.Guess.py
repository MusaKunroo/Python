import random
# answer=random.randint(1,10)
# count=0
# while count<3:
#     guess=int(input("Guess the prize number from/between 1-10:"))
#     if guess>answer:
#         print("Failed.Try a smaller number")
#     elif guess<answer:
#         print("Failed.Try a larger number")
#     elif guess==answer:
#         print("Whatta Guess!.You won the prize")  
#         break   
#     count+1
# else:
#     print("You waster all your chances!")       

# answer = random.randint(0, 100)
# required_base = random.choice([2, 8, 10, 16])  # binary/octal/decimal/hex

# while True:
#     user_guess = int(input('What is your guess? '), required_base)

#     if user_guess == answer:
#       print(f'Right! The answer is {user_guess}')
#       break
    
#     if user_guess < answer:
#       print(f'Your guess of {user_guess} is too low!')
    
#     else:
#       print(f'Your guess of {user_guess} is too high!')
def hello(name):
    return f'Hello, {name}!'
alias=hello()
print(alias)