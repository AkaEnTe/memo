import timeit
from memo import *

def factorial(n):
    if ( n==0 ):
        return 1
    else:
        return n*factorial(n-1)

@Memoizator
def factorial_memoizator(n):
    if ( n==0 ):
        return 1
    else:
        return n*factorial(n-1)

@CustomMemoizator
def factorial_custom_memoizator(n):
    if ( n==0 ):
        return 1
    else:
        return n*factorial(n-1)

@CopyMemoizator
def factorial_copy_memoizator(n):
    if ( n==0 ):
        return 1
    else:
        return n*factorial(n-1)

if __name__=="__main__":
    n = 30
    times = 10_000_000
    print("Factorial time:        " + str(timeit.timeit(f"factorial({n})", setup="from __main__ import factorial", number=times))[0:6])
    print("Memoizated time:       " + str(timeit.timeit(f"factorial_memoizator({n})", setup="from __main__ import factorial_memoizator", number=times))[0:6])
    print("CustomMemoizated time: " + str(timeit.timeit(f"factorial_custom_memoizator({n})", setup="from __main__ import factorial_custom_memoizator", number=times))[0:6])
    print("CopyMemoizated time:   " + str(timeit.timeit(f"factorial_copy_memoizator({n})", setup="from __main__ import factorial_copy_memoizator", number=times))[0:6])

