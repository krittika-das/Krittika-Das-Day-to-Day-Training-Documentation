def prime_funct(a, b):
    while(a!=b):
        c=0
        for i in range(2, a):
            if a%i==0:
                c=c+1
        if c==0:
            print(a)
        c=0
        a=a+1

prime_funct(10,30)

