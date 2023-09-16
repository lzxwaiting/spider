import os
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LuoguScraper:
    def __init__(self):
        self.base_url = "https://www.luogu.com.cn/problem/"
        self.login_url = "https://www.luogu.com.cn/"
        self.savedate = "./save"
        self.cookies = [
            {"name": "__client_id", "value": "7f2944524fdd9fe340f352f3426830d56e40e7bb"},
            {"name": "_uid", "value": "642788"}
        ]
        self.problem_count = 10  # 可根据需要更改
        self.driver = None

    def get_problem_list(self, key, var):
        self.driver.get(self.base_url)
        # 使用 WebDriverWait 来等待搜索框元素的出现
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div.main-container > main > div > section > div > section:nth-child(2) > div > div.refined-input.input-wrap.block-item.search-text.frame > input"))
        )
        search_button = self.driver.find_element(By.CSS_SELECTOR, "#app > div.main-container > main > div > section > div > section:nth-child(2) > div > div.search-option.no-wrap")
        search_box.send_keys(key + var)
        search_button.click()
        self.driver.implicitly_wait(10)

        problems_list = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div/div/div[1]/div[2]")
        problems_row = problems_list.find_elements(By.CLASS_NAME, "row")

        return problems_row

    def login(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.login_url)
        self.driver.delete_all_cookies()

        for cookie in self.cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

    def get_problem_list(self, key, var):
        self.driver.get(self.base_url)
        search_box = self.driver.find_element(By.CSS_SELECTOR, "#app > div.main-container > main > div > section > div > section:nth-child(2) > div > div.refined-input.input-wrap.block-item.search-text.frame > input")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "#app > div.main-container > main > div > section > div > section:nth-child(2) > div > div.search-option.no-wrap")
        search_box.send_keys(key + var)
        search_button.click()
        self.driver.implicitly_wait(10)

        problems_list = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div/div/div[1]/div[2]")
        problems_row = problems_list.find_elements(By.CLASS_NAME, "row")

        return problems_row

    def get_problem(self, url, problem_id):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers, verify=False)
        html = response.text

        bs = BeautifulSoup(html, "html.parser")
        core = bs.select("article")[0]
        md = str(core)
        md = re.sub("<h1>", "# ", md)
        md = re.sub("<h2>", "## ", md)
        md = re.sub("<h3>", "#### ", md)
        md = re.sub("</?[a-zA-Z]+[^<>]*>", "", md)

        fn = bs.title.string[:-5]
        savedate = os.path.join(self.savedate, fn)
        if not os.path.exists(savedate):
            os.makedirs(savedate)

        filename = os.path.join(savedate, f'{fn}.md')
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(md)

    def login_and_scrape(self):
        try:
            self.login()

            key = "你的筛选关键字"
            var = "你的筛选条件1"
            var1 = "你的筛选条件2"

            problems_row = self.get_problem_list(key, var)

            i = 0
            for problem_row in problems_row:
                if i >= self.problem_count:
                    break

                problem_name = problem_row.find_element(By.XPATH, "./div[1]/a")
                problem_url = problem_name.get_attribute('href')
                self.get_problem(problem_url, problem_name.text)
                time.sleep(random.randint(2, 4))
                i += 1

        finally:
            if self.driver:
                self.driver.quit()
    

if __name__ == "__main__":
    scraper = LuoguScraper()
    scraper.login_and_scrape()
