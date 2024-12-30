result=0
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
        elif a=='y':
            break
        print (result) 
    else:
        b,c=map(str,input('then :').split())   
        if b=='+':
            result=result+float(c)
        elif b=='-':
            result=result-float(c)
        elif b=='*':
            result=result*float(c)
        elif b=='/':
            result=result/float(c)
        elif a=='y':
            break
        print(result)