def plusminus(arr):
    a = 0
    b= 0
    c = 0
    for i in arr:
        if i<0:
            a+=1     # nagitive values
        elif i>0:
            b+=1
        else:
            c+=1
    #check arry length
    l = len(arr)
    # print(round(a,6))
    # print(round(b,6))
    # print(round(c,6))
    positve = a/l
    nagitive = b/l
    zero = c/l


    print("{0:.5f}".format(positve), end='')
    print("{0:.5f}".format(nagitive), end='')
    print("{0:.5f}".format(zero))


arry = [-4,3,-9,0,4,1]
plusminus(arry)