# -*- coding: utf-8 -*-
"""
所有用例的断言判断
"""
import unittest
from TestPython.api.trip_replay import trip_post
from TestPython.api.login import login
from TestPython.api.login import logout
from TestPython.api.resetPassword import email
from TestPython.api.resetPassword import reset


class tripApiTest(unittest.TestCase):
    """replaytrip 轨迹回放"""

    def test_tripSuccuss(self):
        result = trip_post.tripSuccuss()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_tripIDNone(self):
        result = trip_post.tripIDNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_tripSTNone(self):
        result = trip_post.tripSTNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_tripETNone(self):
        result = trip_post.tripETNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_tripIdEmpty(self):
        result = trip_post.tripIdEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_tripSTEmpty(self):
        result = trip_post.tripSTEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format')

    def test_tripETEmpty(self):
        result = trip_post.tripETEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format')

    def test_tripNoID(self):
        result = trip_post.tripNoID()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format')

    def test_tripNoST(self):
        result = trip_post.tripNoST()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format')

    def test_tripNoET(self):
        result = trip_post.tripNoET()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format')


class loginApiTest(unittest.TestCase):
    """login登录"""

    def test_loginSuccess(self):
        result = login.loginSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_loginUserErrorOrPwdError(self):
        result = login.loginUserErrorOrPwdError()
        self.assertEqual(result["status"], 220)
        self.assertEqual(result["message"], 'Invalid account and/or password.')

    def test_loginNoActive(self):
        result = login.loginNoActive()
        self.assertEqual(result["status"], 220)
        self.assertEqual(result["message"], 'Invalid account and/or password.')

    def test_loginUserNone(self):
        result = login.loginUserNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_loginPwdNone(self):
        result = login.loginPwdNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_loginNoUser(self):
        result = login.loginNoUser()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_loginNoPwd(self):
        result = login.loginNoPwd()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_loginUserEmpty(self):
        result = login.loginUserEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_loginPwdEmpty(self):
        result = login.loginPwdEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class logoutApiTest(unittest.TestCase):
    """登出"""

    def test_logoutSuccess(self):
        result = logout.logoutSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_logoutFail(self):
        result = logout.logoutFail()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class emailApiTest(unittest.TestCase):
    """重置密码-验证邮箱"""

    def test_resetSuccess(self):
        result = email.resetSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_resetUnregistered(self):
        result = email.resetUnregistered()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetNone(self):
        result = email.resetNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetEmpty(self):
        result = email.resetEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetInvalidFormat(self):
        result = email.resetInvalidFormat()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetNotfound(self):
        result = email.resetNotfound()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetNoEmail(self):
        result = email.resetNoEmail()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class resetApiTest(unittest.TestCase):
    """重置密码"""

    def test_resetSuccess(self):
        result = reset.resetSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_resetWrongCF(self):
        result = reset.resetWrongCF()
        self.assertEqual(result["status"], 500)
        self.assertEqual(result["message"], 'Internal Server Error.')

    def test_resetPwdIllegal(self):
        result = reset.resetPwdIllegal()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_resetCFNone(self):
        result = reset.resetCFNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetPwdNone(self):
        result = reset.resetPwdNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetCFEmpty(self):
        result = reset.resetCFEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetPwdEmpty(self):
        result = reset.resetPwdEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetNoCF(self):
        result = reset.resetNoCF()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetNoPwd(self):
        result = reset.resetNoPwd()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetPwdSmall(self):
        result = reset.resetPwdSmall()
        self.assertEqual(result["status"], 128)
        self.assertEqual(result["message"], 'enter a password more than 6 numbers or letters in length, try again please.')

    def test_resetPwdboundaryS(self):
        result = reset.resetPwdboundaryS()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_PwdboundaryB(self):
        result = reset.resetPwdboundaryB()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_resetPwdBig(self):
        result = reset.resetPwdBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

if __name__ == '__main__':
    unittest.main()
