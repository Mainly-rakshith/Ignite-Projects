# Name: Rakshith Jayakarthikeyan
# Assignment: PROG 1003 - HW3 - Making Change

while True:
    amount = int(input("How much money do you want to get change for? (0-99 cents): "))
    
    quarters = amount // 25
    amount %= 25
    dimes = amount // 10
    amount %= 10
    nickels = amount // 5
    amount %= 5
    pennies = amount

    print(f"For an amount of {quarters * 25 + dimes * 10 + nickels * 5 + pennies} cents, we will need: ")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")

    again = input("\nGo again? (y/n) ")
    if again.lower() != "y":
        break