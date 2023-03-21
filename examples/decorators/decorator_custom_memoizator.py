from memo import CustomMemoizator

@CustomMemoizator
def factorial(n):
    if ( n==0 ):
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    for i in range(10, 0, -1):
        print(f"{i}!: {factorial(i)}")
