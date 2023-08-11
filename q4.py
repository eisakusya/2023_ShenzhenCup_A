# In[0]
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
mpl.rcParams["font.sans-serif"] = ["kaiti"] # 设置中文字体
mpl.rcParams["axes.unicode_minus"] = False # 设置减号不改变

# In[1]
data = pd.read_excel("q4_preprocessed.xlsx")
data1 = data.fillna(-1).values.copy()

# In[2] 预处理
rows_to_del = []
for i in range(data1.shape[0]):
    for j in range(data1.shape[1]):
        if data1[i, j] == -1:
            rows_to_del.append(i)
data1 = np.delete(data1, rows_to_del, axis=0)

# In[3]
for i in range(data1.shape[0]):
    data1[i, 0] = 2023 - data1[i, 0]

# In[4]
changed_col = np.array(data.columns)
changed_col[0] = "年龄"

pd.DataFrame(data1, columns=changed_col).to_excel("./q4_proocessed_age.xlsx", index=False)
Data = pd.read_excel("q4_proocessed_age.xlsx")
Data1 = Data.values.copy()

# In[5] 归一化
scaler = MinMaxScaler()
Data_normalized = scaler.fit_transform(Data1)

# In[6]
# 聚类评估
wcss = []
for i in range(1, 18):
    kmeans = KMeans(n_clusters=i, max_iter=300, n_init=10, init='k-means++', random_state=0)
    kmeans.fit(Data_normalized)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 18), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# In[7]
# kmeans聚类并得出各项的聚类中心
kmeans = KMeans(n_clusters = 5, max_iter = 300, n_init = 10, init = 'k-means++', random_state = 0)
kmeans.fit(Data_normalized)
cluster_centers_normalized = kmeans.cluster_centers_

# In[8] 逆归一化
cluster_centers = scaler.inverse_transform(cluster_centers_normalized)

# In[9]
#输出保存
pd.DataFrame(cluster_centers,columns=Data.columns).to_excel("./q4_cluster_centers.xlsx",index=False)

# In[10]
# 身高体重聚类
Data_height_weight=np.array(Data_normalized[:,1:3])
y_kmeans=kmeans.fit_predict(Data_height_weight)
plt.scatter(Data_height_weight[y_kmeans == 0, 0], Data_height_weight[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Type1')
plt.scatter(Data_height_weight[y_kmeans == 1, 0], Data_height_weight[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Type2')
plt.scatter(Data_height_weight[y_kmeans == 2, 0], Data_height_weight[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Type3')
plt.scatter(Data_height_weight[y_kmeans == 3, 0], Data_height_weight[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Type4')
plt.scatter(Data_height_weight[y_kmeans == 4, 0], Data_height_weight[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Type5')
plt.scatter(kmeans.cluster_centers_[:, 0],  kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()

# In[11]
# 腰围臀围聚类
Data_Size=np.array(Data_normalized[:,3:5])
y_kmeans=kmeans.fit_predict(Data_Size)
plt.scatter(Data_Size[y_kmeans == 0, 0], Data_Size[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Type1')
plt.scatter(Data_Size[y_kmeans == 1, 0], Data_Size[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Type2')
plt.scatter(Data_Size[y_kmeans == 2, 0], Data_Size[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Type3')
plt.scatter(Data_Size[y_kmeans == 3, 0], Data_Size[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Type4')
plt.scatter(Data_Size[y_kmeans == 4, 0], Data_Size[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Type5')
plt.scatter(kmeans.cluster_centers_[:, 0],  kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('腰围')
plt.ylabel('臀围')
plt.legend()
plt.show()

# In[12]
# 收缩压舒张压聚类
Data_Pressure=np.array(Data_normalized[:,5:7])
y_kmeans=kmeans.fit_predict(Data_Pressure)
plt.scatter(Data_Pressure[y_kmeans == 0, 0], Data_Pressure[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Type1')
plt.scatter(Data_Pressure[y_kmeans == 1, 0], Data_Pressure[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Type2')
plt.scatter(Data_Pressure[y_kmeans == 2, 0], Data_Pressure[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Type3')
plt.scatter(Data_Pressure[y_kmeans == 3, 0], Data_Pressure[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Type4')
plt.scatter(Data_Pressure[y_kmeans == 4, 0], Data_Pressure[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Type5')
plt.scatter(kmeans.cluster_centers_[:, 0],  kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('收缩压')
plt.ylabel('舒张压')
plt.legend()
plt.show()

# In[13]
# 脉搏胆固醇聚类
Data_Pressure=np.array(Data_normalized[:,7:9])
y_kmeans=kmeans.fit_predict(Data_Pressure)
plt.scatter(Data_Pressure[y_kmeans == 0, 0], Data_Pressure[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Type1')
plt.scatter(Data_Pressure[y_kmeans == 1, 0], Data_Pressure[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Type2')
plt.scatter(Data_Pressure[y_kmeans == 2, 0], Data_Pressure[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Type3')
plt.scatter(Data_Pressure[y_kmeans == 3, 0], Data_Pressure[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Type4')
plt.scatter(Data_Pressure[y_kmeans == 4, 0], Data_Pressure[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Type5')
plt.scatter(kmeans.cluster_centers_[:, 0],  kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('脉搏')
plt.ylabel('胆固醇')
plt.legend()
plt.show()

# In[14]
# 甘油三酯和尿酸聚类
Data_Pressure=np.array(Data_normalized[:,12:14])
y_kmeans=kmeans.fit_predict(Data_Pressure)
plt.scatter(Data_Pressure[y_kmeans == 0, 0], Data_Pressure[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Type1')
plt.scatter(Data_Pressure[y_kmeans == 1, 0], Data_Pressure[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Type2')
plt.scatter(Data_Pressure[y_kmeans == 2, 0], Data_Pressure[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Type3')
plt.scatter(Data_Pressure[y_kmeans == 3, 0], Data_Pressure[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Type4')
plt.scatter(Data_Pressure[y_kmeans == 4, 0], Data_Pressure[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Type5')
plt.scatter(kmeans.cluster_centers_[:, 0],  kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('甘油三酯')
plt.ylabel('尿酸')
plt.legend()
plt.show()
