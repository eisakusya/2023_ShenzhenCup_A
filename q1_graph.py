# In[0]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

# In[1]
data = pd.read_excel("D4_37_Processed_1.xlsx")
data1 = data.values.copy()

# In[2]
data_vtb = data1[:, 4]
lower_std = 0
close_std = 0
over_std = 0
for datas in data_vtb:
    if datas < 300:
        lower_std += 1
    elif 300 <= datas <= 500:
        close_std += 1
    else:
        over_std += 1
std = [lower_std, close_std, over_std]
subject = ['低于指南', '在指南推荐范围内', '高于指南']
plt.bar(subject, std)
plt.show()

# In[3]
data_fruit = data1[:, 5]
lower_std = 0
close_std = 0
over_std = 0
for datas in data_fruit:
    if datas < 200:
        lower_std += 1
    elif 200 <= datas <= 350:
        close_std += 1
    else:
        over_std += 1
std = [lower_std, close_std, over_std]
subject = ['低于指南', '在指南推荐范围内', '高于指南']
plt.bar(subject, std)
plt.show()

# In[4]
data_meat = data1[:, 1]
lower_std = 0
close_std = 0
over_std = 0
for datas in data_meat:
    if datas < 120:
        lower_std += 1
    elif 120 <= datas <= 200:
        close_std += 1
    else:
        over_std += 1
std = [lower_std, close_std, over_std]
subject = ['低于指南', '在指南推荐范围内', '高于指南']
plt.bar(subject, std)
plt.show()

# In[5]
data_milk = data1[:, 2]
lower_std = 0
close_std = 0
over_std = 0
for datas in data_milk:
    if datas < 500:
        lower_std += 1
    elif 500 <= datas <= 700:
        close_std += 1
    else:
        over_std += 1
std = [lower_std, close_std, over_std]
subject = ['低于指南', '在指南推荐范围内', '高于指南']
plt.bar(subject, std)
plt.show()

# In[6]
data_rice = data1[:, 0]
lower_std = 0
close_std = 0
over_std = 0
for datas in data_rice:
    if datas < 250:
        lower_std += 1
    elif 250 <= datas <= 400:
        close_std += 1
    else:
        over_std += 1
std = [lower_std, close_std, over_std]
subject = ['低于指南', '在指南推荐范围内', '高于指南']
plt.bar(subject, std)
plt.show()

# In[7]
data_oil = data1[:, 6]
lower_std = 0
close_std = 0
over_std = 0
for datas in data_oil:
    if datas < 25:
        lower_std += 1
    elif 25 <= datas <= 30:
        close_std += 1
    else:
        over_std += 1
std = [lower_std, close_std, over_std]
subject = ['低于指南', '在指南推荐范围内', '高于指南']
plt.bar(subject, std)
plt.show()

# In[8]
data_salty = data1[:, 7]
lower_std = 0
close_std = 0
over_std = 0
for datas in data_oil:
    if datas < 5:
        close_std += 1
    else:
        over_std += 1
std = [close_std, over_std]
subject = ['在指南推荐范围内', '高于指南']
plt.bar(subject, std)
plt.show()

# In[9]
avr_rice = np.round(np.mean(data_rice), 2)
avr_meat = np.round(np.mean(data_meat), 2)
avr_milk = np.round(np.mean(data_milk), 2)
data_bean = data1[:, 3]
avr_bean = np.round(np.mean(data_bean), 2)
avr_vtb = np.round(np.mean(data_vtb), 2)
avr_fruit = np.round(np.mean(data_fruit), 2)
avr_oil = np.round(np.mean(data_oil), 2)
avr_salty = np.round(np.mean(data_salty), 2)
subject = ['谷薯类', '肉类', '乳制品', '豆类',
           '新鲜蔬菜', '新鲜水果', '油', '盐']
avr_data = [avr_rice, avr_meat, avr_milk, avr_bean, avr_vtb, avr_fruit, avr_oil, avr_salty]
plt.bar(subject,avr_data)
plt.show()
