import matplotlib.pyplot as plt
import numpy as np

# while True:
#     x1, y1 = input("Unesite koordinate točke A: ").split()
#     x2, y2 = input("Unesite koordinate točke B: ").split()
#     try:
#         x1 = int(x1)
#         y1 = int(y1)
#         x2 = int(x2)
#         y2 = int(y2)
#         break;
#     except:
#         print("Molim unesite numeričku vrijednost.")

# a=(y2-y1)/(x2-x1)
# b=x2-x1
# print(" y -",y1,"=",a,"( x -",x1,")")

def fun(x1,y1,x2,y2):
    a=(y2-y1)/(x2-x1)
    b=x2-x1
    print(" y -",y1,"=",a,"( x -",x1,")")

    xaxis = np.array([2,8])
    yaxis = np.array([4,9])

    plt.plot(xaxis,yaxis)
    x = input("Ako želite prikazati graf, unesite 1. \nAko želite spremiti kao PDF, unesite 2. ")
    if x=='1':
        plt.show()
    elif x=='2':
        name = input("Unesite željeno ime datoteke: ")
        plt.savefig(name)  

    #test

fun(1,2,3,4)

