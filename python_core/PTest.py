# -*- coding: utf-8 -*-


"""P357"""

class P(object):
    def foo(self):
        print 'Hi, I am P-foo()'


class C(P):
    def foo(self):
        P.foo(self)
        super(C, self).foo()
        print 'Hi, I am C-foo()'


if __name__ == '__main__':
    c = C()
    print c.foo()
    print P.foo(c)
