import re

with open('input4.txt', 'r') as f:
    lines = f.readlines() #* Get all lines
    # print(lines)
    lines = [line.strip() for line in lines] #* Remove new lines 
    # print(lines)
    lines = [line for line in lines if not line.startswith("#")] #* Remove comments
    lines = [line for line in lines if line] #* Remove empty lines
    # print(lines)    

    regex = r"(public|private|protected).(static)?.?(int|void|double|string).(.*)"
    for line in lines:
        return_type = ""
        if re.match(regex, line):         
            print("Return type:", re.match(regex, line).group(3))