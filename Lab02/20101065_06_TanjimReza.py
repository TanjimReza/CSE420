""" 
    Name: Tanjim Reza
    Student ID: 20101065
    Course: CSE420 - Compiler Design
    Assignment: Assignment 2
"""
zvalid_tld = ['.com', '.net', '.org', '.edu', '.gov', '.mil', '.int', '.io', '.co', '.bd','.ac.bd','.gov.bd','.com.bd',
              '.net.bd','.org.bd','.edu.bd','.mil.bd','.int.bd','.io.bd','.co.bd','.ac.uk','.gov.uk','.uk','.ac.in',
              '.gov.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae',
              '.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw',
              '.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr',
              '.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in',
              '.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il',
              '.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th','.ac.tw','.tw','.ac.cn','.cn',
              '.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.ac.kr','.kr','.ac.th','.th',
              '.ac.tw','.tw','.ac.cn','.cn','.ac.ae','.ae','.ac.il','.il','.ac.uk','.uk','.ac.in','.in','.ac.jp','.jp','.me']
zspecial_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', 
                      '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', '?', '~', 
                      '`', '.', ',', '/', '\\']
# import from input file 
 
def EmailChecker(email):
        if email.count('@') <= 1:
            if email.find('.') != -1:
                if email.startswith('@') == False and email.endswith('@') == False and email.startswith('.') == False and email.endswith('.') == False:
                    # if starts with digit 
                    if email[0].isdigit() == False:
                        if email[0] not in zspecial_characters:
                            if email[-1] not in zspecial_characters:
                                after_at = email[email.find('@'):]
                                if after_at.find('.') != -1:
                                        return True

        else: 
            return False 
def WebAddressChecker(address):
    if address.startswith('www') or address.startswith('WWW'):
        if address.count('.') >= 2:
            if address[address.find('.')+1:][0] not in zspecial_characters:
                if any(address.endswith(tld) for tld in zvalid_tld if address.count(tld) == 1):
                    return True
                     
    else:
        return False


with open('input.txt', 'r') as f:
    lines = f.readlines() #* Get all lines
    # print(lines)
    lines = [line.strip() for line in lines] #* Remove new lines 
    # print(lines)
    lines = [line for line in lines if not line.startswith("#")] #* Remove comments
    lines = [line for line in lines if line] #* Remove empty lines
    lines.pop(0)
    
    for i in range(1,len(lines)+1):  
        line = lines[i-1]
        if EmailChecker(line):
            print(f"Email, {i}")
            
        elif WebAddressChecker(line):
            print(f"Web, {i}")
            
        else: 
            print(f"Neither, {i}")

 
  