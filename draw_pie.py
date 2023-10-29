import matplotlib.pyplot as plt
import json

# Define the JSON data
file_path = "D:\python_projects\FigureQA\output.json"

# 打开文件并加载JSON数据
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
# Iterate through each "data" section in the JSON
num = 0
for data_section in json_data['data']:
    data = data_section['data'][0]
    labels = data['labels']
    colors = data['colors']
    sizes = [(end - start) * 360 / (2 * 3.141592653589793) for start, end in zip(data['starts'], data['ends'])]

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Set title and legend
    ax.set_title('Pie Chart')
    ax.legend(labels, title="Labels", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    num += 1
    # Save the pie chart as an image or display it
    plt.savefig('pie_chart_{}.png'.format(num), bbox_inches='tight')  # Save the pie chart as an image
    # plt.show()  # Display the pie chart

    # Close the plot to generate the next one
    plt.close()

