import tkinter as tk

def filter_problems():
    # 获取用户选择的筛选条件
    difficulty = difficulty_var.get()
    keyword = keyword_var.get()

    # 在这里执行筛选和爬取操作，根据您的需求编写代码

    # 示例：打印选择的条件
    print("难度：", difficulty)
    print("关键词：", keyword)

# 创建主窗口
root = tk.Tk()
root.title("洛谷题目筛选")

# 添加标题
title_label = tk.Label(root, text="洛谷题目筛选工具", font=("Arial", 16))
title_label.pack(pady=10)

# 添加难度选择框
difficulty_label = tk.Label(root, text="题目难度：", font=("Arial", 12))
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
difficulty_menu = tk.OptionMenu(root, difficulty_var, *difficulty_options)
difficulty_menu.pack()

# 添加关键词输入框
keyword_label = tk.Label(root, text="其他关键词：", font=("Arial", 12))
keyword_label.pack()
keyword_var = tk.StringVar()
keyword_entry = tk.Entry(root, textvariable=keyword_var, width=30)
keyword_entry.pack()

# 添加筛选按钮
filter_button = tk.Button(root, text="筛选题目", command=filter_problems, font=("Arial", 14))
filter_button.pack(pady=10)

# 启动主循环
root.mainloop()
