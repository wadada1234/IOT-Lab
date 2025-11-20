# a) Print a name 'n' times, where name and n are read from standard input, using for
# and while loops.
def string_print(n: int) -> None:
    print("THE STRING IS 'Money Heist'")
    print("The string will be printed", n, "times")
    for _ in range(n):
        print("Money Heist")

if __name__ == "__main__":
    try:
        n = int(input("Enter number of times to print: "))
    except ValueError:
        print("Invalid input: please enter an integer.")
    else:
        string_print(n)
# ...existing code...