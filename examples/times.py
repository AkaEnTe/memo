import timeit
from memo import *

def factorial(n):
    if ( n==0 ):
        return 1
    else:
        return n*factorial(n-1)

memoizated_factorial        = Memoizator(factorial)
custom_memoizated_factorial = CustomMemoizator(factorial)
copy_memoizated_factorial   = CopyMemoizator(factorial)


if __name__=="__main__":
    n = 30
    times = 10_000_000
    #TODO: refactor printing the results
    print("Factorial time:        " + str(timeit.timeit(f"factorial({n})", setup="from __main__ import factorial", number=times))[0:6])
    print("Memoizated time:       " + str(timeit.timeit(f"memoizated_factorial({n})", setup="from __main__ import memoizated_factorial", number=times))[0:6])
    print("CustomMemoizated time: " + str(timeit.timeit(f"custom_memoizated_factorial({n})", setup="from __main__ import custom_memoizated_factorial", number=times))[0:6])
    print("CopyMemoizated time:   " + str(timeit.timeit(f"copy_memoizated_factorial({n})", setup="from __main__ import copy_memoizated_factorial", number=times))[0:6])

