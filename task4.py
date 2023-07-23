from func import *
def main():
    print('дай мне на проверку данные')
    print('сечас проверим пин')
    n = checkpin(input())
    if n==True:
        print('все верно')
    else:
        print('нужно кое что потправить')
    print('сейчас поверим твой пароль')
    n2 = checkpass(input())
    if n2==True:
        print('все верно')
    else:
        print('нужно кое что потправить')
    print('сейчас поверим твой почту')
    n3 = checkmail(input())
    if n3==True:
        print('все верно')
    else:
        print('нужно кое что потправить')
    print('сейчас поверим твой имя')
    n4 = checkname(input())
    if n4==True:
        print('все верно')
    else:
        print('нужно кое что потправить')

main()