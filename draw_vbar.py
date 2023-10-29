import json
import matplotlib.pyplot as plt

# 读取JSON文件
with open('D:\python_projects\FigureQA\output.json', 'r') as file:
    data = json.load(file)

num = 0
# 遍历每个数据集
for dataset in data['data']:
    x = dataset['data'][0]['x']
    y = dataset['data'][0]['y']
    labels = dataset['data'][0]['labels']

    # 创建垂直条形图
    plt.figure(figsize=(8, 6))
    plt.bar(x, y, color=dataset['data'][0]['colors'])

    # 添加标签
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Vertical Bar Chart')

    # 添加柱状图上的标签
    for i in range(len(x)):
        plt.text(x[i], y[i], labels[i], ha='center', va='bottom')

    # 显示图表
    plt.savefig("vbar_{}.png".format(num))
    num += 1
