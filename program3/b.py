 #Handle Divided by Zero Exception
try:
    n = int(input("Enter the value of n: "))
    d = int(input("Enter the value of d: "))
    c = int(input("Enter the value of c: "))
    q = n / (d - c)
except ZeroDivisionError:
    print("Division by Zero!")
except ValueError:
    print("Invalid integer input.")
else:
    print("Quotient:", q)
# ...existing code...