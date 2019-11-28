class Myexception(Exception):
    pass 
def xyz(a,b):
    sum=a+b
    if sum<150:
        raise Myexception("Custome Exception Occured")
    else:
        return sum
a=int(input())
b=int(input())
res=xyz(a,b)
print(res)
