# In[0]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

# %%
data = pd.read_excel("D4_37_Processed_1.xlsx")
data1 = data.values.copy()

# %%
plt.rcParams['figure.dpi'] = 100
x_label = "饮食情况"
y_label = "人数"
names = ['低于指南推荐', '在推荐范围内', '高于指南推荐']
x_data = range(len(names))

# %%
data_rice = data1[:, 0]
lw = 0
cl = 0
ov = 0
for datas in data_rice:
    if datas < 250:
        lw += 1
    elif 250 <= datas <= 400:
        cl += 1
    else:
        ov += 1
D_rice = [lw, cl, ov]
print(D_rice)

# %%
data_meat = data1[:, 1]
lw = 0
cl = 0
ov = 0
for datas in data_meat:
    if datas < 120:
        lw += 1
    elif 120 <= datas <= 200:
        cl += 1
    else:
        ov += 1
D_meat = [lw, cl, ov]
print(D_meat)

# %%
data_milk = data1[:, 2]
lw = 0
cl = 0
ov = 0
for datas in data_milk:
    if datas < 500:
        lw += 1
    elif 500 <= datas <= 700:
        cl += 1
    else:
        ov += 1
D_milk = [lw, cl, ov]
print(D_milk)

# %%
data_vtb = data1[:, 4]
lw = 0
cl = 0
ov = 0
for datas in data_vtb:
    if datas < 300:
        lw += 1
    elif 300 <= datas <= 500:
        cl += 1
    else:
        ov += 1
D_vtb = [lw, cl, ov]
print(D_vtb)

# %%
data_frt = data1[:, 5]
lw = 0
cl = 0
ov = 0
for datas in data_frt:
    if datas < 200:
        lw += 1
    elif 200 <= datas <= 350:
        cl += 1
    else:
        ov += 1
D_frt = [lw, cl, ov]
print(D_frt)

# %%
data_oil = data1[:, 6]
lw = 0
cl = 0
ov = 0
for datas in data_oil:
    if datas < 25:
        lw += 1
    elif 25 <= datas <= 30:
        cl += 1
    else:
        ov += 1
D_oil = [lw, cl, ov]
print(D_oil)

# %%
data_salt = data1[:, 7]
lw = 0
cl = 0
ov = 0
for datas in data_salt:
    if datas < 2:
        lw += 1
    elif 2 <= datas <= 5:
        cl += 1
    else:
        ov += 1
D_salt = [lw, cl, ov]
print(D_salt)

# %%
plt.figure(figsize=(8,6))
plt.scatter(x_data,D_rice,label='谷薯类',color='red',marker='o')
plt.plot(x_data,D_rice,linestyle='-',color='red')

plt.scatter(x_data,D_meat,label='肉类',color='orange',marker='^')
plt.plot(x_data,D_meat,linestyle='-',color='orange')

plt.scatter(x_data,D_milk,label='奶制品',color='gold',marker='3')
plt.plot(x_data,D_milk,linestyle='-',color='gold')

plt.scatter(x_data,D_vtb,label='新鲜蔬菜',color='green',marker='P')
plt.plot(x_data,D_vtb,linestyle='-',color='green')

plt.scatter(x_data,D_frt,label='新鲜水果',color='darkturquoise',marker='x')
plt.plot(x_data,D_frt,linestyle='--',color='darkturquoise')

plt.scatter(x_data,D_oil,label='油',color='blue',marker='v')
plt.plot(x_data,D_oil,linestyle='--',color='blue')

plt.scatter(x_data,D_salt,label='盐',color='purple',marker='1')
plt.plot(x_data,D_salt,linestyle='--',color='purple')

plt.xticks(x_data,names)
plt.title("居民饮食情况")
plt.legend()
plt.show()

#%%
graph_data=np.array(D_rice)[:,np.newaxis]
l_vec=[D_meat,D_milk,D_vtb,D_frt,D_oil,D_salt]
for vec in l_vec:
    another_vec=np.array(vec)[:,np.newaxis]
    graph_data=np.hstack((graph_data,another_vec))

#%%
col=['谷薯类','肉类','乳制品','新鲜蔬菜','新鲜水果','油','盐']
pd.DataFrame(graph_data,columns=col).to_excel("./p1_graph_data.xlsx",index=False)
