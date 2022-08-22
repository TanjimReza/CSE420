import re

with open("input.txt","r",encoding="utf-8") as f:
    lines = f.read()
    lines = lines.split("\n")
    n_regex = int(lines[0])
    n_expr = lines[0+n_regex]
    patterns = lines[1:n_regex+1]
    strings = lines[n_regex+2:]
    #compile the regex
    for string in strings:
        NO_MATCH = True
        for i,pattern in enumerate(patterns):
            if re.search(pattern,string):
                # print(f"YES, {pattern} matches {string}")
                NO_MATCH = False
                idx = i
                break
        if NO_MATCH:
            print("NO,0")
        else:
            print(f"YES,{idx+1}")
                

    
    
