def fibbonachhi(limit):
    a, b = 1,1
    sum=0
    li=[1]
    for x in xrange(1,limit):
        a,b = b, a+b
        li.append(a)
        if a%2==0:
            sum+=a
        if a>=4000000:
            break
    print li
    return sum



if __name__ == '__main__':
    print fibbonachhi(4000000)
