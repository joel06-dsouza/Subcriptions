while True:
    try:
        t=int(input())
        while(t):
            m=0
            x, y = input().split()
            if (int(x) < int(y)):
                print(m)
            else:
                z=int(x)-int(y)
                print(z)
    except EOFError:
        break