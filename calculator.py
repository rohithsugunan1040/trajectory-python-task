import math

a=int(input("enter number 1 "))
b=int(input("enter number 2 "))
op=input("enter operation (+,-,*,/,//,^,%) ")
if(op=='+'):
    sum=a+b
    print("sum is ",sum)
elif(op=='-'):
    diff=a-b
    print("difference is ",diff)
elif(op=='*'):
    pdt=a*b
    print("product is ",pdt)
elif(op=='/'):
    div=a/b
    print("quotient is ",div)
elif(op=='//'):
    fd=a//b
    print("floor division of both nos gives ",fd)
elif(op=='^'):
    exp=math.pow(a,b)
    print("a^b gives ",exp)
elif(op=='%'):
    rem=a%b
    print("remainder of ",a,"and",b,"is",rem)
    
