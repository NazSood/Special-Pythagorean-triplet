import random
m = 1
n = 0
a = 0
b = 0
c = 0
#list = []

while (True):
    a = (m ** 2) - (n ** 2)
    b = 2 * m * n
    c = (m ** 2) + (n ** 2)
    m += 1
    n += 1
    #list.append((a+b+c) / a)
    #print("({0} + {1} + {2} = {3})".format(a, b, c, (a+b+c)))
    if((a+b+c) == 1000):
        print("caught ({0} + {1} + {2} = {3})".format(a, b, c, (a+b+c)))
        #print(list)
        print("Product: ",a * b * c)
        break
    elif ((a+b+c) > 1000):
        print("m: {0} n: {1}".format(m, n))
        m = random.randrange(1, 20, 1)
        print("random m val: ", m)
        n = 0
        a = 0
        b = 0
        c = 0





