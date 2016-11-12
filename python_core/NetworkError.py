# -*- coding: utf-8 -*-


class NetworkError(IOError):
    pass


class FileError(IOError):
    pass


def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)
    if newarg:
        myargs.append(newarg)
    return tuple(myargs)
