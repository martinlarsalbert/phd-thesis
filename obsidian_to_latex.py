import re
import os.path

replacements = {
}

rename_references = {
    "chenOnlineModelingPrediction2023a":"chenOnlineModelingPrediction2023",
    
}


def convert_references(s:str)-> str:
    
    s_latex = str(s)
    
    for result in re.finditer(r"\[\[\@([^\]]+)]]",s):
        
        reference = rename_references.get(result.group(1),result.group(1))
        
        ref_latex = fr"\cite{{{reference}}}"
        
        s_latex = s_latex.replace(result.group(0),ref_latex)

    return s_latex
    
def remove_links(s:str)->str:
    
    s_latex = str(s)
    
    for result in re.finditer(r"\[\[([^\]]+)]]",s):
                
        s_latex = s_latex.replace(result.group(0),result.group(1))

    return s_latex

def remove_highlight(s:str)->str:
    
    s_latex = str(s)
    
    for result in re.finditer(r"\=\=([^\=]+)==",s):
                
        s_latex = s_latex.replace(result.group(0),result.group(1))

    return s_latex

def convert_quotes(s:str)->str:
    
    s_latex = str(s)
    
    for result in re.finditer(r'\"([^\"]+)"',s):
        
        quote_latex = fr"\say{{{result.group(1)}}}"
        
        s_latex = s_latex.replace(result.group(0),quote_latex)

    return s_latex

def convert_headings(s:str)->str:
    
    s_latex = str(s)
    
    for result in re.finditer('#+ *(.+)',s):
        
        heading_latex = fr"\subsection{{{result.group(1)}}}"
        
        s_latex = s_latex.replace(result.group(0),heading_latex)

    return s_latex

    
if __name__ == '__main__':
    
    with open("literature_review.md", encoding="utf8") as file:
        s = file.read()
    
    s_latex = convert_references(s=s)
    s_latex = remove_links(s=s_latex)
    s_latex = remove_highlight(s=s_latex)
    s_latex = convert_quotes(s=s_latex)
    s_latex = convert_headings(s=s_latex)
    
    save_path = os.path.join("kappa","")     
    with open("./kappa/literature_review_obsidian.tex", encoding="utf8", mode='w') as file:
        file.write(s_latex)