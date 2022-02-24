"""
-l : 한 라인에 최대 글자 수 (초기값 88)

—diff : 파일을 변경하지 않고 변경되는 부분을 콘솔로 보여준다.

—color : —diff를 사용했을 때 변경점에 색을 입힌다.

example 
- black {파일명 또는 폴더명} -l 80 --diff --color
"""

from seven_dwwarfs import Grumpy, Happy, Sleepy, Bashful, Sneezy, Dopey, Doc

x = {"a": 37, "b": 42, "c": 927}

x = 123456789.123456789e1234567891111111111111

if (
    very_long_variable_name is not None
    and very_long_variable_name.field > 0
    or very_long_variable_name.is_debug
):
    z = "hello " + "world"
else:
    world = "world"
    a = "hello {}".format(world)
    f = rf"hello {world}"
if this and that:
    y = "hello " "world"  # FIXME: https://github.com/python/black/issues/26


class Foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


def f(a: List[int]):
    return 37 - a[42 - u : y**3]


def very_important_function(
    template: str,
    *variables,
    file: os.PathLike,
    debug: bool = False,
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        ...


# fmt: off
custom_formatting = [
    0,  1,  2,
    3,  4,  5,
    6,  7,  8,
]
# fmt: on
regular_formatting = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]
