import requests
from bs4 import BeautifulSoup
import pandas
import datetime

def naver_Ad_Close(code,year)
    today_date = datetime.datetime.now
    period = float(year) * 365
    get_period = float(year) / 1.47
    naver_addr= f'???'
    request_result = requests.get(naver_addr)
    bs = BeautifulSoup(request_result.content, 'html.parser')
    all_data = bs.select('chartdata')
    stock_symbol = all_data[0].attrs['name']
    stock_data = bs.select('item')
    date_list = []
    modified_closing_price_list = []
    data_dict = {}
    for i in range(len(stock_data)):
        int = str(stock_data[i])[12:-9]
        int_sptiled = int.split('|')
        date = pandas.to_datetime(int_sptiled[0])
        modified_closing_price = float(int_sptiled[4])
        date_list.append(date)
        modified_closing_price_list.append(modified_closing_price)
    data_dict['Price'] = modified_closing_price_list

    df = pandas.DataFrame(data_dict, index=date_list)
    print(df)
    file_name = f'{stock_symbol}_{str(date_list[0])[:10]}-{str(today_date)[:10]}'
    df.to_scv('{0}.csv'.format(file_name), encodings='ms949')
    print('\n{0} 저장완료'.format(file_name))

네이버수정종가크롤링('005930', '10')