### Memo

A simple, lightweight memoization implementation.

This module is made for educational purpouses.

### Implements:

- Memoizator
- CustomMemoizator
- CopyMemoizator

All 3 classes can be used as decorators as shown in the examples.

### TODOs:

- [X] Create decorators for memoization
- [X] Documentation
- [X] Testing

### WARNING:

For recursive functions the implementation seems to fail cacheing the recursive calls and only the first call is cached.

This implementation is still usefull for situations where a function is called multiple times with the same arguments.

### References:
- Memoization:
    - https://en.wikipedia.org/wiki/Memoization
- Factorial:
    - https://en.wikipedia.org/wiki/Factorial
- Make a class callable:
    - https://stackoverflow.com/questions/15719172/overload-operator-in-python
- Copy module:
    - https://docs.python.org/3/library/copy.html

