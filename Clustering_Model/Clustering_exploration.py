import pandas as pd
import pyodbc
import numpy as np
from lib.connector import DBConnector
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import pprint

# data = pd.read_csv('experimental_data.txt', sep="\t")

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

# read SQL tables
conn = DBConnector()
items = pd.read_sql('SELECT * FROM items', conn)

# convert text to tokens and fit a vectorizer
vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words='english')
X = vectorizer.fit_transform(items.title.values)
print('A vectorizer was created with {} tokens'.format(len(vectorizer.get_feature_names())))

# create an input dataframe based on token's occurrences
data_df = pd.DataFrame(data=X.toarray(), columns=vectorizer.get_feature_names())

# # tune the number of clusters
# list_k = range(2, 10)
# sse = []
# for k in list_k:
#     km = MiniBatchKMeans(n_clusters=k)
#     km.fit(data_df.values)
#     sse.append(km.inertia_)
#
# # Plot sse against k
# plt.figure(figsize=(6, 6))
# plt.title('SSE based on Number of clusters')
# plt.plot(list_k, sse, '-o')
# plt.xlabel(r'Number of clusters *k*')
# plt.ylabel('Sum of squared distance');
# plt.show()

# train a clustering model (with the chosen K)
kmeans = MiniBatchKMeans(n_clusters=5, random_state=12345)
kmean_indices = kmeans.fit_predict(data_df.values)
print('\nClustering is finish: {} clusters were created'.format(len(set(kmean_indices))))

# Visualization - reducing to two dimentions using PCA
pca = PCA(n_components=2)
scatter_plot_points = pca.fit_transform(X.toarray())
colors = np.random.rand(len(set(kmean_indices)), 3)
x_axis = [o[0] for o in scatter_plot_points]
y_axis = [o[1] for o in scatter_plot_points]
fig, ax = plt.subplots(figsize=(20, 10))
plt.title('Listings Title Clustering')
ax.scatter(x_axis, y_axis, c=[colors[d] for d in kmean_indices])
for i, txt in enumerate(items.title.values):
    ax.annotate(txt, (x_axis[i], y_axis[i]))
plt.show()

# print clusters
items['cluster'] = list(kmean_indices)

print(kmeans.inertia_)
for cluster in range(len(items['cluster'].unique())):
    print('\n----- Cluster {} -----'.format(cluster))
    cluster_titles = items[items['cluster'] == cluster].title.values
    print(cluster_titles)
