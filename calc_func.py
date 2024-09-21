print("\033[1mThese are the simple Math Functions\033[0m")
def add_num(a, b):
    return a + b
print(f"Addition: a + b = ",add_num(10, 5))


def sub_num(a, b):
    return a - b
print(f"Subtraction: a - b = ", sub_num(10, 5))

def mul_num(a, b):
    return a * b
print("Multiplication: a * b = ", mul_num(10, 5))

def div_num(a, b):
    return a / b
print("Division: a / b = ", div_num(10, 5))


print("\033[1mFor Printing of Table 2\033[0m")
for x in range(1,11):
    print(f"\n 2 x {x} = {x*2}")
print("\n")
print("\033[1mFor Printing of Table 7\033[0m")
for x in range(1,11):
    print(f"\n 7 x {x} = {x*7}")
print("\n")
print("\033[1mFor Printing of Table 11\033[0m")
for x in range(1,11):
    print(f"\n 11 x {x} = {x*11}")