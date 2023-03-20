import copy

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


class Memoizator(_BaseMemoizator):
    def __init__(self, func):
        super().__init__(func)


class CopyMemoizator(_BaseMemoizator):
    def __init__(self, func):
        super().__init__(func)

    def __call__(self, *args):
        return copy.deepcopy(self._cache(*args))


class CustomMemoizator(_BaseMemoizator):
    def __init__(self, func, custom_func = lambda x: x):
        super().__init__(func)
        self.custom_func = custom_func

    def __call__(self, *args):
        return self.custom_func(self._cache(*args))

