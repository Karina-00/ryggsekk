from time import *
from sys import *
from rygg.classes import *
from rygg.dynamic import *
from rygg.heuristic import *
from rygg.brute_force import *

capacity = int(input())
itemsNum = int(input())

itemsLib = []


for i in range(itemsNum):
    itemsLib.append(
        Item(*input().split(' '), _id=i)
    )


if __name__ == '__main__':
    if argv[1] == "-d":
        dynamic(capacity, itemsNum, itemsLib)
    elif argv[1] == "-f":
        brute_force(capacity, itemsNum, itemsLib)
    elif argv[1] == "-h":
        heuristic(capacity, itemsLib)
