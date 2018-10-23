def yishu(m, n):
    #m为待转换的十进制数，n为机制，取值为2-16
    a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
    b=[]
    while True:
        s=int(m)//int(n)#商
        y=m%n#余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    for i in b:
        print(a[i], end='end')

if __name__ == '__main__':
    n, m = input('输入用#号隔开的进制数和数字：').split('#')
    while int(n) < 2 or int(n) > 16:
        n, m = input('输入用#号隔开的进制数和数字：').split('#')
    m = int(m)
    n = int(n)
    yishu(int(m), int(n))

