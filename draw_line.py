import json
import matplotlib.pyplot as plt

# 读取JSON文件
with open('D:\python_projects\FigureQA\output.json', 'r') as json_file:
    data = json.load(json_file)

num = 0
# 循环遍历数据并绘制图表
for chart_data in data['data']:
    # import pdb; pdb.set_trace()
    plt.figure(figsize=(chart_data['visuals']['figure_width'] // 100, chart_data['visuals']['figure_height'] // 100))
    
    for line_data in chart_data['data']:
        x = line_data['x']
        y = line_data['y']
        label = line_data['label']
        color = line_data['color']
        
        plt.plot(x, y, label=label, color=color)

    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Line Chart')
    plt.legend(loc='best')
    
    plt.savefig("line_{}.png".format(num))
    num += 1