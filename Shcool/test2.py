for A in range(32):
    B = True
    for x in range(32):
        if ((x&25==0) or (x&19!=0) or (x&A!=0))==0:
            B=False

    if B:
        print(A)
        break