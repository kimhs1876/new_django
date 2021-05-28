from bs4 import BeautifulSoup
import requests

class BugsMusic(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}


    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers = self.headers).text
    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='p',attrs=({"class":self.class_name[0]}))
        ls2 = soup.find_all(name='p',attrs=({"class":self.class_name[1]}))


    def insert_title_dict(self):
       pass


    @staticmethod
    def main():
        b = BugsMusic()
        while 1:
            menu = int(input('0.Exit\n1.Input URL\n2.Get Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                b.set_url(input('상세정보입력'))
            elif menu == 2:
                b.class_name.append("artist")
                b.class_name.append("title")
                b.get_ranking()
            else:
                print('Wrong Number')
                continue

BugsMusic.main()
