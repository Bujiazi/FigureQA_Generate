PLOT_KEY_PAIRS = [("vbar", "vbar_categorical"), ("hbar", "hbar_categorical"), ("pie", None), ("line", None), ("dot_line", None)]

locals = {'data_config_yaml': 'D:\\python_projects\\FigureQA\\config\\color_scheme1_source_data.yaml', 'output_file_json': 'D:\\python_projects\\FigureQA\\output.json', 'common_config_yaml': 'config\\common_source_data.yaml', 'seed': 1, 'colors': 'resources\\x11_colors_refined.txt', 'keep_all_questions': False, 'vbar': 1, 'hbar': 0, 'pie': 0, 'line': 0, 'dot_line': 0, 'PLOT_KEY_PAIRS': [('vbar', 'vbar_categorical'), ('hbar', 'hbar_categorical'), ('pie', None), ('line', None), ('dot_line', None)]}
for arg_name, actual_name in PLOT_KEY_PAIRS:
    print(locals[arg_name])

print(all([locals[arg_name] == 0 for arg_name, actual_name in PLOT_KEY_PAIRS]))
print(any([locals[arg_name] < 0 for arg_name, actual_name in PLOT_KEY_PAIRS]))