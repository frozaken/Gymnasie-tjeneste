from random import randint
# from matplotlib.mlab import PCA
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy.random import random


def getXs():
    x = [[1, 5, 1, 1, 1, 2, 1, 3, 1, 1], [1, 5, 4, 4, 5, 7, 10, 3, 2, 1],
         [1, 3, 1, 1, 1, 2, 2, 3, 1, 1], [1, 6, 8, 8, 1, 3, 4, 3, 7, 1],
         [1, 4, 1, 1, 3, 2, 1, 3, 1, 1], [1, 8, 10, 10, 8, 7, 10, 9, 7, 1],
         [1, 1, 1, 1, 1, 2, 10, 3, 1, 1], [1, 2, 1, 2, 1, 2, 1, 3, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 1, 5], [1, 4, 2, 1, 1, 2, 1, 2, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 3, 1, 1], [1, 2, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 5, 3, 3, 3, 2, 3, 4, 4, 1], [1, 1, 1, 1, 1, 2, 3, 3, 1, 1],
         [1, 8, 7, 5, 10, 7, 9, 5, 5, 4], [1, 7, 4, 6, 4, 6, 1, 4, 3, 1],
         [1, 4, 1, 1, 1, 2, 1, 2, 1, 1], [1, 4, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 10, 7, 7, 6, 4, 10, 4, 1, 2], [1, 6, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 7, 3, 2, 10, 5, 10, 5, 4, 4], [1, 10, 5, 5, 3, 6, 7, 7, 10, 1],
         [1, 3, 1, 1, 1, 2, 1, 2, 1, 1], [1, 8, 4, 5, 1, 2, 1, 7, 3, 1],
         [1, 1, 1, 1, 1, 2, 1, 3, 1, 1], [1, 5, 2, 3, 4, 2, 7, 3, 6, 1],
         [1, 3, 2, 1, 1, 1, 1, 2, 1, 1], [1, 5, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 1], [1, 1, 1, 3, 1, 2, 1, 1, 1, 1],
         [1, 3, 1, 1, 1, 1, 1, 2, 1, 1], [1, 2, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 10, 7, 7, 3, 8, 5, 7, 4, 3], [1, 2, 1, 1, 2, 2, 1, 3, 1, 1],
         [1, 3, 1, 2, 1, 2, 1, 2, 1, 1], [1, 2, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 10, 10, 10, 8, 6, 1, 8, 9, 1], [1, 6, 2, 1, 1, 1, 1, 7, 1, 1],
         [1, 5, 4, 4, 9, 2, 10, 5, 6, 1], [1, 2, 5, 3, 3, 6, 7, 7, 5, 1],
         [1, 6, 6, 6, 9, 6, 5, 7, 8, 1], [1, 10, 4, 3, 1, 3, 3, 6, 5, 2],
         [1, 6, 10, 10, 2, 8, 10, 7, 3, 3], [1, 5, 6, 5, 6, 10, 1, 3, 1, 1],
         [1, 10, 10, 10, 4, 8, 1, 8, 10, 1], [1, 1, 1, 1, 1, 2, 1, 2, 1, 2],
         [1, 3, 7, 7, 4, 4, 9, 4, 8, 1], [1, 1, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 4, 1, 1, 3, 2, 1, 3, 1, 1], [1, 7, 8, 7, 2, 4, 8, 3, 8, 2],
         [1, 9, 5, 8, 1, 2, 3, 2, 1, 5], [1, 5, 3, 3, 4, 2, 4, 3, 4, 1],
         [1, 10, 3, 6, 2, 3, 5, 4, 10, 2], [1, 5, 5, 5, 8, 10, 8, 7, 3, 7],
         [1, 10, 5, 5, 6, 8, 8, 7, 1, 1], [1, 10, 6, 6, 3, 4, 5, 3, 6, 1],
         [1, 8, 10, 10, 1, 3, 6, 3, 9, 1], [1, 8, 2, 4, 1, 5, 1, 5, 4, 4],
         [1, 5, 2, 3, 1, 6, 10, 5, 1, 1], [1, 9, 5, 5, 2, 2, 2, 5, 1, 1],
         [1, 5, 3, 5, 5, 3, 3, 4, 10, 1], [1, 1, 1, 1, 1, 2, 2, 2, 1, 1],
         [1, 9, 10, 10, 1, 10, 8, 3, 3, 1], [1, 6, 3, 4, 1, 5, 2, 3, 9, 1],
         [1, 1, 1, 1, 1, 2, 1, 2, 1, 1], [1, 10, 4, 2, 1, 3, 2, 4, 3, 10],
         [1, 4, 1, 1, 1, 2, 1, 3, 1, 1], [1, 5, 3, 4, 1, 8, 10, 4, 9, 1],
         [1, 8, 3, 8, 3, 4, 9, 8, 9, 8], [1, 1, 1, 1, 1, 2, 1, 3, 2, 1],
         [1, 5, 1, 3, 1, 2, 1, 2, 1, 1], [1, 6, 10, 2, 8, 10, 2, 7, 8, 10],
         [1, 1, 3, 3, 2, 2, 1, 7, 2, 1], [1, 9, 4, 5, 10, 6, 10, 4, 8, 1],
         [1, 10, 6, 4, 1, 3, 4, 3, 2, 3], [1, 1, 1, 2, 1, 2, 2, 4, 2, 1],
         [1, 1, 1, 4, 1, 2, 1, 2, 1, 1], [1, 5, 3, 1, 2, 2, 1, 2, 1, 1],
         [1, 3, 1, 1, 1, 2, 3, 3, 1, 1], [1, 2, 1, 1, 1, 3, 1, 2, 1, 1],
         [1, 2, 2, 2, 1, 1, 1, 7, 1, 1], [1, 4, 1, 1, 2, 2, 1, 2, 1, 1],
         [1, 5, 2, 1, 1, 2, 1, 3, 1, 1], [1, 3, 1, 1, 1, 2, 2, 7, 1, 1],
         [1, 3, 5, 7, 8, 8, 9, 7, 10, 7], [1, 5, 10, 6, 1, 10, 4, 4, 10, 10],
         [1, 3, 3, 6, 4, 5, 8, 4, 4, 1], [1, 3, 6, 6, 6, 5, 10, 6, 8, 3],
         [1, 4, 1, 1, 1, 2, 1, 3, 1, 1], [1, 2, 1, 1, 2, 3, 1, 2, 1, 1],
         [1, 1, 1, 1, 1, 2, 1, 3, 1, 1], [1, 3, 1, 1, 2, 2, 1, 1, 1, 1],
         [1, 4, 1, 1, 1, 2, 1, 3, 1, 1], [1, 1, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 3, 1, 1], [1, 1, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 2, 1, 1, 2, 2, 1, 1, 1, 1], [1, 5, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 9, 6, 9, 2, 10, 6, 2, 9, 10], [1, 7, 5, 6, 10, 5, 10, 7, 9, 4]
         ]
    return x[0:25]


def getXs1():
    x = [[1, 5, 1, 1, 1, 2, 1, 3, 1, 1], [1, 5, 4, 4, 5, 7, 10, 3, 2, 1],
         [1, 3, 1, 1, 1, 2, 2, 3, 1, 1], [1, 6, 8, 8, 1, 3, 4, 3, 7, 1],
         [1, 4, 1, 1, 3, 2, 1, 3, 1, 1], [1, 8, 10, 10, 8, 7, 10, 9, 7, 1],
         [1, 1, 1, 1, 1, 2, 10, 3, 1, 1], [1, 2, 1, 2, 1, 2, 1, 3, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 1, 1, 5], [1, 4, 2, 1, 1, 2, 1, 2, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 3, 1, 1], [1, 2, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 5, 3, 3, 3, 2, 3, 4, 4, 1], [1, 1, 1, 1, 1, 2, 3, 3, 1, 1],
         [1, 8, 7, 5, 10, 7, 9, 5, 5, 4], [1, 7, 4, 6, 4, 6, 1, 4, 3, 1],
         [1, 4, 1, 1, 1, 2, 1, 2, 1, 1], [1, 4, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 10, 7, 7, 6, 4, 10, 4, 1, 2], [1, 6, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 7, 3, 2, 10, 5, 10, 5, 4, 4], [1, 10, 5, 5, 3, 6, 7, 7, 10, 1],
         [1, 3, 1, 1, 1, 2, 1, 2, 1, 1], [1, 8, 4, 5, 1, 2, 1, 7, 3, 1],
         [1, 1, 1, 1, 1, 2, 1, 3, 1, 1], [1, 5, 2, 3, 4, 2, 7, 3, 6, 1],
         [1, 3, 2, 1, 1, 1, 1, 2, 1, 1], [1, 5, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 2, 1, 1], [1, 1, 1, 3, 1, 2, 1, 1, 1, 1],
         [1, 3, 1, 1, 1, 1, 1, 2, 1, 1], [1, 2, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 10, 7, 7, 3, 8, 5, 7, 4, 3], [1, 2, 1, 1, 2, 2, 1, 3, 1, 1],
         [1, 3, 1, 2, 1, 2, 1, 2, 1, 1], [1, 2, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 10, 10, 10, 8, 6, 1, 8, 9, 1], [1, 6, 2, 1, 1, 1, 1, 7, 1, 1],
         [1, 5, 4, 4, 9, 2, 10, 5, 6, 1], [1, 2, 5, 3, 3, 6, 7, 7, 5, 1],
         [1, 6, 6, 6, 9, 6, 5, 7, 8, 1], [1, 10, 4, 3, 1, 3, 3, 6, 5, 2],
         [1, 6, 10, 10, 2, 8, 10, 7, 3, 3], [1, 5, 6, 5, 6, 10, 1, 3, 1, 1],
         [1, 10, 10, 10, 4, 8, 1, 8, 10, 1], [1, 1, 1, 1, 1, 2, 1, 2, 1, 2],
         [1, 3, 7, 7, 4, 4, 9, 4, 8, 1], [1, 1, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 4, 1, 1, 3, 2, 1, 3, 1, 1], [1, 7, 8, 7, 2, 4, 8, 3, 8, 2],
         [1, 9, 5, 8, 1, 2, 3, 2, 1, 5], [1, 5, 3, 3, 4, 2, 4, 3, 4, 1],
         [1, 10, 3, 6, 2, 3, 5, 4, 10, 2], [1, 5, 5, 5, 8, 10, 8, 7, 3, 7],
         [1, 10, 5, 5, 6, 8, 8, 7, 1, 1], [1, 10, 6, 6, 3, 4, 5, 3, 6, 1],
         [1, 8, 10, 10, 1, 3, 6, 3, 9, 1], [1, 8, 2, 4, 1, 5, 1, 5, 4, 4],
         [1, 5, 2, 3, 1, 6, 10, 5, 1, 1], [1, 9, 5, 5, 2, 2, 2, 5, 1, 1],
         [1, 5, 3, 5, 5, 3, 3, 4, 10, 1], [1, 1, 1, 1, 1, 2, 2, 2, 1, 1],
         [1, 9, 10, 10, 1, 10, 8, 3, 3, 1], [1, 6, 3, 4, 1, 5, 2, 3, 9, 1],
         [1, 1, 1, 1, 1, 2, 1, 2, 1, 1], [1, 10, 4, 2, 1, 3, 2, 4, 3, 10],
         [1, 4, 1, 1, 1, 2, 1, 3, 1, 1], [1, 5, 3, 4, 1, 8, 10, 4, 9, 1],
         [1, 8, 3, 8, 3, 4, 9, 8, 9, 8], [1, 1, 1, 1, 1, 2, 1, 3, 2, 1],
         [1, 5, 1, 3, 1, 2, 1, 2, 1, 1], [1, 6, 10, 2, 8, 10, 2, 7, 8, 10],
         [1, 1, 3, 3, 2, 2, 1, 7, 2, 1], [1, 9, 4, 5, 10, 6, 10, 4, 8, 1],
         [1, 10, 6, 4, 1, 3, 4, 3, 2, 3], [1, 1, 1, 2, 1, 2, 2, 4, 2, 1],
         [1, 1, 1, 4, 1, 2, 1, 2, 1, 1], [1, 5, 3, 1, 2, 2, 1, 2, 1, 1],
         [1, 3, 1, 1, 1, 2, 3, 3, 1, 1], [1, 2, 1, 1, 1, 3, 1, 2, 1, 1],
         [1, 2, 2, 2, 1, 1, 1, 7, 1, 1], [1, 4, 1, 1, 2, 2, 1, 2, 1, 1],
         [1, 5, 2, 1, 1, 2, 1, 3, 1, 1], [1, 3, 1, 1, 1, 2, 2, 7, 1, 1],
         [1, 3, 5, 7, 8, 8, 9, 7, 10, 7], [1, 5, 10, 6, 1, 10, 4, 4, 10, 10],
         [1, 3, 3, 6, 4, 5, 8, 4, 4, 1], [1, 3, 6, 6, 6, 5, 10, 6, 8, 3],
         [1, 4, 1, 1, 1, 2, 1, 3, 1, 1], [1, 2, 1, 1, 2, 3, 1, 2, 1, 1],
         [1, 1, 1, 1, 1, 2, 1, 3, 1, 1], [1, 3, 1, 1, 2, 2, 1, 1, 1, 1],
         [1, 4, 1, 1, 1, 2, 1, 3, 1, 1], [1, 1, 1, 1, 1, 2, 1, 2, 1, 1],
         [1, 2, 1, 1, 1, 2, 1, 3, 1, 1], [1, 1, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 2, 1, 1, 2, 2, 1, 1, 1, 1], [1, 5, 1, 1, 1, 2, 1, 3, 1, 1],
         [1, 9, 6, 9, 2, 10, 6, 2, 9, 10], [1, 7, 5, 6, 10, 5, 10, 7, 9, 4]
         ]
    return x


def getYs():
    y = [1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1,
         -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1,
         -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1]
    return y[0:25]


def getYs1():
    y = [1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1,
         -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1,
         -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1]
    return y


def prikProd(u, v):
    result = 0
    for i in range(0, len(u)):
        result += u[i] * v[i]
    return result

#
# def pcaHelper(vector, ys):
#     dataMatrix = np.array(vector)
#     myPCA = PCA(dataMatrix)
#     greensX = []
#     greensY = []
#     redsX = []
#     redsY = []
#     i = 0
#     for y in ys:
#         if y == 1:
#             greensX.append(myPCA.Y[i, 0])
#             greensY.append(myPCA.Y[i, 1])
#         else:
#             redsX.append(myPCA.Y[i, 0])
#             redsY.append(myPCA.Y[i, 1])
#         plt.plot(greensX, greensY, 'o', color='green')
#         plt.plot(redsX, redsY, 'o', color='red')
#         i += 1
#     plt.show()
#


def sumList(lst1, lst2):
    newList = []
    for i in range(0, len(lst1)):
        newElem = lst1[i] + lst2[i]
        newList.append(newElem)
    return newList


def gangList(n, lst):
    newLst = []
    for x in lst:
        newLst.append(n * x)
    return newLst


def makeHyper():
    w = [1]
    for i in range(1, 10):
        w.append(randint(1, 10))
    return w


def update(w, x, y):
    wNew = gangList(y, x)
    wNew = sumList(w, wNew)
    return wNew


def hypo(w, x):
    prik = prikProd(w, x)
    val = 1
    if(prik < 0):
        val = -1
    return val


def findWeight(x, y):
    w = makeHyper()
    wasWrong = True
    while(wasWrong and j < 10 ** 6):
        wasWrong = False
        for i in range(len(x)):
            if(hypo(w, x[i]) != y[i]):
                w = update(w, x[i], y[i])
                wasWrong = True
                j += 1
    return w


def calcError(w):
    xs = getXs1()
    ys = getYs1()
    err = [0, 0, len(xs)]
    for i in range(len(xs)):
        if(hypo(w, xs[i]) != ys[i]):
            err[0] += 1
        else:
            err[1] += 1
    print("Algoritmen ramte forkert:  " + str(err[0]) + " gange")
    print("Algoritmen ramte rigtigt: " + str(err[1]) + " gange")
    print("Det giver en succesrate paa " + str(float(err[1])/(len(xs)) * 100))
