f = open("differencemat.txt", "r")
f.readline()
N = 1516 #1517
fo = open("Names.txt", "w")
for i in range(N):
    fo.write(f.readline())
f.readline()
fw = open("nummat.txt", "w")
for i in range(N):
    fw.write(f.readline())
