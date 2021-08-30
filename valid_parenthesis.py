string="[(])"

di={"}":"{", "]":"[", ")":"("}
stack=[]
def parenthesis(string):
    for el in string:
        if el=="{" or el=="[" or el=="(":
            stack.append(el)
        else:
            if stack[len(stack)-1]==di[el]:
                stack.pop()
            else:
                return False

    if(len(stack)==0):
        return True
    return False

print(parenthesis(string))
