# In[1]
import matplotlib as mpl
import pandas as pd
import numpy as np

mpl.rcParams["font.sans-serif"] = ["kaiti"]  # 设置中文字体
mpl.rcParams["axes.unicode_minus"] = False  # 设置减号不改变

# In[2]

data = pd.read_excel("D4_37_Data.xlsx")

# In[3]
# 先将所有空缺进行填补，后面再根据细节进行响应填补
data1 = data.fillna(-1).values.copy()

# In[4]
# 对是否吃过食物根据使用量来填补缺失值
j = 0
for i in range(data1.shape[0]):
    for j in range(0, data1.shape[1] - 7, 5):
        if data1[i, j] > 0:
            pass
        elif np.any(data1[i, j + 1:j + 5] > 0):
            data1[i, j] = 1
        else:
            data1[i, j] = 2

# In[5]
# 错误值修正，即如果某人没有某事物的进食频率，则该事物是否吃设为否
j = 0
for i in range(data1.shape[0]):
    for j in range(0, data1.shape[1], 5):
        if np.all(data1[i, j + 1:j + 5] < 0):
            data1[i, j] = 2

# In[6]
# 将使用频率统一为月
j = 0
for i in range(data1.shape[0]):
    for j in range(0, data1.shape[1], 5):
        if data1[i, j] == 2 and j + 4 < data1.shape[1]:
            data1[i, j + 3] = 0
            data1[i, j + 4] = 0
        else:
            if j + 4 < data1.shape[1] and data1[i, j + 3] > 0:
                pass
            elif j + 4 < data1.shape[1] and data1[i, j + 2] > 0:
                # 月频率为周的4倍
                data1[i, j + 3] = 4 * data1[i, j + 2].copy()
            elif j + 4 < data1.shape[1] and data1[i, j + 1] > 0:
                # 月频率为日的30倍
                data1[i, j + 3] = 30 * data1[i, j + 1].copy()

# In[7]
# 将使用频率的缺失值替换为平均值
for j in range(0, data1.shape[1], 5):
    if j + 3 < data1.shape[1]:
        m = np.mean(data1[data1[:, j + 3] > 0, j + 3])
        data1[data1[:, j + 3] < 0, j + 3] = round(m, 2)

# In[8]
# 将平均使用量的缺失值使用同频率下的均值填充
for i in range(data1.shape[0]):
    for j in range(0, data1.shape[1], 5):
        if j + 4 < data1.shape[1] and data1[i, j + 4] < 0:
            data1[i, j + 4] = round(np.mean(data1[data1[:, j + 3] == data1[i, j + 3], j + 4]), 2)
        if j + 4 < data1.shape[1] and data1[i, j + 4] < 0:
            data1[i, j + 4] = round(np.mean(data1[:, j + 4]), 2)

# In[9]
data2 = data1[:, np.array([0, 3, 4])].copy()
for j in range(5, data1.shape[1] - 7, 5):
    if j + 4 < data1.shape[1] - 7:
        data2 = np.c_["1", data2, data1[:, np.array([0, 3, 4]) + j].copy()]

# In[10]
# 将最后几列单独拼接
data_subset = data1[:, 135:142].copy()
data2 = np.hstack((data2, data_subset))

# In[11]
# 对原数据处理data，处理成data2样式的
selected_columns = [col for col in data.columns.values if col[0] != "U"]
data_filtered = data[selected_columns]

# In[12]
# 将预处理后的数组输出成Excel
pd.DataFrame(data2, columns=selected_columns).to_excel("./D4_37_Processed.xlsx", index=False)

# In[13]
import pandas as pd

data_num = pd.read_excel("number.xlsx")

# In[14]
# 全部填充1
data_num1 = data_num.fillna(1).values.copy()

# In[15]
num_of_member = data_num1[:, 0]
com_vec = data_num1[:, 1]
for i in range(data_num1.shape[0]):
    # 家庭用餐人数取最大值
    if com_vec[i] > num_of_member[i]:
        num_of_member[i] = com_vec[i]
    if num_of_member[i] == 0:
        num_of_member[i] = 1

# In[16]
# 读入处理后数据，在进行细化
Data = pd.read_excel("D4_37_Processed.xlsx")
Data1 = Data.values.copy()

# In[17]
# 对平均每次使用量进行单位换算
for i in range(Data1.shape[0]):
    # 大米小麦杂粮
    for k in range(0, 3):
        Data1[i, 2 + k * 3] = Data1[i, 2 + k * 3] * 50
    # 假设薯类一个100g
    Data1[i, 2 + 3 * 3] = Data1[i, 2 + 3 * 3] * 100
    # 肉类、水产品和鲜奶
    for k in range(4, 11):
        Data1[i, 2 + k * 3] *= 50
    # 换算奶粉
    Data1[i, 2 + 11 * 3] *= 10
    # 换算酸奶
    Data1[i, 2 + 12 * 3] *= 50
    # 鸡蛋
    Data1[i, 2 + 13 * 3] *= 60
    # 豆制品和加工品
    for k in range(14, 25):
        Data1[i, 2 + k * 3] *= 50
    # 饮料，取1杯250g
    for k in range(25, 27):
        Data1[i, 2 + k * 3] *= 250
    # 调味料
    for k in range(81, 83):
        Data1[i, k] = Data1[i, k] / num_of_member[i] * 500
    Data1[i, 83] *= 50
    for k in range(84, 86):
        Data1[i, k] *= (500 / num_of_member[i])
    for k in range(86, 88):
        Data1[i, k] *= (50 / num_of_member[i])

# In[18]
# 合并归类
# 薯类
Data2 = Data1[:, 2:3].copy()
rst_vec = Data1[:, 2].copy()
rst_vec.fill(0)
for j in range(2, 12, 3):
    amt_vec = np.array(Data1[:, j])
    num_vec = np.array(Data1[:, j - 1])
    temp_vec = amt_vec * num_vec
    rst_vec += temp_vec
Data2 = rst_vec[:, np.newaxis].copy()

# 蛋白质 -肉类
rst_vec.fill(0)
for j in range(17, 30, 3):
    amt_vec = np.array(Data1[:, j])
    num_vec = np.array(Data1[:, j - 1])
    temp_vec = amt_vec * num_vec
    rst_vec += temp_vec
col_vec = rst_vec[:, np.newaxis]
Data2 = np.hstack((Data2, col_vec))

# 蛋白质-乳制品
for j in range(32, 39, 3):
    amt_vec = np.array(Data1[:, j])
    num_vec = np.array(Data1[:, j - 1])
    temp_vec = amt_vec * num_vec
    rst_vec += temp_vec
Data2 = np.hstack((Data2, rst_vec[:, np.newaxis]))

# 豆类
for j in range(44, 54, 3):
    amt_vec = np.array(Data1[:, j])
    num_vec = np.array(Data1[:, j - 1])
    temp_vec = amt_vec * num_vec
    rst_vec += temp_vec
Data2 = np.hstack((Data2, rst_vec[:, np.newaxis]))

# 新鲜蔬菜
amt_vec = np.array(Data1[:, 56])
num_vec = np.array(Data1[:, 55])
rst_vec = amt_vec * num_vec
Data2 = np.hstack((Data2, rst_vec[:, np.newaxis]))

# 新鲜水果
amt_vec = np.array(Data1[:, 74])
num_vec = np.array(Data1[:, 73])
rst_vec = amt_vec * num_vec
Data2 = np.hstack((Data2, rst_vec[:, np.newaxis]))

# 油
amt_vec = np.array(Data1[:, 81])
rst_vec = amt_vec
amt_vec = np.array(Data1[:, 82])
rst_vec += amt_vec
Data2 = np.hstack((Data2, rst_vec[:, np.newaxis]))

# 盐
Data_temp = np.array(Data1[:, 83:84])
Data2 = np.hstack((Data2, Data_temp))

# In[19]
# 将归类好的数据计算成日均食用量
Data3 = np.round(Data2 / 30, 2)

# In[20]
# 将归类处理后的数组输出成Excel
pd.DataFrame(Data3).to_excel("./D4_37_Processed_1.xlsx", index=False)
