import translate.types as t, translate.sentences as s, translate.general as g
def all(code:str, /, modules:tuple=(g, s, t)) -> str:
    for module in modules:
        code = module.all(code)
    

    return code