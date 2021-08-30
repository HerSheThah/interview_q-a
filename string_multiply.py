string="a1b2c3"

i=0
while i <len(string):
    if string[i].isdigit():
        alpha=string[i-1]
        multi=""
        while i<len(string) and string[i].isdigit():
            multi += string[i]
            i+=1
        print(alpha*int(multi),end='')
    i+=1
