import re 
regex = "[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)"
var = "1.0"

j = re.match("[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)", str(var))
print(j)