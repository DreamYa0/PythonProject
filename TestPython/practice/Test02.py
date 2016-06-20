# -*- coding: UTF-8 -*-
records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4), ('bar1', 5, 6)]


def do_foo(x, y):
    print('foo', x)


def do_bar(s):
    print('bar', s)


def do_bar1(x, y):
    print('bar', x, y)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
    elif tag == 'bar1':
        do_bar1(*args)
