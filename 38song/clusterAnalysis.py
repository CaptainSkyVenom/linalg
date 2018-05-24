from __future__ import print_function

from sklearn.datasets import make_blobs
from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def analysisMaxC(matb):
    # X, y = make_blobs(n_samples=200,
    #                   n_features=2,
    #                   centers=4,
    #                   cluster_std=1,
    #                   center_box=(-10.0, 10.0),
    #                   shuffle=True,
    #                   random_state=1)  # For reproducibility
    #

    X = matb


    range_n_clusters = list(range(2,11))

    maxc = 0
    maxi = 0
    for n_clusters in range_n_clusters:

        clusterer = SpectralClustering(n_clusters = n_clusters, affinity='precomputed')
        cluster_labels = clusterer.fit_predict(matb)
        silhouette_avg = silhouette_score(X, cluster_labels)
        print("For n_clusters =", n_clusters,
              "The average silhouette_score is :", silhouette_avg)

        if silhouette_avg > maxc:
            maxc = silhouette_avg
            maxi = n_clusters
    return maxi
