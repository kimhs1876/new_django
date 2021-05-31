from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class NaverMovies(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    dirve = path = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = ''
    title_list = []
    dict = {}
    df = None

    def scrap(self):
        pass

if __name__ == '__main__':
    naver = NaverMovies()
    naver.scrap()

