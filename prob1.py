def multipleOf3and5(num):
    sum = 0
    for i in xrange(num):
        if (i%3==0 or i%5==0):
            sum =sum+i;
    return sum

if __name__ == '__main__':
    #x = raw_input("enter the range: ")
    x = 1000
    print "the sum is: "+str(multipleOf3and5(x))
