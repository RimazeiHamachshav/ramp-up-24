def loop_factorial(n):
    if isinstance(n, float) or int(n) < 0:
            print("Invalid input. Please enter a nonnegative integer.")
    n = int(n)
    if n == 0:
        return 1
    elif n > 0:
        factorial = 1
        for i in range(0, n):
            factorial *= i+1
        return factorial
def recursive_factorial(n):
    if isinstance(n, float) or int(n) < 0:
            print("Invalid input. Please enter a nonnegative integer.")
    n = int(n)
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return recursive_factorial(n-1) * n
    
if __name__ == '__main__':
    n = int(input("Enter a nonnegative integer: "))
    if n < 0:
        print("Invalid input. Please enter a nonnegative integer.")
    else:
        l = loop_factorial(n)
        r = recursive_factorial(n)
        print(f"The factorial achieved through iteration of {n} is {l}.\nThe factorial achieved through recursion of {n} is {r}.")