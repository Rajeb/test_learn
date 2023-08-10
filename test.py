def manipulate_strings(a,b, c ):

    def inner(s):
        s=s.lower()
        print(s)
        return s[::-1]
        

    return inner(a), inner(b), inner(c)
a="HELLO"
b="WORD"
c = "TO"
print(manipulate_strings(a,b,c))  
    