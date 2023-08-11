# In[1]
import pandas as pd
import numpy as np

# In[2]
# 读入数据，准备预处理
data = pd.read_excel("q2_perprocessbyhands.xlsx")

# In[3]
# 先将所有的空缺设置为-1，后续再做细致处理
data1 = data.fillna(-1).values.copy()

# In[4]
# 如果在基本信息上(column0-6)存在缺失，则将该行数据删除
rows_to_delete = []  # List to store rows to be deleted

# Loop through data1 and find rows to delete
for i in range(data1.shape[0]):
    for j in range(7):
        if data1[i, j] == -1 and j != 2 and j != 3:
            rows_to_delete.append(i)
            break
        else:
            if data1[i, 2] == -1 and data1[i, 3] == -1:
                rows_to_delete.append(i)

# Delete rows in data1
data1 = np.delete(data1, rows_to_delete, axis=0)

# In[5]
# 将出生年份数据转化为年龄
for i in range(data1.shape[0]):
    data1[i, 0] = 2023 - data1[i, 0]

# In[6]
# 预处理完成，导出
pd.DataFrame(data1, columns=[col for col in data.columns.values]).to_excel("./q2_Preproocessed.xlsx", index=False)

# In[7]
# 读入预处理后数据
Data = pd.read_excel("q2_Preproocessed.xlsx")
Data1 = Data.values.copy()

# In[8]
# 处理吸烟(column 7-12)
i = 0
while True:
    if Data1[i, 7] == 1 and Data1[i, 10] <= 0:
        # 吸烟但是日均吸烟数量没写，删除此数据
        Data1 = np.delete(Data1, i, axis=0)
    elif Data1[i, 11] == 2 and Data1[i, 12] < 0:
        # 被动吸烟但是被动吸烟数量没写，删除此数据
        Data1 = np.delete(Data1, i, axis=0)
    else:
        # 不吸烟的日均吸烟数量全部设为0
        if Data1[i, 10] == -1:
            Data1[i, 10] = 0
        # 没有被动吸烟的日均被动吸烟数量全部设为0
        if Data1[i, 12] == -1:
            Data1[i, 12] = 0
        i += 1
    if i >= Data1.shape[0]:
        break

# In[9]
# 处理日均吸烟数量：吸烟天数*一天吸烟数量/7
for i in range(Data1.shape[0]):
    if Data1[i, 9] > 0:
        Data1[i, 10] = Data1[i, 9] * Data1[i, 10] / 7

# In[10]
# 删除不需要的列数据7,8,9,11
Data1 = np.delete(Data1, 7, axis=1)
Data1 = np.delete(Data1, 7, axis=1)
Data1 = np.delete(Data1, 7, axis=1)
Data1 = np.delete(Data1, 8, axis=1)

# In[11]
# 从原表格中筛选列
selected_columns = Data.columns.values.copy()
selected_columns = np.delete(selected_columns, 7)
selected_columns = np.delete(selected_columns, 7)
selected_columns = np.delete(selected_columns, 7)
selected_columns = np.delete(selected_columns, 8)

# In[12]
selected_columns[7] = "日平均吸烟根数"

# In[12]
# 吸烟指标处理完成，导出保存
pd.DataFrame(Data1, columns=selected_columns).to_excel("./q2_Processed_cigarette.xlsx", index=False)

# In[13]
# 人工在上一步导出文件加入新列用于记录酒精日均摄入量，并重新导入文件
Data = pd.read_excel("q2_Processed_cigarette.xlsx")
Data2 = Data.values.copy()

# In[14]
# 计算酒精日均摄入量 column9-25,26
for i in range(Data2.shape[0]):
    for j in range(9, 26):
        if Data2[i, j] == -1:
            Data2[i, j] = 0

    Data2[i, 26] = (50 / 7) * (
            Data2[i, 12] * Data2[i, 13] * 0.52 + Data2[i, 15] * Data2[i, 16] * 0.38 + Data2[i, 18] * Data2[
        i, 19] * 0.04 + Data2[i, 21] * Data2[i, 22] * 0.15 + Data2[i, 24] * Data2[i, 25] * 0.1)
    Data2[i, 26] = np.round(Data2[i, 26], 2)

# In[15]
# 删除不必要的列
selected_columns = Data.columns.values.copy()
for i in range(17):
    Data2 = np.delete(Data2, 9, axis=1)
    selected_columns = np.delete(selected_columns, 9)

# In[16]
# 酒精指标处理完成，导出保存
pd.DataFrame(Data2, columns=selected_columns).to_excel("./q2_Processed_alcohol.xlsx", index=False)

# In[17]
# 处理最后一列运动数据并导出 column18
Data = pd.read_excel("q2_Processed_alcohol.xlsx")
Data3 = Data.values.copy()
for i in range(Data3.shape[0]):
    if Data3[i, 18] == -1:
        Data3[i, 18] = 0

pd.DataFrame(Data3, columns=Data.columns).to_excel("./q2_Processed.xlsx", index=False)

# In[18],20 21
Data = pd.read_excel("q2_Processed.xlsx")
Data4 = Data.values.copy()

# In[19]
# 处理疾病数据
row_del = []
for i in range(Data4.shape[0]):
    for j in range(19, 21):
        if Data4[i, j] == -1:
            row_del.append(i)
        if Data4[i, j] == 2:  # 没有
            Data4[i, j] = 0

Data4 = np.delete(Data4, row_del, axis=0)

# In[20]
# 年龄段分类
for i in range(Data4.shape[0]):
    if Data4[i, 0] < 18:
        Data4[i, 0] = 1
    elif 18 <= Data4[i, 0] < 45:
        Data4[i, 0] = 2
    elif 45 <= Data4[i, 0] < 65:
        Data4[i, 0] = 3
    else:
        Data4[i, 0] = 4

# In[21] 输出
selected_columns = np.array(Data.columns)
selected_columns[0] = "年龄"
pd.DataFrame(Data4, columns=selected_columns).to_excel("./q2&3_Processed.xlsx", index=False)
