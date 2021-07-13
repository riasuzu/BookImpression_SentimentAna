import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# headlessモードを使用する
options.add_argument('--headless')
# headlessモードで暫定的に必要なフラグ(そのうち不要になる)
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
# 起動時にウィンドウを最大化する
options.add_argument('--start-maximized')
# すべての拡張機能を無効にする。ユーザースクリプトも無効にする
options.add_argument('--disable-extensions')
# Proxy経由ではなく直接接続する
options.add_argument('--proxy-server="direct://"')
# すべてのホスト名
options.add_argument('--proxy-bypass-list=*')

driver_path = 'BookImpression_SentimentAna/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, options=options)

driver.get('https://bookmeter.com/rankings/monthly')

# 要素が見つかるまで最大10秒待機
driver.implicitly_wait(10)


class BookImp:

    # 本のタイトルを返す(リスト)
    def get_BookTitle(self):

        bookTitle = []      # 本のタイトルを格納
        bookTitle_elements = driver.find_elements_by_class_name(
            "detail__title")

        for element in bookTitle_elements:
            bookTitle.append(element.text)

        return bookTitle

    # ランキングの月を返す
    def get_BookRank_M(self):

        # ランキングの月
        ranking_month = driver.find_element_by_class_name(
            'title__content').text

        return ranking_month

    # 本のリンクを返す(リスト)
    def get_BookLink(self):

        bookLink = []       # 本のリンクを格納
        bookTitle = self.get_BookTitle()
        for title in bookTitle:
            bookLink.append(driver.find_element_by_link_text(
                title).get_attribute("href"))

        return bookLink

    # 本の感想を返す(リスト)最大120件
    def get_BookImp_text(self, url):

        imp = []            # 本の感想を格納

        driver.get(url)     # 感想を取りたい本のリンクへ

        time.sleep(2)

        imp_element1 = driver.find_elements_by_class_name(
            "frame__content__text")

        for element1 in imp_element1:
            imp.append(element1.text)

        time.sleep(2)

        driver.get(url + '?page=2')

        time.sleep(2)

        imp_element2 = driver.find_elements_by_class_name(
            "frame__content__text")

        for element2 in imp_element2:
            imp.append(element2.text)

        driver.get(url + '?page=3')

        time.sleep(2)

        imp_element3 = driver.find_elements_by_class_name(
            "frame__content__text")

        for element3 in imp_element3:
            imp.append(element3.text)

        return imp
