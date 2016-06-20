import string

from Tools.scripts.treesync import raw_input

alphas = string.ascii_letters + '_'
nums = string.digits
print('Welcome to the Identifier')
print('Testees must ')
myInput = raw_input('Identifier to test?')
if len(myInput) > 1:
    if myInput[0] not in alphas:
        print('invalid: first symbol must be alphabetic')
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print('invalid: remaining')
                break
        else:
            print('okay as an identifier')
