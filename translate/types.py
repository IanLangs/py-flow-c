
from re import Match, sub
def primitive(code:str) -> str:
    def string(m:Match) -> str:
        r"""str"""
        return "char*"
    def number(m:Match) -> str:
        r"""(int|float)"""
        return "int" if m.group(1) == "int" else "double"
    def Nonetype(m:Match) -> str:
        r"""None"""
        return "void"
    def func(m:Match) -> str:
        r"""fn"""
        return ""
    for fn in (string, number, Nonetype, func):
        code = sub(fn.__doc__, fn, code)
    return code
def all(code):
    code = primitive(code)
    return code