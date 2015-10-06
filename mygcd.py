def gcd (a,b):
    if (not ( isinstance(a,int) or isinstance(a,long))):
        return(-1)
    if (not ( isinstance(b, int) or isinstance(b,long))):
        return(-1)
    if ((a==0) or (b==0)):
        return(-1)
    while(1>0):
        if (b==0):
            return(a)
        a = a%b
        if (a==0):
            return(b)
        b=b%a
