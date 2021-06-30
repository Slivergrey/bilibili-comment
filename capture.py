"""
此文件用于抓取网页评论信息，获取的Html源码后续使用extract.py提取有效信息
此代码的写成参考了CSDN博主「举个栗子不容易」的原创文章，在这里对他的工作表示感谢，并附上原文链接。
原文链接：https://blog.csdn.net/qq_32201423/article/details/91451391
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import re

pattern_stop = re.compile(r'<div class="loading-state">没有更多评论</div>')
#创建chrome浏览器驱动，无头模式（后台运行，不需要的话可以把headless那行注释掉）
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", options=chrome_options)

# 加载界面
driver.get("https://www.bilibili.com/video/BV1SK4y1T7h3")
time.sleep(3)

# 获取页面初始高度
js = "return action=document.body.scrollHeight"
height = driver.execute_script(js)

# 将滚动条调整至页面底部
driver.execute_script('window.scrollTo(0, document.body.scrollHeight/4)')
time.sleep(5)
driver.find_element_by_class_name('new-sort').click()
# 定义初始时间戳（秒）
t1 = int(time.time())

status = True
driver.set_page_load_timeout(90)
driver.set_script_timeout(90)
while status:
    # 获取当前时间戳（秒）
    t2 = int(time.time())
    # 判断时间初始时间戳和当前时间戳相差是否大于30秒，小于30秒则下拉滚动条
    if t2 - t1 < 30:
        try:
            new_height = driver.execute_script(js)
        except TimeoutException:
            status = False
            driver.execute_script('window.scrollTo(0, 0)')
            print("超时过久放弃加载剩余评论！")
            break
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # 重置初始页面高度
        height = new_height
        print(height)
        # 重置初始时间戳，重新计时
        t1 = int(time.time())
    elif not pattern_stop.search(driver.page_source, 0):
        time.sleep(10)
        t1 = int(time.time())
        print("等待页面刷新中……")
    else:
        status = False
        driver.execute_script('window.scrollTo(0, 0)')
        break
# 打印页面源码
content = driver.page_source
# driver.close()
f = open("3-30_BV1SK4y1T7h3.html", "w", encoding='utf-8')
f.write(content)
f.close()
