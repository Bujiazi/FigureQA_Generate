import json
import matplotlib.pyplot as plt

# 解析 JSON 数据
with open('D:\python_projects\FigureQA\output.json', 'r') as json_file:
    data = json.load(json_file)

num = 0
# 遍历每个 "dot_line" 数据
for chart_data in data["data"]:
    plt.figure(figsize=(chart_data['visuals']['figure_width'] // 100, chart_data['visuals']['figure_height'] // 100))
    for class_data in chart_data["data"]:
        x = class_data["x"]
        y = class_data["y"]
        label = class_data["label"]
        color = class_data["color"]

        # 绘制数据点
    plt.scatter(x, y, label=label, color=color, marker='o', s=30)

        # 连接数据点
    plt.plot(x, y, color=color)
    plt.xlabel('X-Axis')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Dot Line Chart')
    plt.legend(loc='best')
    plt.savefig("dot_line_{}.png".format(num))
    num += 1

