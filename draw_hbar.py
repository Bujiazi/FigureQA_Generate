import json
import matplotlib.pyplot as plt

# 读取JSON文件
with open('D:\python_projects\FigureQA\output.json', 'r') as json_file:
    data = json.load(json_file)

num = 0
# 提取数据
for chart_data in data["data"]:
    colors = chart_data["data"][0]["colors"]
    values = chart_data["data"][0]["x"]
    labels = chart_data["data"][0]["y"]

    # 绘制水平条形图
    plt.barh(labels, values, color=colors)

    # 标题和标签
    plt.title("Horizontal Bar Chart")
    plt.xlabel("Values")
    plt.ylabel("Colors")

    # 显示图例
    if chart_data["visuals"]["draw_legend"]:
        plt.legend()

    # 显示网格线
    if chart_data["visuals"]["draw_gridlines"]:
        plt.grid(True)

    # 显示图表
    plt.savefig("hbar_{}.png".format(num))
    num += 1
