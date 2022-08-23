import re
FOUND_METHODS = []
FOUND_TYPES = []
with open('input4.txt', 'r') as f:
    lines = f.readlines() #* Get all lines
    # print(lines)
    lines = [line.strip() for line in lines] #* Remove new lines 
    # print(lines)
    lines = [line for line in lines if not line.startswith("#")] #* Remove comments
    lines = [line for line in lines if line] #* Remove empty lines
    # print(lines)    
    print("Methods:")
    regex = r"(public|private|protected).(static)?.?(int|void|double|string).(.*)"
    for line in lines:
        return_type = ""
        if re.match(regex, line):
            
            method = re.match(regex, line).group(4)
            return_type = re.match(regex, line).group(3)
            if method not in FOUND_METHODS and "main" not in method:
                FOUND_METHODS.append(method)
                FOUND_TYPES.append(return_type)
            # print(re.match(regex, line).group(4),end=", ")   
            # print("return type:", re.match(regex, line).group(3)) 
    
    for i in range(len(FOUND_METHODS)):
        print(FOUND_METHODS[i],", return type: ",FOUND_TYPES[i])
        