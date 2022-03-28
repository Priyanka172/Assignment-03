string = 'The quick Brow Fox'
def fun(string):
    n1 = 0
    n2 = 0
    for i in string:
        if i.islower():
            n1=n1+1
        elif i.isupper():
            n2=n2+1
    print("no. of Lower case letters:", n1)
    print("no. of upper case letters:", n2)
fun(string)