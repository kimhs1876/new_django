import pandas as pd
from bs4 import BeautifulSoup
import requests

class MelonMusic(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}, header=self.header').text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('---제목---')
        ls = soup.find_all("div", {"class": self.class_name[0]})
        for i in ls:
            print(f'{i.find("a").text}')
        print('---가수---')
        ls = soup.find_all("div", {"class": self.class_name[1]})
        for i in ls:
            print(f'{i.find("a").text}')

    def insert_dict(self):
        ''' #방법 1. range
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
        '''

        ''' #방법 2. zip
        for i, j in zip(self.title_ls, self.artist_ls):
        self.dict[i] = j
        '''
        # 방법 3. enumerate
        for i, j in enumerate(self.title_ls, self.artist_ls):
            self.dict[j] = self.artist_ls[i]
            print(self.dict)

    def dict_to_datagram(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_cvs(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep='', na_rep='NaN')


    @staticmethod
    def main():
        m = MelonMusic()
        while 1:
            menu = (input('0.Exit\n1.Input URL\n2.Get Ranking\n3.Print dict\n4.Dict to Dataframe\n5.DF to Csv'))
            if menu == '0':
                break
            elif menu == '1':
                m.set_url(input('스크래핑할 날짜 입력'))  # '2021052511'
            elif menu == '2':
                m.class_name.append(('ellipsis rank01'))
                m.class_name.append(('ellipsis rank02'))
                m.get_ranking()
            elif menu == '3':
                m.insert_dict()
            elif menu == '4':
                m.dict_to_datagram()
            elif menu == '5':
                m.df_to_cvs()
            else:
                print('Wrong Number')
                continue


MelonMusic.main()

''' 
*남현우씨 코드 
        def title_dict(self):
            for i, j in enumerate(self.get_title):
                self.dict[j] = self.get_artist[i]
            print(self.dict)
'''

