#!/usr/bin/env python3
"""reducer.py"""

from sklearn.cluster import KMeans
import numpy as np
import sys

subclusters_centroid = []
for line in sys.stdin:
    key, value = line.strip().split(" ", 1)
    X = np.array(list(map(float, value.split())))
    subclusters_centroid.append(X)
# for X in arr:
#     subclusters_centroid.append(X)

kmeans = KMeans(init="k-means++").fit(subclusters_centroid)
print(kmeans.cluster_centers_)
