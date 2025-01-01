"""
Two friends playing this game with below rules.
fizz - Number is divided by 3
fuzz - Number is divided by 5
fizz, fuzz - Number is divided by 3 and 5 both.
"""

for i in range(1, 20):
    skip = True
    if i % 3 == 0:
        print("fizz", end=", ")
        skip = False
    if i % 5 == 0:
        print("buzz", end=", ")
        skip = False
    if skip:
        print(i, end=", ")

    print()
