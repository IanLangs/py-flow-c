def all(code):
    if "fn None init()" not in code:
        code += """
fn None init() {
    pass
}
"""

    if "fn None tick()" not in code:
        code += """
fn None tick() {
    pass
}   
"""
    if "fn int main(" not in code:
        code += """
fn int main() {
    init();
    for(;;) {
        tick();
    }
    return 0;
}
"""
    if "pass" in code:
        code = "#define pass (void)0\n"  + code
    
    if "print(" in code:
        code = """#include <stdio.h>
fn None print(str txt){
    printf("%s\\n", txt);
}
""" + code
    return code