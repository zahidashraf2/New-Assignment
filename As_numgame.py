sortedprint(f"\nHello {user_name}! Lets explore your favorite numbers:")
for num in numbers:
    if num % 2 ==0:
        print(f"The number {num} is even number.")
    else:
        print(f"The number {num} is odd number.")
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num**2})")
sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is {sum}")
is_prime = True
if sum <= 1:
    is_prime = False
for x in range(2, sum):
    if sum % x ==0:
        is_prime = False
if is_prime:
    print(f"Wow! The number {sum} is a prime number.")
else:
    print(f"Great!! The {sum} is not a prime number. ")
