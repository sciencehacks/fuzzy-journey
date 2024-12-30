result=0
def math(result):
    b,c=map(str,input('then :').split())   
    if b=='+':
            result=result+float(c)
    elif b=='-':
            result=result-float(c)
    elif b=='*':
            result=result*float(c)
    elif b=='/':
            result=result/float(c)
    print(result)    
for i in range(100):
    if i==0:
        a,b,c=map(str,input('enter the math (with space) :').split())
        if b=='+':
            result=float(a)+float(c)
        elif b=='-':
            result=float(a)-float(c)
        elif b=='*':
            result=float(a)*float(c)
        elif b=='/':
            result=float(a)/float(c)
        print (result) 
    else:
        d=input('Do you want to continue [y/n]:')
        if d=="y":
               math()
        else:
            break
        