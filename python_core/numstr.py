# -*- coding: utf-8 -*-

"""P378"""


class NumStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[%d :: %r]' % (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.__num + self.__string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __nonzero__(self):
        return self.__num or len(self.__string)

    @staticmethod
    def __norm_cval(cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.__num, other.__num)) + self.__norm_cval(cmp(self.__string, other.__string))


if __name__ == '__main__':
    print NumStr(3, 'foo')
    print NumStr(2, 'goo')
    print NumStr(2, 'foo')
    print NumStr()
    print NumStr(string='boo')
    print NumStr(1)
