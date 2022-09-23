def isValid(s: str) -> bool:
    new_list = []
    for i in s:
        if i in ["(", "{", "["]:
            new_list.append(i)
        elif i in [")", "}", "]"] and len(new_list)==0:
            return False
        elif i == ")" and new_list[-1]=="(":
            new_list = new_list[:-1]
        elif i == "}" and new_list[-1]=="{":
            new_list = new_list[:-1]
        elif i == "]" and new_list[-1]=="[":
           new_list = new_list[:-1]
        else:
            return False
    if len(new_list) == 0:
        return True
    else:
        return False


print(isValid("(])"))
# print(isValid("{)(}"))
# print(isValid("{}"))
# print(isValid(")"))
# print(isValid("()}"))