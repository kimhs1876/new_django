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
        all_div = soup.find_all('div', {"class" : self.class_name}) # practice more
        self.title_list = [ i.find('a').text for i in all_div] # practice more
        driver.close()

        for i,j in enumerate(self.title_list):
            self.dict[i+1] = self.title_list[i]   # practice more

        self.df = pd.DataFramde.from_dict(self.dict, orient = 'index')
        path = './data/movie.csv'
        self.df.to_csv(path, sep='', na_rep = 'NaN')
        print(self.dict)



if __name__ == '__main__':
    naver = NaverMovies()
    naver.scrap()

<<<<<<< HEAD
=======

    
>>>>>>> dcd8d7dd7232544c60e9c60c7813019f5622e2ea
