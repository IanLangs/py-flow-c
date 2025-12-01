
from re import Match, sub
def primitive(code:str) -> str:
    def string(m:Match) -> str:
        r"""str"""
        return "char*"
    def number(m:Match) -> str:
        r"""(int|float)"""
        return "int" if m.group(1) == "int" else "double"
    def boolean(m:Match) -> str:
        r"""(bool|true|false)"""
        return "int" if m.group(1) == "bool" else ("1" m.group(1) == "true" else "0")
    def Nonetype(m:Match) -> str:
        r"""None"""
        return "void"
    def Anypointer(m:Match) -> str:
        """AnyPointer"""
        return "void*"
    def func(m:Match) -> str:
        r"""fn"""
        return ""
    for fn in (string, number, Nonetype, func, Anypointer):
        code = sub(str(fn.__doc__), fn, code)
    return code
def all(code):
    code = primitive(code)
    return code
