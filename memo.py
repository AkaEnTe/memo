import copy

"""
A base class implementing the main memoization logic.
"""
class _BaseMemoizator:
    def __init__(self, func):
        self.cache = {}
        self.func = func

    def __call__(self, *args):
        return self._cache(*args)

    def _cache(self, *args):
        if args not in self.cache.keys():
            self.cache[args] = self.func(*args)
        return self.cache[args]


"""
The most basic Memoizator, it accepts a function and the call is propagated from the Memoizator to the function.

The Memoizator can be used as a decorator.

Examples:
    
    memoizated_func = Memoizator(func)
    memoizated_func()

    ----------------
    @Memoizator
    fun memoizated_func():
        pass

    memoizated_func()

Extended examples can be found in the examples folder.
"""
class Memoizator(_BaseMemoizator):
    def __init__(self, func):
        super().__init__(func)


"""
A Memoizator which return a deepcopy of the cached value, it accepts a function and the call is propagated from the Memoizator to the function.

The Memoizator can be used as a decorator.

Examples:
    
    memoizated_func = CopyMemoizator(func)
    memoizated_func()

    ----------------
    @CopyMemoizator
    fun memoizated_func():
        pass

    memoizated_func()

Extended examples can be found in the examples folder.
"""
class CopyMemoizator(_BaseMemoizator):
    def __init__(self, func):
        super().__init__(func)

    def __call__(self, *args):
        return copy.deepcopy(self._cache(*args))


"""
A Memoizator which applies a custom function to the cached return , it accepts a function for memoization and another for applying to the returned value.
The call is propagated from the Memoizator to the first function.

The Memoizator can be used as a decorator.

Examples:
    
    memoizated_func = CustomMemoizator(func)
    memoizated_func()

    ----------------
    @CustomMemoizator
    fun memoizated_func():
        pass

    memoizated_func()

Extended examples can be found in the examples folder.
"""
class CustomMemoizator(_BaseMemoizator):
    def __init__(self, func, custom_func = lambda x: x):
        super().__init__(func)
        self.custom_func = custom_func

    def __call__(self, *args):
        return self.custom_func(self._cache(*args))

