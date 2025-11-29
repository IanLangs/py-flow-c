def nomain(code):
    if "pass" in code:
        code = "#define pass (void)0\n"  + code
    
    if "print(" in code:
        code = "#include <stdio.h>\nfn None print(str txt){\n\tprintf(\"%s\\n\", txt);\n}\n" + code
    return code

def all(code):
    if not ("fn None init()" not in code and "fn None tick()" not in code):
        if "fn None init()" not in code:
            code += "fn None init() {\n\tpass\n}"

        if "fn None tick()" not in code:
            code += "fn None tick() {\npass\n}"
            
        if "fn int main(" not in code:
            code += "fn int main() {\ninit();\n\tfor(;;) {\n\t\ttick();\n}\n\treturn 0;\n}"
    code = nomain(code)
    return code