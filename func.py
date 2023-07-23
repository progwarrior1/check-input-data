from langdetect import detect
def checkpin(pin):
    if len(pin)==4 and pin!='1234' and pin[0]!=pin[1]:
        return True
    else:
        return False
def checkpass(password):
    flag1 = False
    flag2 = False
    for i in password:
        if i in 'абвгдеёжзийклмнопрстуфцзъхчщшыюяэ':
            flag1 = True
            break
        if i in '12345678910':
            flag2=True
            break
    if len(password)>=8 and flag1 and flag2:
        return True
    else:
        return False
def checkmail(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False
def checkname(name):
    name2 = name.split()
    flag1 = True
    flag2 = True
    for i in name:
        if not i.isalpha():
            if not i==' ':
                flag1 = False
                break
    for j in name2:
        if j<'Я':
            flag2 = False
            break
    if flag1 and flag2:
        return True
    else:
        return False


