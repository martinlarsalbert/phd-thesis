import re
import os.path

def convert_references(s:str)-> str:
    
    s_latex = str(s)
    
    for result in re.finditer(r"\[\[\@([^\]]+)]]",s):
        
        ref_latex = fr"\cite{{{result.group(1)}}}"
        
        s_latex = s_latex.replace(result.group(0),ref_latex)

    return s_latex
    
    
if __name__ == '__main__':
    
    with open("literature_review.md", encoding="utf8") as file:
        s = file.read()
    
    s_latex = convert_references(s=s)
    
    save_path = os.path.join("kappa","")     
    with open("./kappa/literature_review_obsidian.tex", encoding="utf8", mode='w') as file:
        file.write(s_latex)