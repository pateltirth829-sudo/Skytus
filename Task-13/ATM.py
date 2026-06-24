balance = 10000

amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal Successful")
    print("Remaining Balance =", balance - amount)
else:
    print("Insufficient Balance")