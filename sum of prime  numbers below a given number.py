# 10974001
# I certify that I Oduro Derrick wrote this code all by myself.

user_input = int(input("Type in a number: \n"))

def prime_checker(value):
    is_prime = False
    num_factors = 0;
    for x in range(1, value + 1):
        if value % x == 0:
            num_factors += 1
    if num_factors == 2:
            is_prime = True;
    return is_prime
    
def prime_sum(user_input):
    sum = 0;
    for x in range(1, user_input + 1):
        if prime_checker(x) == True:
            sum += x
    print(f"The sum of the prime numbers below {user_input} is {sum}.")
    
prime_sum(user_input)
