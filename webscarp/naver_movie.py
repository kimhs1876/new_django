from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class NaverMovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    dirver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name =''
    title_ls = []
    dict ={}
    df = None


    def scrap(self):
        driver = webdriver.Chrome(self.dirver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div',{"class":input('클래스명을 입력하세요')}) # tit3
        self.title_ls = [i.find('a').text for i in all_div]

        driver.close()

        for i, j in enumerate(self.title_ls):
            self.dict[i+1] = self.title_ls[i]

        self.df = pd.DataFrame.from_dict(self.dict, orient='index')

        path = './data/movie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')
        print(self.dict)


if __name__ == '__main__':
    naver = NaverMovie()
    naver.scrap()