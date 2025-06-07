import time

def lower_triangular(n):
    print("\nLower Triangular Pattern: ")
    for i in range(1, n+1):
        for j in range(i):
            print("* ", end='', flush=True)
            time.sleep(0.1)
        print()

def upper_triangular(n):
    print("\nUpper Triangular Pattern: ")
    for i in range(n, 0, -1):
        print("  " * (n-i), end='', flush=True)
        for j in range(i):
            print("* ", end='', flush=True)
            time.sleep(0.1)
        print()

def pyramid(n):
    print("\nPyramid Pattern: ")
    for i in range(1, n+1):
        print(" " * (n-i), end='', flush=True)
        for j in range(i):
            print("* ", end='', flush=True)
            time.sleep(0.1)
        print()

def main():
    print("Python star pattern generator!!")
    n = int(input("Enter the number of rows: "))

    print("\nChoose a pattern: ")
    print("1. Lower Triangular")
    print("2. Upper Triangular")
    print("3. Pyramid")

    choice = int(input("\nEnter your choice (1/2/3): "))

    if choice==1:
        lower_triangular(n)
    elif choice==2:
        upper_triangular(n)
    elif choice==3:
        pyramid(n)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()