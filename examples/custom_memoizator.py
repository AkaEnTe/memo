from memo import CustomMemoizator

def factorial(n):
    if ( n==0 or n==1 ):
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    f = CustomMemoizator(factorial, custom_func = lambda x: f"|{x}|")
    for i in range(10, 0, -1):
        print(f"{i}!: {f(i)}")
