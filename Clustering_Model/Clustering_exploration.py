import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import pprint

data = pd.read_csv('experimental_data.txt', sep="\t")

# ------------ TF-IDF + MiniBatchKMeans -------- #

# vec = TfidfVectorizer(stop_words="english")
# vec.fit(data.text.values)
# features = vec.transform(data.text.values)

# cls = MiniBatchKMeans(n_clusters=3, random_state=12345)
# cls.fit(features)

# print('Real labels:\t\t', list(data.label))
# # predict cluster labels for new dataset
# print('Predicted lables:\t', list(cls.predict(features)))

# # reduce the features to 2D
# pca = PCA(n_components=2, random_state=12345)
# reduced_features = pca.fit_transform(features.toarray())
#
# # reduce the cluster centers to 2D
# reduced_cluster_centers = pca.transform(cls.cluster_centers_)
#
# plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=cls.predict(features))
# plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:, 1], marker='x', s=150, c='b')
# plt.show()

# print('silhouette_score:',silhouette_score(features, labels=cls.predict(features)))

vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words='english')
X = vectorizer.fit_transform(data.text.values)

data_df = pd.DataFrame(data=X.toarray(), columns=vectorizer.get_feature_names())

kmeans = MiniBatchKMeans(n_clusters=3, random_state=12345)
kmean_indices = kmeans.fit_predict(data_df.values)

# Visualization - reducing to two dimentions using PCA
pca = PCA(n_components=2)
scatter_plot_points = pca.fit_transform(X.toarray())

colors = ["r", "b", "c", "y", "m"]
x_axis = [o[0] for o in scatter_plot_points]
y_axis = [o[1] for o in scatter_plot_points]
fig, ax = plt.subplots(figsize=(20, 10))
plt.title('Listings Title Clustering')
ax.scatter(x_axis, y_axis, c=[colors[d] for d in kmean_indices])
for i, txt in enumerate(data.text.values):
    ax.annotate(txt, (x_axis[i], y_axis[i]))
plt.show()
