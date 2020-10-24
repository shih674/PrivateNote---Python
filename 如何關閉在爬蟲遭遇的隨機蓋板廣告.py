'''
最後更新日期 2020.09
替同學示範如何關閉在爬蟲遭遇的隨機蓋板廣告
目標網站: pinkoi
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 打開瀏覽器
driver = webdriver.Chrome("chromedriver")  # 括號裡面打chromedriver的路徑
driver.get("https://www.pinkoi.com/browse")  # 開啟爬蟲網址
time.sleep(1)  # 休息一秒等網站載入

# 關掉廣告: 試圖尋找廣告HTML物件，有就關閉沒有就跳過
try:
    ad_block = driver.find_element_by_class_name('m-modal-close').click()
    print("有廣告")
except:
    print("沒有廣告")

# 抓取頁面內容
allpage = driver.page_source  # 載入整頁原始碼
soup = BeautifulSoup(allpage, "html.parser")  # 透過beautifulsoup解析

# 想要的商品項目存放在product-link下
domain = "https://www.pinkoi.com/"
linklist = []
title = []
link_topall = soup.find_all(class_='product-link')
for i, ele in enumerate(link_topall):
    linklist.append(domain + ele.find_all('a')[0].get('href'))
    title = ele.find_all('a')[1].get('title')
    print(i, title, ele)
