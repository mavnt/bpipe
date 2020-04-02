import builtins
import functools
from typing import Iterable, Union


class bpipe(object):
    def __init__(
        self,
        function_,
        filter_map_lambda_reduce=None,
        enumerate_start=None,
        eval_args=None,
        int_base=None,
        zip_other=None,
    ):
        self.function_ = function_
        self.filter_map_lambda_reduce = filter_map_lambda_reduce
        self.enumerate_start = enumerate_start
        self.eval_args = eval_args
        self.int_base = int_base
        self.zip_other = zip_other

    def __ror__(self, other):
        if self.filter_map_lambda_reduce is not None:
            return self.function_(self.filter_map_lambda_reduce, other)
        if self.enumerate_start is not None:
            return self.function_(other, self.enumerate_start)
        if self.eval_args is not None:
            return self.function_(other, *self.eval_args)
        if self.int_base is not None:
            return self.function_(other, self.int_base)
        if self.zip_other is not None:
            return self.function_(other, self.zip_other)
        return self.function_(other)

    def __rrshift__(self, other):
        return self.__ror__(other)


def abs(x: Union[int, float, complex] = None):
    if x is None:
        return bpipe(abs)
    else:
        return builtins.abs(x)


assert abs(-3) == -3 | abs()


def all(x: Iterable = None):
    if x is None:
        return bpipe(all)
    else:
        return builtins.all(x)


assert all([True, True, False]) == [True, True, False] | all()


def any(x: Iterable = None):
    if x is None:
        return bpipe(any)
    else:
        return builtins.any(x)


assert any([True, True, False]) == [True, True, False] | any()


def ascii(x=None):
    if x is None:
        return bpipe(ascii)
    else:
        return builtins.ascii(x)


assert ascii("hello") == "hello" | ascii()


def bin(x=None):
    if x is None:
        return bpipe(bin)
    else:
        return builtins.bin(x)


assert bin(2) == 2 | bin()


def bool(x=None):
    if x is None:
        return bpipe(bool)
    else:
        return builtins.bool(x)


assert bool(1) == 1 | bool()


# breakpoint - skipped
# bytearray - skipped
# bytes - skipped


def callable(x=None):
    if x is None:
        return bpipe(callable)
    else:
        return builtins.callable(x)


assert callable(print) == print | callable()


def chr(x: int = None):
    if x is None:
        return bpipe(chr)
    else:
        return builtins.chr(x)


assert chr(10) == 10 | chr()


# classmethod - skipped
# compile - skipped
# complex - skipped
# delattr - skipped
# dir - skipped
# divmod - skipped


def enumerate(iterable=None, start=None):
    if iterable is None and start is None:
        return bpipe(enumerate, enumerate_start=0)
    if iterable is None and start is not None:
        return bpipe(enumerate, enumerate_start=start)
    if iterable is not None:
        if start is None:
            return builtins.enumerate(iterable, start=0)
        return builtins.enumerate(iterable, start=start)


assert list(range(100) | enumerate()) == list(enumerate(range(100)))
assert list(range(100) | enumerate(start=3)) == list(enumerate(range(100), start=3))


# TODO: check args
def eval(expression=None, *args):
    if expression is not None:
        return builtins.eval(expression, *args)
    else:
        return bpipe(eval, eval_args=args)


assert "2+2" | eval() == 4 == eval("2+2")


# exec - skipped


def filter(*args):
    if len(args) == 2:
        return builtins.filter(*args)
    elif len(args) == 1 and builtins.callable(args[0]):
        return bpipe(filter, filter_map_lambda_reduce=args[0])


assert list(filter(lambda x: x % 2 == 0, range(100))) == list(
    range(100) | filter(lambda x: x % 2 == 0)
)


def float(x=None):
    if x is None:
        return bpipe(float)
    else:
        return builtins.float(x)


assert float(3) == 3 | float()


def frozenset(x=None):
    if x is None:
        return bpipe(frozenset)
    else:
        return builtins.frozenset(x)


assert frozenset(range(100)) == range(100) | frozenset()


# getattr - skipped
# globals - skipped
# hasattr - skipped


def hash(x=None):
    if x is None:
        return bpipe(hash)
    else:
        return builtins.hash(x)


assert hash(1) == 1 | hash()


def hex(x=None):
    if x is None:
        return bpipe(hex)
    else:
        return builtins.hex(x)


assert hex(1) == 1 | hex()


def id(x=None):
    if x is None:
        return bpipe(id)
    else:
        return builtins.id(x)


assert id(hex) == hex | id()


# input - skipped


def int(x=None, base=None):
    if x is None:
        if base is None:
            return bpipe(int)
        else:
            return bpipe(int, int_base=base)
    else:
        if base is None:
            return builtins.int(x)
        else:
            return builtins.int(x, base=base)


assert int("3") == "3" | int()
assert int("10", base=2) == "10" | int(base=2) == 2
assert int(3) == 3 | int()


# isinstance - skipped
# issubclass - skipped
# iter - skipped


def len(x=None):
    if x is None:
        return bpipe(len)
    else:
        return builtins.len(x)


assert len(list(range(100))) == list(range(100)) | len()


def list(x=None):
    if x is None:
        return bpipe(list)
    else:
        return builtins.list(x)


def map(*args):
    if len(args) == 2:
        return builtins.map(*args)
    elif len(args) == 1 and builtins.callable(args[0]):
        return bpipe(map, filter_map_lambda_reduce=args[0])


assert list(map(lambda x: x % 2 == 0, range(100))) == list(
    range(100) | map(lambda x: x % 2 == 0)
)


def max(*args):
    if len(args) == 0:
        return bpipe(max)
    else:
        return builtins.max(*args)


def min(*args):
    if len(args) == 0:
        return bpipe(min)
    else:
        return builtins.min(*args)


_a = [1, 2, 3, 4, 5]
assert max(_a) == _a | max() == 5
assert min(_a) == _a | min() == 1


# next - skipped
# object - skipped


def oct(x=None):
    if x is None:
        return bpipe(oct)
    else:
        return builtins.oct(x)


assert oct(3) == 3 | oct()


# object - skipped
# open - skipped


def ord(x=None):
    if x is None:
        return bpipe(ord)
    else:
        return builtins.ord(x)


assert ord("c") == "c" | ord()


# pow - skipped
# print - skipped
# property - skipped
# range - skipped
# repr - skipped


def reversed(x=None):
    if x is None:
        return bpipe(reversed)
    else:
        return builtins.reversed(x)


assert list(reversed(_a)) == _a | reversed() | list()


# round - skipped


def set(x=None):
    if x is None:
        return bpipe(set)
    else:
        return builtins.set(x)


# setattr - skipped
# slice - skipped


def sorted(*args):
    if len(args) == 0:
        return bpipe(sorted)
    else:
        return builtins.sorted(*args)


# staticmethod - skipped


def str(x=None):
    if x is None:
        return bpipe(str)
    else:
        return builtins.str(x)


def sum(*args):
    if len(args) == 0:
        return bpipe(sum)
    else:
        return builtins.sum(*args)


# super - skipped


def tuple(x=None):
    if x is None:
        return bpipe(tuple)
    else:
        return builtins.tuple(x)


def type(x=None):
    if x is None:
        return bpipe(type)
    else:
        return builtins.type(x)


# vars - skipped


def zip(*args):
    if len(args) == 1:
        return bpipe(zip, zip_other=args[0])
    else:
        return builtins.zip(*args)


_a, _b = [1, 2], [11, 22]
assert list(zip(_a, _b)) == _a | zip(_b) | list()
assert list(zip(_a, _b)) == _a >> zip(_b) >> list()


# extra
def reduce(*args):
    if len(args) == 1:
        return bpipe(reduce, filter_map_lambda_reduce=args[0])
    else:
        return functools.reduce(*args)


assert (
    reduce(lambda x, y: x + y, [1, 2, 3])
    == 6
    == [1, 2, 3] >> reduce(lambda x, y: x + y)
)


def main():
    pass


if __name__ == "__main__":
    main()
