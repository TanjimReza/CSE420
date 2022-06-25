""" 
    Name: Tanjim Reza
    Student ID: 20101065
    Course: CSE420 - Compiler Design
    Assignment: Assignment 1

"""




zkeyword_list = ['if','else','while','int','float','char','return','void','main','printf','scanf']
zmath_operators = ['+','-','*','/','%','=']
# zdelimiter_list = ['(',')','[',']','{','}','.',',',';']
zlogical_operators = ['&&','||','!=', '==', '>', '<', '>=', '<=']
others = ['(',')','[',']','{','}',',',';']
output = ""
regex_abcd = r'[a-zA-Z]'

from pprint import pprint
import re 
with open('input.txt', 'r') as f:
    lines = f.readlines() #* Get all lines
    # print(lines)
    lines = [line.strip() for line in lines] #* Remove new lines 
    # print(lines)
    lines = [line for line in lines if not line.startswith("#")] #* Remove comments
    lines = [line for line in lines if line] #* Remove empty lines
    
    
    
    #!###### Keywords #######!#
    keyword_list = [] 
    for line in lines:
        for word in line.split():
            if word in zkeyword_list and word not in keyword_list:
                keyword_list.append(word)
    #!##########################!#
     #* Remove duplicates-2
    output += f"Keywords:"
    for i in keyword_list:
        output += f" {i}"
        #* remove last comma 
        if i != keyword_list[-1]:
            output += ","
    output += "\n"
    
    #!###### IDENTIFIERS #######!#
    indentifiers_list = [] #* List of variables
    for line in lines:
        if line.startswith('int') or line.startswith('float') or line.startswith('char'):
            line = line.replace(';','').replace(',','').replace('int', '').replace('float', '')
            lst = [i for i in line.split(' ') if i]
            for variable in lst:
                if variable not in indentifiers_list:
                    indentifiers_list.append(variable)
                    # indentifiers_list.append(variable) #* Add variable to list, In case I need to check for duplicate variables
    # print(indentifiers_list)
    # print(sorted(set(indentifiers_list)))
    # indentifiers_list = list(set(indentifiers_list)) #* Remove duplicates #! ORDER GETS MESSED UP 
    # # x = [indentifiers_list.append(i) for i in indentifiers_list if i not in indentifiers_list]
    # indentifiers_list = sorted(set(indentifiers_list)) #* Remove duplicates-2
    output += f"Identifiers:"
    for i in indentifiers_list:
        output += f" {i}"
        #* remove last comma 
        if i != indentifiers_list[-1]:
            output += ","
    output += "\n"
    #!##########################!#
    
    #!###### Math Operators #######!#
    math_operators_list = []
    for line in lines:
        for word in line.split():
            if word in zmath_operators and word not in math_operators_list:
                math_operators_list.append(word)
    # print(sorted(math_operators_list))
    
    output += f"Math Operators:"
    for i in sorted(math_operators_list):
        output += f" {i}"
        #* remove last comma 
        if i != math_operators_list[-1]:
            output += ","
    output += "\n"
    #!##########################!#
    
    #!###### Logical Operators #######!#
    logical_operators = []
    for line in lines:
        for word in line.split():
            if word in zlogical_operators and word not in logical_operators:
                logical_operators.append(word)
    # print(sorted(logical_operators))
    output += f"Logical Operators:"
    for i in sorted(logical_operators):
        output += f" {i}"
        #* remove last comma 
        if i != logical_operators[-1]:
            output += ","
    output += "\n"
    #!##########################!#
        
    #!###### Numerical Values #######!#
    numerical_values = []
    for line in lines:
        line = line.replace(';','').replace(',','').replace('int', '').replace('float', '')
        for word in line.split():
            #! This is very interesting, there are multiple ways to do this.
            #! 01: Converting to Float and check for errors
            #! 02: Good old regex
            regex = "[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)" 
            
            """Regex explanation:
            [+-]? : optional sign, there can be + or -
            [0-9]+ : one or more digits (0-9)
            ([.][0-9]*)? : optional decimal point and one or more digits after decimal (0-9)
            | : or operator (if the first regex fails, the second one will be used)
            [.][0-9]+ : decimal point and one or more digits, nothing before decimal
            """
            
            if re.match(regex, word):
                # print(word)
                numerical_values.append(word)
    
    # print(numerical_values)
    output += f"Numerical Values:"
    for i in numerical_values:
        output += f" {i}"
        #* remove last comma 
        if i != numerical_values[-1]:
            output += ","
    output += "\n"
    #!##########################!# 
    
    
#!###### Other Operators #######!#
    other_operators = []
    for line in lines:
        # line = line.replace(';','').replace(',','')
        for word in line:
            if word in others and word not in zkeyword_list and word not in zmath_operators \
                and word not in zlogical_operators and word not in numerical_values \
                and word not in indentifiers_list and word not in other_operators:
                    # print(word)
                    other_operators.append(word)

    output += f"Other Operators:"
    for i in other_operators:
        output += f" {i}"
        #* remove last comma 
        
    output += "\n"
    
print(output)