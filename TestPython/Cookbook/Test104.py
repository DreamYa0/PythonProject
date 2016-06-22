# coding:utf-8

from Tools.scripts.treesync import raw_input

db = {}


def newuser():
    prompt = 'login desired'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken,try another:'
            continue
        else:
            break
    pwd = raw_input('password')
    db[name] = pwd


def olduser():
    name = raw_input('login')
    pwd = raw_input('password')
    password = db.get(name)
    if password == pwd:
        print('welcome incorrect')
    else:
        print('login incorrect')


def showmenu():
    pass
