from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class NaverMovies(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    dirve_path = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = []
    title_list = []
    dict = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver, page_source, 'html.parser')
        all_div = soup.find_all('div', {"class" : self.class_name}) # 구글검색! #
        self.title_list = [ i.find('a').text for i in all_div]
        driver.close()




if __name__ == '__main__':
    naver = NaverMovies()

    
