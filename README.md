# spider
23年秋软工第二次作业--洛谷爬虫

目前可以可以直接运行GUI1.1.py 和main.py
可以看见GUI界面

2023秋软工实践个人作业二

| 这个作业属于哪个课程 | [2023秋软工实践](https://bbs.csdn.net/forums/fzusdn-0831?typeId=4994744) |
| -------------------- | ------------------------------------------------------------ |
| 这个作业要求在哪里   | [2023秋软工实践个人作业二](https://bbs.csdn.net/topics/617213407) |
| 这个作业的目标       | 1.学习AIGC；2.通过AIGC学习爬虫；3.写出合理的GUI以进行图形化操作 |
| 学号                 | 102101136                                                    |

# 1.项目仓库

[项目在这里](https://github.com/lzxwaiting/spider)

# 2-3.项目分析与测试

**AI第一次给的源代码**

```python
import os
import requests
from bs4 import BeautifulSoup

# 创建一个目录来存储题目
output_dir = "题目存储"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 定义要爬取的 URL（这里以洛谷题目列表页为例）
url = "https://www.luogu.com.cn/problem/list?_contentOnly=1"

# 发送 HTTP 请求并解析页面内容
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 在页面中查找题目信息，这部分需要根据具体页面结构来编写代码
# 以下示例仅为演示，你需要根据洛谷页面的实际结构来修改
problem_list = soup.find_all("div", class_="problem-name")

# 遍历题目列表，爬取并存储题目信息
for problem in problem_list:
    title = problem.text.strip()  # 题目标题
    problem_id = problem.find("a")["href"].split("/")[-1]  # 题目编号

    # 创建一个以题目编号和标题命名的文件夹
    folder_name = f"{problem_id}-{title}"
    folder_path = os.path.join(output_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 这里你可以继续爬取题目的详细信息，并生成 Markdown 文件
    # 请注意，这只是一个示例，你需要根据洛谷页面的结构来编写具体代码
    # 你可能需要爬取题目描述、输入输出格式、题解等信息，并以 Markdown 格式保存到文件中

    # 示例：创建一个 Markdown 文件并写入标题
    with open(os.path.join(folder_path, f"{problem_id}-{title}.md"), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        # 这里可以继续写入其他题目信息

print("爬取完成。")

```

可见，GPT-3.5给的代码相对简陋，需要人工去学习爬虫知识，否则光看这份代码会不知所云（哭），会漏掉很多实践所需的模块

**GUI模块**

第一版GUI模块的实现是最快的，虽然GPT3.5给的代码相对简单，但是一个字都没写，花的时间也最少，仅仅3分钟：

```python
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
    "暂无评定入门",
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

```

![image](https://github.com/lzxwaiting/spider/assets/91645131/2e28f1b7-b2d9-4507-bedd-b8a406b61716)


可见，运行效果还是相对不错的

# 4.AIGC表格

| 子任务         | 预估哪些部分使用AIGC | 实际中哪些部分使用AIGC |
| -------------- | -------------------- | ---------------------- |
| 网页内容解析   | 部分                 | 未使用                 |
| 数据提取和清洗 | 部分                 | 部分                   |
| 目录和文件管理 | 未使用               | 部分                   |
| 爬取策略设计   | 部分                 | 部分                   |
| 用户代理模拟   | 未使用               | 部分                   |
| 预处理和后处理 | 部分                 | 未使用                 |

**总结：**

AIGC技术的优点包括自动化、智能化、提高效率、减少错误、适用于大规模数据处理等方面。它适合用在数据提取、爬虫策略优化、异常处理、自动化测试等领域。然而，不适合<u>全盘</u>用于复杂的任务，这需要我们在使用过程中进行调试。

# 5.心得体会

1. 进一步学习了GPT的使用，体会到GPT3.5的实力远不如copilot或者GPT4；
2. 学习到了时间管理的技能，不止一次在自学的过程当中陷入心流状态；
3. 学习到了简单的爬虫原理，虽然并没有从零开始敲代码，但大概和我原先进行前端学习的基础知识有些挂钩。

# 6.PSP表格


| Personal Software Process Stages                             | 预估耗时（分钟） | 实际耗时（分钟） |
| ------------------------------------------------------------ | ---------------- | ---------------- |
| Planning（计划）                                             | 30               | 40               |
| Estimate（估计时间）                                         | 450              | 900              |
| Development（开发）                                          | 360              | 600              |
| Analysis（需求分析（包括学习新技术）                         | 35               | 50               |
| Design（具体设计）                                           | 25               | 20               |
| Coding（具体编码）                                           | 300              | 480              |
| Test（测试（自我测试，修改代码，提交修改）                   | 240              | 360              |
| Postmortem & Process Improvement Plan（事后总结，并提出过程改进计划） | 30               | 30               |
| Total（合计）                                                | 1620             | 1880             |

## 学习和反思：

1. 用GPT-3.5刚开始上手很快，但实际上效果并不是很好；
2. 本来想用copilot来辅助写代码，但是做完学生认证之后他也迟迟没有结果，所以爬虫方面效果并不好
3. 其他课程占用的时间太多，基本只有晚上有时间来思考软工的课程。在接下来的过程中要抓住重点，争取不让其他课程占用宝贵的软工开发时间
