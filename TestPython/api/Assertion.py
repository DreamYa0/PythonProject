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
from TestPython.api.users import userManagement
from TestPython.api.users import Adduser
from TestPython.api.users import Adituser
from TestPython.api.users import DeleteUser
from TestPython.api.Timeline import timeline
from TestPython.api.report_Dashboard import Dashboard
from TestPython.api.users import user_id
from TestPython.api.role import permissions
from TestPython.api.role import userrole
from TestPython.api.role import Addrole
from TestPython.api.role import role_id
from TestPython.api.role import Aditrole
from TestPython.api.role import deleterole


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

    def test_loginPwdSmall(self):
        result = login.loginPwdSmall()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_loginPwdBig(self):
        result = login.loginPwdBig()
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
        self.assertEqual(result["status"], 218)
        self.assertEqual(result["message"], 'Mailbox not activated.')

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

    def test_resetInvalid(self):
        result = reset.resetInvalid()
        self.assertEqual(result["status"], 219)
        self.assertEqual(result["message"], 'Link failure.')

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
        self.assertEqual(result["message"],
                         'enter a password more than 6 numbers or letters in length, try again please.')

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


class userManagementApiTest(unittest.TestCase):
    """获取全部子账号列表"""

    def test_userSuccess(self):
        result = userManagement.userSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_userNoCookie(self):
        result = userManagement.userNoCookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class AdduserApiTest(unittest.TestCase):
    """新增子账号"""

    def test_AdduserNoCookie(self):
        result = Adduser.AdduserNoCookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_AdduserSuccess(self):
        result = Adduser.AdduserSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AdduserENone(self):
        result = Adduser.AdduserENone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserFNNONE(self):
        result = Adduser.AdduserFNNONE()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserLNNone(self):
        result = Adduser.AdduserLNNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserATNone(self):
        result = Adduser.AdduserATNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserMNone(self):
        result = Adduser.AdduserMNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserPwdNone(self):
        result = Adduser.AdduserPwdNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserRIdNone(self):
        result = Adduser.AdduserRIdNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserTidsNone(self):
        result = Adduser.AdduserTidsNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserEEmpty(self):
        result = Adduser.AdduserEEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserFNEmpty(self):
        result = Adduser.AdduserFNEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserLNEmpty(self):
        result = Adduser.AdduserLNEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserATEmpty(self):
        result = Adduser.AdduserATEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserMEmpty(self):
        result = Adduser.AdduserMEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserPwdEmpty(self):
        result = Adduser.AdduserPwdEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserRIdEmpty(self):
        result = Adduser.AdduserRIdEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserTidsEmpty(self):
        result = Adduser.AdduserTidsEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoEmail(self):
        result = Adduser.AdduserNoEmail()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoFN(self):
        result = Adduser.AdduserNoFN()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoLN(self):
        result = Adduser.AdduserNoLN()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoAT(self):
        result = Adduser.AdduserNoAT()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoM(self):
        result = Adduser.AdduserNoM()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoPwd(self):
        result = Adduser.AdduserNoPwd()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoRId(self):
        result = Adduser.AdduserNoRId()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserNoTids(self):
        result = Adduser.AdduserNoTids()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserAEmailError(self):
        result = Adduser.AdduserAEmailError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserUEmailError(self):
        result = Adduser.AdduserUEmailError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserEFormError(self):
        result = Adduser.AdduserEFormError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserFNBig(self):
        result = Adduser.AdduserFNBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserLNBig(self):
        result = Adduser.AdduserLNBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserMEBig(self):
        result = Adduser.AdduserMEBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserPwdBig(self):
        result = Adduser.AdduserPwdBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserPwdSmall(self):
        result = Adduser.AdduserPwdSmall()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserRIdError(self):
        result = Adduser.AdduserRIdError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class user_idApiTest(unittest.TestCase):
    """获取单个子账号详情"""

    def oneuserSuccess(self):
        result = user_id.oneuserSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def oneuserNocookie(self):
        result = user_id.oneuserNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class AdituserApiTest(unittest.TestCase):
    """修改子账号"""

    def test_AdituserNoCookie(self):
        result = Adituser.AdituserNoCookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_AdituserENone(self):
        result = Adituser.AdituserENone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserFNNONE(self):
        result = Adituser.AdituserFNNONE()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserLNNone(self):
        result = Adituser.AdituserLNNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserATNone(self):
        result = Adituser.AdituserATNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserMNone(self):
        result = Adituser.AdituserMNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserRIdNone(self):
        result = Adituser.AdituserRIdNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserTidsNone(self):
        result = Adituser.AdituserTidsNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserEEmpty(self):
        result = Adituser.AdituserEEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserFNEmpty(self):
        result = Adituser.AdituserFNEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserLNEmpty(self):
        result = Adituser.AdituserLNEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserATEmpty(self):
        result = Adituser.AdituserATEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserMEmpty(self):
        result = Adituser.AdituserMEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserRIdEmpty(self):
        result = Adituser.AdituserRIdEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserTidsEmpty(self):
        result = Adituser.AdituserTidsEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserAEmailError(self):
        result = Adituser.AdituserAEmailError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserUEmailError(self):
        result = Adituser.AdituserUEmailError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserEFormError(self):
        result = Adituser.AdituserEFormError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserFNBig(self):
        result = Adituser.AdituserFNBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserLNBig(self):
        result = Adituser.AdituserLNBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserMEBig(self):
        result = Adituser.AdituserMEBig()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserRIdError(self):
        result = Adituser.AdituserRIdError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdituserESuccess(self):
        result = Adituser.AdituserESuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AdituserFNSuccess(self):
        result = Adituser.AdituserFNSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AdituserLNSuccess(self):
        result = Adituser.AdituserLNSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AdituserATSuccess(self):
        result = Adituser.AdituserATSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AdituserMSuccess(self):
        result = Adituser.AdituserMSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AdituserRIdSuccess(self):
        result = Adituser.AdituserRIdSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AdituserTidsSuccess(self):
        result = Adituser.AdituserTidsSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')


class DeleteUserApiTest(unittest.TestCase):
    """删除子账号"""

    def test_deleteUserSuccess(self):
        result = DeleteUser.deleteUserSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_deleteUserNocookie(self):
        result = DeleteUser.deleteUserNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class timelineApiTest(unittest.TestCase):
    """轨迹时间轴查询"""

    def test_timelineNoCookie(self):
        result = timeline.timelineNoCookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_timelineSuccessA(self):
        result = timeline.timelineSuccessA()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_timelineSuccessB(self):
        result = timeline.timelineSuccessB()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_timelineIdsNone(self):
        result = timeline.timelineIdsNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineSTNone(self):
        result = timeline.timelineSTNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineETNone(self):
        result = timeline.timelineETNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineIdsEmpty(self):
        result = timeline.timelineIdsEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineSTEmpty(self):
        result = timeline.timelineSTEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineETEmpty(self):
        result = timeline.timelineETEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineNoIds(self):
        result = timeline.timelineNoIds()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineNoST(self):
        result = timeline.timelineNoST()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineNoET(self):
        result = timeline.timelineNoET()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class DashboardApiTest(unittest.TestCase):
    """获取各报表前7数据"""

    def test_mileageSuccess(self):
        result = Dashboard.mileageSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def driving_timeSuccess(self):
        result = Dashboard.driving_timeSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def fuelSuccess(self):
        result = Dashboard.fuelSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def speedSuccess(self):
        result = Dashboard.speedSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def temperatureSuccess(self):
        result = Dashboard.temperatureSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def visitSuccess(self):
        result = Dashboard.visitSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def maintenceSuccess(self):
        result = Dashboard.maintenceSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def IFIASuccess(self):
        result = Dashboard.IFIASuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def NOcookie(self):
        result = Dashboard.NOcookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class permissionsApiTest(unittest.TestCase):
    """获取角色所有权限"""

    def test_roleSuccess(self):
        result = permissions.roleSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_roleNocookie(self):
        result = permissions.roleNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class userroleApiTest(unittest.TestCase):
    """获取权限子账号信息"""

    def test_userroleSuccess(self):
        result = userrole.userroleSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_userroleNocookie(self):
        result = userrole.userroleNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class AddroleApiTest(unittest.TestCase):
    """创建子角色"""

    def test_addroleSuccess(self):
        result = Addrole.addroleSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_addroleNocookie(self):
        result = Addrole.addroleNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_addroleOnly(self):
        result = Addrole.addroleOnly()
        self.assertEqual(result["status"], 918)
        self.assertEqual(result["message"], 'Name repetition.')

    def test_addroleNMEmpty(self):
        result = Addrole.addroleNMEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_addrolePMSEmpty(self):
        result = Addrole.addrolePMSEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_addroleNMNone(self):
        result = Addrole.addroleNMNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_addrolePMSNone(self):
        result = Addrole.addrolePMSNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_addroleNoNM(self):
        result = Addrole.addroleNoNM()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_addroleNoPMS(self):
        result = Addrole.addroleNoPMS()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class role_idApiTest(unittest.TestCase):
    """获取单个子角色信息"""

    def test_oneroleSuccess(self):
        result = role_id.oneroleSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_oneroleNocookie(self):
        result = role_id.oneroleNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class AditroleApiTest(unittest.TestCase):
    """修改子角色"""

    def test_roleNocookie(self):
        result = Aditrole.roleNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_rolenameSuccess(self):
        result = Aditrole.rolenameSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_rolePMSSuccess(self):
        result = Aditrole.rolePMSSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_rolePMSNothing(self):
        result = Aditrole.rolePMSNothing()
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["message"], 'Not found.')

    def test_rolenameNone(self):
        result = Aditrole.rolenameNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolePMSNone(self):
        result = Aditrole.rolePMSNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolenameEmpty(self):
        result = Aditrole.rolenameEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolePMSEmpty(self):
        result = Aditrole.rolePMSEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class deleteroleApiTest(unittest.TestCase):
    """删除子角色"""

    def test_roleNocookie(self):
        result = deleterole.roleNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_roleDeleteSuccess(self):
        result = deleterole.roleDeleteSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')


if __name__ == '__main__':
    unittest.main()
