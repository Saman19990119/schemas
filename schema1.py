def diamond():
    # l_h_v=input('lines.horizontal.vertical seperated with "." :').split('.')
    # for i in range(0,len(l_h_v)):
    #     l_h_v[i]=int(l_h_v[i])

    lhv=list(map(lambda a:int(a),input('lines.horizontal.vertical seperated with "." :').split('.'))) #same as above using (map & lambda)

    def body(a,c):
        b=1
        print(end='')
        for i in range (0,a):
            obj=b*"*"
            b+=2
            for i in range (0,c):
                print(obj.center(2*a),end='')
            print()
        b-=2
        for j in range(0,a):
            b-=2
            obj=b*"*"
            for i in range (0,c):
                print(obj.center(2*a),end='')
            print()
        print(end='')
    for i in range(0,lhv[2]):
        body((lhv[0]),lhv[1])


            # easier version of codes above: def "diamond" is equal in both of them, 
            # but a "body" def has replaced with for

    # for i in range(0,l_h_v[2]):
    #     b=1
    #     print(end='')
    #     for i in range (0,(l_h_v[0])):
    #         obj=b*"*"
    #         b+=2
    #         for i in range (0,l_h_v[1]):
    #             print(obj.center(2*(l_h_v[0])),end='')
    #         print()
    #     b-=2
    #     for j in range(0,(l_h_v[0])):
    #         b-=2
    #         obj=b*"*"
    #         for i in range (0,l_h_v[1]):
    #             print(obj.center(2*(l_h_v[0])),end='')
    #         print()
    #     print(end='')


def square():

    lh=input('enter length and height seperated by "." :').split('.')
        # for i in range(0,len(length_height)):
        #     length_height[i]=int(length_height[i])
    lh=list(map(lambda a:int(a),lh)) #map(def,iterable) ,, lambda InnerItterable: FuncOnInnerItterable
    hv=input('enter horizontally and vertically seperated by "." :').split('.')
    hv=list(map(lambda a:int(a),hv))
    for h in range(0,hv[1]):
        print()
        for j in range(0,lh[1]):
            print()
            for i in range(0,hv[0]):
                print(lh[0]*'*',"   ",end = "")


def ask():
    return(input('write "y" to start or "n" to quit: '))


while True:
    match ask():
        case "y":
            match input("chose one to draw:diamond,square,triangle "):
                case "diamond":
                    diamond()
                case "square":
                    square()
                case _:
                    raise Exception('wrong input, try again'.title())
        case "n":
            print('good luck'.title())
            break
        case _:
            print ('wrong input, try again'.title())
            ask()

