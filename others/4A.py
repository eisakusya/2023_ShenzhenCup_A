#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score, auc
mpl.rcParams["font.sans-serif"] = ["kaiti"] # 设置中文字体
mpl.rcParams["axes.unicode_minus"] = False # 设置减号不改变


# In[24]:


data = pd.read_excel(r"E:\zm\230726深圳杯\A4\数据\d4.xlsx",index_col = 0)


# In[25]:


print("存在缺失值的ID\n",data[np.sum(data.values==-999,axis=1)>0].index.values)
print("共有",np.sum(np.sum(data.values==-999,axis=1)>0),"条数据存在缺失值")


# In[26]:


data1 = data[np.sum(data.values==-999,axis=1)==0].values


# In[68]:


PTP = data1.ptp(axis=0)
MIN = data1.min(axis=0)


# In[69]:


data1 = (data1-MIN)/PTP


# In[70]:


sse = []
for k in range(1,20):
    # 第一次的聚类中心随机产生
    np.random.seed(0) # 设置随机种子
    index = np.random.choice(np.arange(data1.shape[0]),replace =0,size = k)
    center = data1[index].copy()
    # 设置每个类的颜色
    color  =plt.cm.jet(np.linspace(0.01,0.99,k))
    # 初始化标签
    label = np.full(shape=(data1.shape[0],),fill_value=-1)
    # 进行第一次的初始分类
    for i in range(data1.shape[0]):
        label[i]=np.argmin(np.sum((center - data1[i])**2,axis=1)**0.5)
    while True:
        old_label = label.copy()
        for i in range(k):
            class_data = data1[label==i]
            if class_data.shape[0]==0:
                index = np.random.choice(np.arange(data1.shape[0]),replace =0,size = 1)
                center[i] = data1[index].copy()
            else:
                center[i]= np.mean(class_data,axis=0)
        for i in range(data1.shape[0]):
            label[i]=np.argmin(np.sum((center - data1[i])**2,axis=1)**0.5)
        if np.all(old_label==label):
            break
    SSE = 0
    for i in range(k):
        class_data = data1[label==i]
        SSE+= np.mean(np.sum((class_data - center[i])**2,axis=1)**0.5)
    SSE =SSE/k 
    sse+=[SSE]
    print(f"k={k},sse = {SSE}")


# In[73]:


plt.plot(np.arange(1,len(sse)+1),sse,color = "k",marker = "s")
plt.plot(np.arange(1,7),(np.arange(1,7)-1)*(sse[3]-sse[0])/3+sse[0],color = "r")
plt.plot(np.arange(3,19),(np.arange(3,19)-19)*(sse[-1]-sse[-4])/3+sse[-1],color="blue")
plt.xlabel("K(簇的数量)",fontsize=14)
plt.ylabel("SSE(残差)",fontsize = 14)
plt.xticks([6],[6],minor=1)
#plt.savefig(r"E:\zm\230726深圳杯\A4\图\SSE.png",dpi = 1000)
plt.show()


# In[74]:


# 确定k值
k=5
# 第一次的聚类中心随机产生
np.random.seed(0) # 设置随机种子
index = np.random.choice(np.arange(data1.shape[0]),replace =0,size = k)
center = data1[index].copy()
# 设置每个类的颜色
color  =plt.cm.jet(np.linspace(0.01,0.99,k))
# 初始化标签
label = np.full(shape=(data1.shape[0],),fill_value=-1)
# 进行第一次的初始分类
for i in range(data1.shape[0]):
    label[i]=np.argmin(np.sum((center - data1[i])**2,axis=1)**0.5)
while True:
    old_label = label.copy()
    for i in range(k):
        class_data = data1[label==i]
        if class_data.shape[0]==0:
            index = np.random.choice(np.arange(data1.shape[0]),replace =0,size = 1)
            center[i] = data1[index].copy()
        else:
            center[i]= np.mean(class_data,axis=0)
    for i in range(data1.shape[0]):
        label[i]=np.argmin(np.sum((center - data1[i])**2,axis=1)**0.5)
    if np.all(old_label==label):
        break
SSE = 0
for i in range(k):
    class_data = data1[label==i]
    SSE+= np.mean(np.sum((class_data - center[i])**2,axis=1)**0.5)
SSE =SSE/k 
print(f"k={k},sse = {SSE}")


# In[48]:


#pd.DataFrame(label,index = data.index[np.sum(data.values==-999,axis=1)==0],columns=["类别"]).to_excel(r"E:\zm\230726深圳杯\A4\数据\分类结果.xlsx")


# In[84]:


nmb = 0
for i in range(14):
    for j in range(i+1,14):
        n = 100
        data2 = np.zeros(shape=(n,data1.shape[1]))
        data2[:,0] = np.linspace(0,1,n)
        data2[:,1] = np.linspace(0,1,n)
        data2 = np.meshgrid(data2[:,0],data2[:,1])
        x = data2[0].reshape(data2[0].size)
        y = data2[1].reshape(data2[1].size)
        data3 = np.zeros(shape=(x.shape[0],2))
        data3[:,0]=x
        data3[:,1]=y
        newlabel = np.zeros(shape=(x.shape[0],),dtype=np.int16)
        for t in range(data3.shape[0]):
            newlabel[t]=np.argmin(np.sum((center[:,[i,j]] - data3[t])**2,axis=1)**0.5)
        plt.scatter(x,y,alpha=0.1,c = color[newlabel],s=10,zorder = 0)
        plt.scatter(data1[:,i],data1[:,j],c = color[label])
        plt.xlabel(data.columns[i])
        plt.ylabel(data.columns[j])
        #plt.savefig(r"E:\zm\230726深圳杯\A4\图\{}_{}_{}.png".format(nmb,data.columns[i],data.columns[j]),dpi = 500)
        plt.show()
        nmb+=1


# In[ ]:




