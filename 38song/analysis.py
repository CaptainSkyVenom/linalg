from sklearn import cluster, datasets, mixture
import numpy as np
import csv
import json
from clusterAnalysis import analysisMaxC
import random

bigN = 38
N = 38
N = min(N,bigN)
mat = np.loadtxt(open("nummat.txt", "rb"), delimiter='\t')
matb = np.delete(mat, np.s_[0:1], axis=1)

tempMatrix = []
sample = sorted(random.sample(range(0,bigN), N))

sample = [i for i in sample if not i in list(range(93,105)) ]

N = len(sample)

for i in sample:
    temp = []
    for j in sample:
        temp.append(matb[i][j])
    tempMatrix.append(temp)

matb = np.array(tempMatrix)


matb = (np.zeros(matb.shape)+1) - matb
C = analysisMaxC(matb)
spectral = cluster.SpectralClustering(n_clusters = C, affinity='precomputed')
#spectral = cluster.SpectralClustering(n_clusters = 2, affinity = 'precomputed')

spectral.fit(matb)

f = open("newnamesID.txt", "r")
names = []
idtoname = {}
idtolabel = {}

#f.readline()
j = 0
for i in range(bigN): #1517
    #s = f.readline().split("\t")
    #print(f.readline().split("\t")[1].strip())
    s = f.readline().split("\t")[1].strip()
    if i in sample:
        names.append(s)
        idtoname[j] = s
        idtolabel[j] = int(spectral.labels_[j])
        j += 1

import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

FG=nx.Graph()
FG.add_weighted_edges_from([(i,j,matb[i][j]) for i in range(N) for j in range(N)])
forceatlas2 = ForceAtlas2(
                          # Behavior alternatives
                          outboundAttractionDistribution=False,  # Dissuade hubs
                          linLogMode=False,  # NOT IMPLEMENTED
                          adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
                          edgeWeightInfluence=1.0,

                          # Performance
                          jitterTolerance=1.0,  # Tolerance
                          barnesHutOptimize=True,
                          barnesHutTheta=1.2,
                          multiThreaded=False,  # NOT IMPLEMENTED

                          # Tuning
                          scalingRatio=2.0,
                          strongGravityMode=False,
                          gravity=1.0,

                          # Log
                          verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(FG, pos=None, iterations=500)

x = {}
y = {}
for i in range(len(positions)):
    x[i] = positions[i][0]
    y[i] = positions[i][1]

with open('data.js', 'w') as outfile:
    outfile.write("var x = " + json.dumps({"names":idtoname, "labels":idtolabel, "x":x, "y":y}, sort_keys=True, indent=4))
    outfile.write("\nvar C = " + str(C))
    outfile.write("\nvar N = " + str(N))
