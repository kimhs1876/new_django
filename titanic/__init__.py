# 콘트롤러 인풋 menu
from titanic.views.controller import Controller

if __name__ == '__main__':
    controller = Controller() # 생성자 반드시 해야한다.
    while 1:
        menu = input('0-exit 1-preprocess')
        if menu == '0':
            break
        elif menu == '1':
            controller.preprocess('train.csv')
        else:
            continue