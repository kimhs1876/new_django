class Member(object):
    id = ''
    pw = ''
    name = ''
    email = ''


@staticmethod
def main():
    member = Member()
    while 1:
        menu = int(input('0.Exit 1.회원가입 2.로그인 3.마이페이지 4.회원정보수정 5.회원탈퇴'))
        if menu == 0:
            break
        elif menu == 1:
            pass
        elif menu == 2:
            pass
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        else:
            continue
