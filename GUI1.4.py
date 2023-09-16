import tkinter as tk
from tkinter import ttk

def filter_problems():
    # 获取用户选择的筛选条件
    difficulty = difficulty_var.get()
    keyword = keyword_var.get()

    # 在这里执行筛选和爬取操作，根据您的需求编写代码

    # 示例：模拟任务进度
    progress_bar['value'] = 20  # 更新进度条，这里假设已完成20%的任务
    root.update_idletasks()  # 更新窗口

    # 模拟任务进行中...
    for i in range(5):
        progress_bar['value'] += 20  # 模拟任务进度增加
        root.update_idletasks()  # 更新窗口

        # 模拟正在爬取的题目和题解
        current_problem = f"正在爬取题目 {i + 1}"
        current_solution = f"正在爬取题解 {i + 1}"
        
        # 在文本框中显示正在爬取的题目和题解
        current_info_text.config(state=tk.NORMAL)
        current_info_text.insert(tk.END, current_problem + "\n")
        current_info_text.insert(tk.END, current_solution + "\n")
        current_info_text.config(state=tk.DISABLED)  # 锁定文本框，不允许编辑

        root.update_idletasks()  # 更新窗口

    progress_bar['value'] = 100  # 任务完成，更新进度条到100%

# 创建主窗口
root = tk.Tk()
root.title("洛谷题目筛选")

# 设置窗口大小
root.geometry("800x600")

# 添加标题
title_label = ttk.Label(root, text="洛谷题目筛选工具", font=("Arial", 16))
title_label.pack(pady=10)

# 添加难度选择框
difficulty_label = ttk.Label(root, text="题目难度：", font=("Arial", 12))
difficulty_label.pack()
difficulty_var = tk.StringVar()
difficulty_options = [
    "暂无评定",
    "入门",
    "普及-",
    "普及/提高-",
    "普及+/提高",
    "提高+/省选-",
    "省选/NOI-",
    "NOI/NOI+/CTSC",
]
difficulty_var.set(difficulty_options[0])  # 默认选择第一个
difficulty_combobox = ttk.Combobox(root, textvariable=difficulty_var, values=difficulty_options)
difficulty_combobox.pack()

# 添加关键词输入框
keyword_label = ttk.Label(root, text="其他关键词：", font=("Arial", 12))
keyword_label.pack()
keyword_var = tk.StringVar()
keyword_entry = ttk.Entry(root, textvariable=keyword_var, width=30)
keyword_entry.pack()

# 添加筛选按钮
filter_button = ttk.Button(root, text="筛选题目", command=filter_problems, style="TButton")
filter_button.pack(pady=10)

# 添加进度条
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)

# 添加文本框显示正在爬取的题目和题解
current_info_label = ttk.Label(root, text="正在爬取的题目和题解：", font=("Arial", 12))
current_info_label.pack()
current_info_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
current_info_text.pack()
current_info_text.config(state=tk.DISABLED)  # 锁定文本框，不允许编辑

# 创建主题化样式
style = ttk.Style()
style.configure("TButton", font=("Arial", 14))

# 启动主循环
root.mainloop()
