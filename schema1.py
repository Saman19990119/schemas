def diamond():
    l_h_v=input('lines.horizontal.vertical seperated with "." :').split('.')
    for i in range(0,len(l_h_v)):
        l_h_v[i]=int(l_h_v[i])
    def left(a,c):
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
    for i in range(0,l_h_v[2]):
        left((l_h_v[0]),l_h_v[1])


def ask():
    return(input('write "y" to start or "n" to quit: '))
while True:
    match ask():
        case "y":
            typeof=input("chose one to draw:diamond,square,triangle ")
            if typeof=='diamond':
                diamond()
            elif typeof  != 'diamond':
                raise Exception('wrong input, try again'.title())
        case "n":
            print('good luck')
            break
        case _:
            print('wrong input, try again'.title())
            ask()



# while ask()=="yes":
#     if ask()=="no":
#         break

#     typeof=input("chose one to draw:diamond,square,triangle ")
#     if typeof=='diamond':
#         diamond()

#     elif typeof  != 'diamond':
#         raise Exception('wrong input, try again'.title())
# print('good luck')