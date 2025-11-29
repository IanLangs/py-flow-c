from re import sub, Pattern, compile as recom, DOTALL
class sentence:
    def __init__(self, flowcs:tuple|list, cs:tuple|list):
        self.sentences = {fc:c for fc, c in zip(flowcs, cs)}
    def replace(self, code:str)->str:
        for fc, c in self.sentences.items():
            if isinstance(fc, Pattern):
                code = fc.sub(c, code)
            code = sub(fc, c, code)
        return code
sentences = {r"//.*":"", recom(r"\"\"\"[^\"]*\"\"\"", flags=DOTALL):""}
fc, c = [], []
for fcs, cs in sentences.items():
    fc.append(fcs)
    c.append(cs)
def all(code):
    sentences = sentence(fc, c)
    return sentences.replace(code)
    