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
from TestPython.api.users import Edituser
from TestPython.api.users import DeleteUser
from TestPython.api.Timeline import timeline
from TestPython.api.report_Dashboard import Dashboard
from TestPython.api.users import user_id
from TestPython.api.role import permissions
from TestPython.api.role import userrole
from TestPython.api.role import Addrole
from TestPython.api.role import role_id
from TestPython.api.role import Editrole
from TestPython.api.role import deleterole
from TestPython.api.POI_GEO import pois
from TestPython.api.POI_GEO import Addpoi
from TestPython.api.POI_GEO import EditPOI
from TestPython.api.POI_GEO import deletepoi
from TestPython.api.POI_GEO import GEO
from TestPython.api.POI_GEO import Addgeo
from TestPython.api.POI_GEO import Editgeo
from TestPython.api.POI_GEO import deletegeo
from TestPython.api.notification import notification
from TestPython.api.CHApiTest import Register
from TestPython.api.CHApiTest import Email
from TestPython.api.CHApiTest import Profile
from TestPython.api.CHApiTest import Trackers
from TestPython.api.CHApiTest import Tracker
from TestPython.api.CHApiTest import TrackerAdd
from TestPython.api.CHApiTest import LabelGet
from TestPython.api.CHApiTest import LabelAdd
from TestPython.api.CHApiTest import LabelEdit
from TestPython.api.CHApiTest import LabelDel
from TestPython.api.CHApiTest import NotificationEdit


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
        self.assertEqual(result["status"], 914)
        self.assertEqual(result["message"],
                         'Your account has been created. Please use your email address and password to login.')

    def test_AdduserUEmailError(self):
        result = Adduser.AdduserUEmailError()
        self.assertEqual(result["status"], 914)
        self.assertEqual(result["message"],
                         'Your account has been created. Please use your email address and password to login.')

    def test_AdduserEFormError(self):
        result = Adduser.AdduserEFormError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserPwdOut(self):
        result = Adduser.AdduserPwdOut()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserPwdLess(self):
        result = Adduser.AdduserPwdLess()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AdduserPwdMax(self):
        result = Adduser.AdduserPwdMax()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')


class EdituserApiTest(unittest.TestCase):
    """修改子账号"""

    def test_EdituserNoCookie(self):
        result = Edituser.EdituserNoCookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_EdituserENone(self):
        result = Edituser.EdituserENone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserFNNONE(self):
        result = Edituser.EdituserFNNONE()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserLNNone(self):
        result = Edituser.EdituserLNNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserATNone(self):
        result = Edituser.EdituserATNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserMNone(self):
        result = Edituser.EdituserMNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserRIdNone(self):
        result = Edituser.EdituserRIdNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserTidsNone(self):
        result = Edituser.EdituserTidsNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserEEmpty(self):
        result = Edituser.EdituserEEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserFNEmpty(self):
        result = Edituser.EdituserFNEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserLNEmpty(self):
        result = Edituser.EdituserLNEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserATEmpty(self):
        result = Edituser.EdituserATEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserMEmpty(self):
        result = Edituser.EdituserMEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserRIdEmpty(self):
        result = Edituser.EdituserRIdEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserTidsEmpty(self):
        result = Edituser.EdituserTidsEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserAEmailError(self):
        result = Edituser.EdituserAEmailError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserUEmailError(self):
        result = Edituser.EdituserUEmailError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserEFormError(self):
        result = Edituser.EdituserEFormError()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EdituserESuccess(self):
        result = Edituser.EdituserESuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EdituserFNSuccess(self):
        result = Edituser.EdituserFNSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EdituserLNSuccess(self):
        result = Edituser.EdituserLNSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EdituserATSuccess(self):
        result = Edituser.EdituserATSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EdituserMSuccess(self):
        result = Edituser.EdituserMSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EdituserRIdSuccess(self):
        result = Edituser.EdituserRIdSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EdituserTidsSuccess(self):
        result = Edituser.EdituserTidsSuccess()
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
        self.assertEqual(result["message"], 'Name has existed.')

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

    def test_addroleNMInt(self):
        result = Addrole.addroleNMInt()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_addrolePMSStr(self):
        result = Addrole.addrolePMSStr()
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


class EditroleApiTest(unittest.TestCase):
    """修改子角色"""

    def test_roleNocookie(self):
        result = Editrole.roleNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_rolenameSuccess(self):
        result = Editrole.rolenameSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_rolePMSSuccess(self):
        result = Editrole.rolePMSSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_rolePMSNothing(self):
        result = Editrole.rolePMSNothing()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolenameNone(self):
        result = Editrole.rolenameNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolePMSNone(self):
        result = Editrole.rolePMSNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolenameEmpty(self):
        result = Editrole.rolenameEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolePMSEmpty(self):
        result = Editrole.rolePMSEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolenameInt(self):
        result = Editrole.rolenameInt()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_rolePMSStr(self):
        result = Editrole.rolePMSStr()
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


class emailApiTest(unittest.TestCase):
    """重置密码-验证邮箱"""

    def test_resetUnregistered(self):
        result = email.resetUnregistered()
        self.assertEqual(result["status"], 218)
        self.assertEqual(result["message"], 'This email address is not activated.')

    def test_resetNone(self):
        result = email.resetNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetEmpty(self):
        result = email.resetEmpty()
        self.assertEqual(result["status"], 912)
        self.assertEqual(result["message"], 'Invalid email format.')

    def test_resetInvalidFormat(self):
        result = email.resetInvalidFormat()
        self.assertEqual(result["status"], 912)
        self.assertEqual(result["message"], 'Invalid email format.')

    def test_resetNotfound(self):
        result = email.resetNotfound()
        self.assertEqual(result["status"], 218)
        self.assertEqual(result["message"], 'This email address is not activated.')

    def test_resetNoEmail(self):
        result = email.resetNoEmail()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_resetSuccess(self):
        result = email.resetSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')


class resetApiTest(unittest.TestCase):
    """重置密码"""

    def test_resetInvalid(self):
        result = reset.resetInvalid()
        self.assertEqual(result["status"], 219)
        self.assertEqual(result["message"],
                         "The confirmation code has expired. Please click 'Forget password' to obtain a new one.")

        # def test_resetWrongCF(self):
        #     result = reset.resetWrongCF()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')

        # def test_resetPwdIllegal(self):
        #     result = reset.resetPwdIllegal()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')
        #
        # def test_resetCFNone(self):
        #     result = reset.resetCFNone()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')
        #
        # def test_resetPwdNone(self):
        #     result = reset.resetPwdNone()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')
        #
        # def test_resetCFEmpty(self):
        #     result = reset.resetCFEmpty()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')
        #
        # def test_resetPwdEmpty(self):
        #     result = reset.resetPwdEmpty()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')
        #
        # def test_resetPwdless(self):
        #     result = reset.resetPwdless()
        #     self.assertEqual(result["status"], 128)
        #     self.assertEqual(result["message"],
        #                      'enter a password more than 6 numbers or letters in length, try again please.')
        #
        # def test_resetPwdMin(self):
        #     result = reset.resetPwdMin()
        #     self.assertEqual(result["status"], 200)
        #     self.assertEqual(result["message"], 'Operation is successful.')
        #
        # def test_resetPwdMax(self):
        #     result = reset.resetPwdMax()
        #     self.assertEqual(result["status"], 200)
        #     self.assertEqual(result["message"], 'Operation is successful.')
        #
        # def test_resetPwdOut(self):
        #     result = reset.resetPwdOut()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')
        #
        # def test_resetPwdInt(self):
        #     result = reset.resetPwdInt()
        #     self.assertEqual(result["status"], 400)
        #     self.assertEqual(result["message"], 'Invalid request data format.')
        #
        # def test_resetSuccess(self):
        #     result = reset.resetSuccess()
        #     self.assertEqual(result["status"], 200)
        #     self.assertEqual(result["message"], 'Operation is successful.')


class DashboardApiTest(unittest.TestCase):
    """获取各报表前7数据"""

    def test_mileageSuccess(self):
        result = Dashboard.mileageSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_driving_timeSuccess(self):
        result = Dashboard.driving_timeSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_fuelSuccess(self):
        result = Dashboard.fuelSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_speedSuccess(self):
        result = Dashboard.speedSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_temperatureSuccess(self):
        result = Dashboard.temperatureSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_visitSuccess(self):
        result = Dashboard.visitSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_maintenceSuccess(self):
        result = Dashboard.maintenceSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_IFIASuccess(self):
        result = Dashboard.IFIASuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_NOcookie(self):
        result = Dashboard.NOcookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')


class notificationApiTest(unittest.TestCase):
    """"获取提醒标签列表"""

    def test_notificationNocookie(self):
        result = notification.notificationNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_notificationSuccess(self):
        result = notification.notificationSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')


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

    def test_timelineSTStr(self):
        result = timeline.timelineSTStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_timelineETStr(self):
        result = timeline.timelineETStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class poisApiTest(unittest.TestCase):
    """获取poi列表"""

    def test_poisNocookie(self):
        result = pois.poisNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_poisSuccess(self):
        result = pois.poisSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_poisEmpty(self):
        result = pois.poisEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_poisNone(self):
        result = pois.poisNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_poisPSizaNone(self):
        result = pois.poisPSizaNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_poisStr(self):
        result = pois.poisStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class AddpoiApiTest(unittest.TestCase):
    """添加poi"""

    def test_AddpoiNocookie(self):
        result = Addpoi.AddpoiNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_AddpoiSuccess(self):
        result = Addpoi.AddpoiSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AddpoiSuccessNoalert(self):
        result = Addpoi.AddpoiSuccessNoalert()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_AddpoiNameEmpty(self):
        result = Addpoi.AddpoiNameEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiARSEmpty(self):
        result = Addpoi.AddpoiARSEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiPathEmpty(self):
        result = Addpoi.AddpoiPathEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiREmpty(self):
        result = Addpoi.AddpoiREmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiLtEmpty(self):
        result = Addpoi.AddpoiLtEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiLgEmpty(self):
        result = Addpoi.AddpoiLgEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiEAEmpty(self):
        result = Addpoi.AddpoiEAEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiOAEmpty(self):
        result = Addpoi.AddpoiOAEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoitidsEmpty(self):
        result = Addpoi.AddpoitidsEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNameNone(self):
        result = Addpoi.AddpoiNameNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiARSNone(self):
        result = Addpoi.AddpoiARSNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiPathNone(self):
        result = Addpoi.AddpoiPathNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiRNone(self):
        result = Addpoi.AddpoiRNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiLtNone(self):
        result = Addpoi.AddpoiLtNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiLgNone(self):
        result = Addpoi.AddpoiLgNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiEANone(self):
        result = Addpoi.AddpoiEANone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiOANone(self):
        result = Addpoi.AddpoiOANone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoitidsNone(self):
        result = Addpoi.AddpoitidsNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoname(self):
        result = Addpoi.AddpoiNoname()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoaddress(self):
        result = Addpoi.AddpoiNoaddress()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoAP(self):
        result = Addpoi.AddpoiNoAP()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoR(self):
        result = Addpoi.AddpoiNoR()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoLT(self):
        result = Addpoi.AddpoiNoLT()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoLG(self):
        result = Addpoi.AddpoiNoLG()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoaEA(self):
        result = Addpoi.AddpoiNoaEA()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoOA(self):
        result = Addpoi.AddpoiNoOA()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNoTids(self):
        result = Addpoi.AddpoiNoTids()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiNameInt(self):
        result = Addpoi.AddpoiNameInt()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiRStr(self):
        result = Addpoi.AddpoiRStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiLtStr(self):
        result = Addpoi.AddpoiLtStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiLgStr(self):
        result = Addpoi.AddpoiLgStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiEAStr(self):
        result = Addpoi.AddpoiEAStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_AddpoiOAStr(self):
        result = Addpoi.AddpoiOAStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class EditPOIApiTest(unittest.TestCase):
    """修改poi"""

    def test_EditPOINocookie(self):
        result = EditPOI.EditPOINocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_EditPOINameSuccess(self):
        result = EditPOI.EditPOINameSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EditPOIAPSuccess(self):
        result = EditPOI.EditPOIAPSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EditPOIEASuccess(self):
        result = EditPOI.EditPOIEASuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EditPOIOASuccess(self):
        result = EditPOI.EditPOIOASuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EditPOITidsSuccess(self):
        result = EditPOI.EditPOITidsSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_EditPOINameEmpty(self):
        result = EditPOI.EditPOINameEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIPathEmpty(self):
        result = EditPOI.EditPOIPathEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIEAEmpty(self):
        result = EditPOI.EditPOIEAEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIOAEmpty(self):
        result = EditPOI.EditPOIOAEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOItidsEmpty(self):
        result = EditPOI.EditPOItidsEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOINameNone(self):
        result = EditPOI.EditPOINameNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIPathNone(self):
        result = EditPOI.EditPOIPathNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIEANone(self):
        result = EditPOI.EditPOIEANone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIOANone(self):
        result = EditPOI.EditPOIOANone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOItidsNone(self):
        result = EditPOI.EditPOItidsNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOINameInt(self):
        result = EditPOI.EditPOINameInt()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIEAStr(self):
        result = EditPOI.EditPOIEAStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOIOAStr(self):
        result = EditPOI.EditPOIOAStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_EditPOITidsNoExist(self):
        result = EditPOI.EditPOITidsNoExist()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class deletepoiApiTest(unittest.TestCase):
    """删除poi"""

    def test_deletePoiNocookie(self):
        result = deletepoi.deletePoiNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_deletePoiSuccess(self):
        result = deletepoi.deletePoiSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')


class GEOApiTest(unittest.TestCase):
    """获取围栏列表"""

    def test_geoNocookie(self):
        result = GEO.geoNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_geoSuccess(self):
        result = GEO.geoSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_geoEmpty(self):
        result = GEO.geoEmpty()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_geoNone(self):
        result = GEO.geoNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_geoPSizaNone(self):
        result = GEO.geoPSizaNone()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_geoStr(self):
        result = GEO.geoStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')

    def test_geoPSStr(self):
        result = GEO.geoPSStr()
        self.assertEqual(result["status"], 400)
        self.assertEqual(result["message"], 'Invalid request data format.')


class AddgeoApiTest(unittest.TestCase):
    """新增围栏"""

    def test_geoNocookie(self):
        result = Addgeo.geoNocookie()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_geoCircleSuccess(self):
        result = Addgeo.geoCircleSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_geoPolygonSuccess(self):
        result = Addgeo.geoPolygonSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')

    def test_geoNameRepeat(self):
        result = Addgeo.geoNameRepeat()
        self.assertEqual(result['status'], 918)
        self.assertEqual(result['message'], 'Name has existed.')

    def test_geoNameMin(self):
        result = Addgeo.geoNameMin()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoNameMax(self):
        result = Addgeo.geoNameMax()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoNameOut(self):
        result = Addgeo.geoNameOut()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoNameEmpty(self):
        result = Addgeo.geoNameEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoNameNone(self):
        result = Addgeo.geoNameNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoNameInt(self):
        result = Addgeo.geoNameInt()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoNameNo(self):
        result = Addgeo.geoNameNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoShapeNoExist(self):
        result = Addgeo.geoShapeNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoShapeStr(self):
        result = Addgeo.geoShapeStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoShapeEmpty(self):
        result = Addgeo.geoShapeEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoShapeNone(self):
        result = Addgeo.geoShapeNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoShapeIncorrect(self):
        result = Addgeo.geoShapeIncorrect()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoShapeNo(self):
        result = Addgeo.geoShapeNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoPolygonEmpty(self):
        result = Addgeo.geoPolygonEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoCicleEmpty(self):
        result = Addgeo.geoCicleEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoPolygonNone(self):
        result = Addgeo.geoPolygonNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoCicleNone(self):
        result = Addgeo.geoCicleNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoTypeInvalid(self):
        result = Addgeo.geoTypeInvalid()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoTypeNo(self):
        result = Addgeo.geoTypeNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoEnterAlert0(self):
        result = Addgeo.geoEnterAlert0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoEnterAlertNoExist(self):
        result = Addgeo.geoEnterAlertNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoEnterAlertStr(self):
        result = Addgeo.geoEnterAlertStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoEnterAlertEmpty(self):
        result = Addgeo.geoEnterAlertEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoEnterAlertNone(self):
        result = Addgeo.geoEnterAlertNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoEnterAlertNo(self):
        result = Addgeo.geoEnterAlertNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoOutAlert0(self):
        result = Addgeo.geoOutAlert0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoOutAlertNoExist(self):
        result = Addgeo.geoOutAlertNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoOutAlertStr(self):
        result = Addgeo.geoOutAlertStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoOutAlertEmpty(self):
        result = Addgeo.geoOutAlertEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoOutAlertNone(self):
        result = Addgeo.geoOutAlertNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoOutAlertNo(self):
        result = Addgeo.geoOutAlertNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoSchedule2(self):
        result = Addgeo.geoSchedule2()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoSchedule3(self):
        result = Addgeo.geoSchedule3()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoSchedule4(self):
        result = Addgeo.geoSchedule4()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoScheduleEmpty(self):
        result = Addgeo.geoScheduleEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoScheduleNone(self):
        result = Addgeo.geoScheduleNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoScheduleNo(self):
        result = Addgeo.geoScheduleNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoTidNoNotifications(self):
        result = Addgeo.geoTidNoNotifications()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoTidStr(self):
        result = Addgeo.geoTidStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoTidEmpty(self):
        result = Addgeo.geoTidEmpty()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_geoTidNoExist(self):
        result = Addgeo.geoTidNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoTidNone(self):
        result = Addgeo.geoTidNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_geoTidNo(self):
        result = Addgeo.geoTidNo()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')


class EditgeoApiTest(unittest.TestCase):
    """编辑围栏"""

    def test_regionEditFail(self):
        result = Editgeo.regionEditFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_regionEditNoParam(self):
        result = Editgeo.regionEditNoParam()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditNameMin(self):
        result = Editgeo.regionEditNameMin()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditNameRepeat(self):
        result = Editgeo.regionEditNameRepeat()
        self.assertEqual(result['status'], 918)
        self.assertEqual(result['message'], 'Name has existed.')

    def test_regionEditNameMax(self):
        result = Editgeo.regionEditNameMax()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditNameOut(self):
        result = Editgeo.regionEditNameOut()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditNameEmpty(self):
        result = Editgeo.regionEditNameEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditNameNone(self):
        result = Editgeo.regionEditNameNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditNameInt(self):
        result = Editgeo.regionEditNameInt()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditShapeNoExist(self):
        result = Editgeo.regionEditShapeNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditShapeStr(self):
        result = Editgeo.regionEditShapeStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditShapeEmpty(self):
        result = Editgeo.regionEditShapeEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditShapeNone(self):
        result = Editgeo.regionEditShapeNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditShapeIncorrect(self):
        result = Editgeo.regionEditShapeIncorrect()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditPolygonEmpty(self):
        result = Editgeo.regionEditPolygonEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditCicleEmpty(self):
        result = Editgeo.regionEditCicleEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditPolygonNone(self):
        result = Editgeo.regionEditPolygonNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditCicleNone(self):
        result = Editgeo.regionEditCicleNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditTypeInvalid(self):
        result = Editgeo.regionEditTypeInvalid()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditEnterAlert0(self):
        result = Editgeo.regionEditEnterAlert0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditEnterAlertNoExist(self):
        result = Editgeo.regionEditEnterAlertNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditEnterAlertStr(self):
        result = Editgeo.regionEditEnterAlertStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditEnterAlertEmpty(self):
        result = Editgeo.regionEditEnterAlertEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditEnterAlertNone(self):
        result = Editgeo.regionEditEnterAlertNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditOutAlert0(self):
        result = Editgeo.regionEditOutAlert0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditOutAlertNoExist(self):
        result = Editgeo.regionEditOutAlertNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditOutAlertStr(self):
        result = Editgeo.regionEditOutAlertStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditOutAlertEmpty(self):
        result = Editgeo.regionEditOutAlertEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditOutAlertNone(self):
        result = Editgeo.regionEditOutAlertNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditSchedule2(self):
        result = Editgeo.regionEditSchedule2()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditSchedule3(self):
        result = Editgeo.regionEditSchedule3()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditSchedule4(self):
        result = Editgeo.regionEditSchedule4()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditScheduleEmpty(self):
        result = Editgeo.regionEditScheduleEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditScheduleNone(self):
        result = Editgeo.regionEditScheduleNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditTidNoNotifications(self):
        result = Editgeo.regionEditTidNoNotifications()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditTidStr(self):
        result = Editgeo.regionEditTidStr()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditTidEmpty(self):
        result = Editgeo.regionEditTidEmpty()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_regionEditTidNoExist(self):
        result = Editgeo.regionEditTidNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_regionEditTidNone(self):
        result = Editgeo.regionEditTidNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')


class deletegeoApiTest(unittest.TestCase):
    """删除围栏"""

    def test_deletegeoNocookie(self):
        result = deletegeo.deletegeoNocookie()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_deletegeoSuccess(self):
        result = deletegeo.deletegeoSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')


class trackersApiTest(unittest.TestCase):
    """获取终端信息"""

    def test_trackerSuccess(self):
        result = Trackers.trackerSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackersFail(self):
        result = Trackers.trackersFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')


class trackerApiTest(unittest.TestCase):
    """修改终端信息"""

    def test_trackerSuccess(self):
        result = Tracker.trackerSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackerFail(self):
        result = Tracker.trackerFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_trackerErrorId(self):
        result = Tracker.trackerErrorId()
        self.assertEqual(result['status'], 403)
        self.assertEqual(result['message'], 'Permission is denied.')

    def test_trackerNoParam(self):
        result = Tracker.trackerNoParam()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackerAlias(self):
        result = Tracker.trackerAlias()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackerAliasEmpty(self):
        result = Tracker.trackerAliasEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerAliasNone(self):
        result = Tracker.trackerAliasNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerIcon(self):
        result = Tracker.trackerIcon()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackerIconNoExist(self):
        result = Tracker.trackerIconNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerIconEmpty(self):
        result = Tracker.trackerIconEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerIconNone(self):
        result = Tracker.trackerIconNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerPowerSavingOff(self):
        result = Tracker.trackerPowerSavingOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackerPowerSavingOpen(self):
        result = Tracker.trackerPowerSavingOpen()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackerPowerSavingEmpty(self):
        result = Tracker.trackerPowerSavingEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerPowerSavingNone(self):
        result = Tracker.trackerPowerSavingNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')


class trackerAddApiTest(unittest.TestCase):
    """添加终端"""

    def test_trackerAddSuccess(self):
        result = TrackerAdd.trackerAddSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_trackerAddFail(self):
        result = TrackerAdd.trackerAddFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_trackerAddIsUsed(self):
        result = TrackerAdd.trackerAddIsUsed()
        self.assertEqual(result['status'], 315)
        self.assertEqual(result['message'], 'SN is used.')

    def test_trackerAddInvaild(self):
        result = TrackerAdd.trackerAddInvaild()
        self.assertEqual(result['status'], 316)
        self.assertEqual(result['message'], 'Invalid activation code and/or Serial Number')

    def test_trackerAddError(self):
        result = TrackerAdd.trackerAddError()
        self.assertEqual(result['status'], 316)
        self.assertEqual(result['message'], 'Invalid activation code and/or Serial Number')

    def test_trackerAddNoSn(self):
        result = TrackerAdd.trackerAddNoSn()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerAddNoActivationCode(self):
        result = TrackerAdd.trackerAddNoActivationCode()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerAddSnEmpty(self):
        result = TrackerAdd.trackerAddSnEmpty()
        self.assertEqual(result['status'], 316)
        self.assertEqual(result['message'], 'Invalid activation code and/or Serial Number')

    def test_trackerAddSnNone(self):
        result = TrackerAdd.trackerAddSnNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_trackerAddActivationCodeEmpty(self):
        result = TrackerAdd.trackerAddActivationCodeEmpty()
        self.assertEqual(result['status'], 316)
        self.assertEqual(result['message'], 'Invalid activation code and/or Serial Number')

    def test_trackerAddActivationCodeNone(self):
        result = TrackerAdd.trackerAddActivationCodeNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')


class EmailApiTest(unittest.TestCase):
    """修改account邮箱"""

    def test_emailChangeSuccess(self):
        result = Email.emailChangeSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_emailChangeFail(self):
        result = Email.emailChangeFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_emailChangeAleady(self):
        result = Email.emailChangeAleady()
        self.assertEqual(result['status'], 216)
        self.assertEqual(result['message'],
                         'This email address has already been registered. Please use another one. To recover password click Forgot Password.')

    def test_emailChangeInvaildEmailFormat(self):
        result = Email.emailChangeInvaildEmailFormat()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_emailChangeInvaildPassword(self):
        result = Email.emailChangeInvaildPassword()
        self.assertEqual(result['status'], 217)
        self.assertEqual(result['message'], 'Password error.')

    def test_emailChanageEmptyEmail(self):
        result = Email.emailChanageEmptyEmail()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_emailChangeEmptyPassword(self):
        result = Email.emailChangeEmptyPassword()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_emailChangeEmailNone(self):
        result = Email.emailChangeEmailNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_emailChangePasswordNone(self):
        result = Email.emailChangePasswordNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_emailChangeNoEmail(self):
        result = Email.emailChangeEmailNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_emailChangeNoPassword(self):
        result = Email.emailChangeNoPassword()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')


class registerApiTest(unittest.TestCase):
    """注册"""

    def test_registerSuccess(self):
        result = Register.registerSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_registerEmpty(self):
        result = Register.registerEmpty()
        self.assertEqual(result['status'], 912)
        self.assertEqual(result['message'], 'Invalid email format.')

    def test_registerNone(self):
        result = Register.registerNone()
        self.assertEqual(result['status'], 912)
        self.assertEqual(result['message'], 'Invalid email format.')

    def test_registerNoParam(self):
        result = Register.registerNoParam()
        self.assertEqual(result['status'], 912)
        self.assertEqual(result['message'], 'Invalid email format.')

    def test_registerInvaildEmailFormat(self):
        result = Register.registerInvaildEmailFormat()
        self.assertEqual(result['status'], 912)
        self.assertEqual(result['message'], 'Invalid email format.')

    def test_registerRepeat(self):
        result = Register.registerRepeat()
        self.assertEqual(result['status'], 216)
        self.assertEqual(result['message'],
                         'This email address has already been registered. Please use another one. To recover password click Forgot Password.')


class profileApiTest(unittest.TestCase):
    """获取profile"""

    def test_profileSuccess(self):
        result = Profile.profileSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_profileFail(self):
        result = Profile.profileFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')


class notificationEditApiTest(unittest.TestCase):
    """告警设置"""

    def test_notificationEditFail(self):
        result = NotificationEdit.notificationEditFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_notificationEditError(self):
        result = NotificationEdit.notificationEditErrorTid()
        self.assertEqual(result['status'], 403)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_notificationEditMaxTemp0(self):
        result = NotificationEdit.notificationEditMaxTemp0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditMaxTempBelowZero(self):
        result = NotificationEdit.notificationEditMaxTempBelowZero()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditMaxTempOver(self):
        result = NotificationEdit.notificationEditMaxTempOver()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditMaxTempEmpty(self):
        result = NotificationEdit.notificationEditMaxTempEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditMaxTempNone(self):
        result = NotificationEdit.notificationEditMaxTempNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditMinTemp0(self):
        result = NotificationEdit.notificationEditMinTemp0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditMinTempBelowZero(self):
        result = NotificationEdit.notificationEditMinTempBelowZero()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditMinTempOver(self):
        result = NotificationEdit.notificationEditMinTempOver()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditMinTempEmpty(self):
        result = NotificationEdit.notificationEditMinTempEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditMinTempNone(self):
        result = NotificationEdit.notificationEditMinTempNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditMaxTempLessMinTemp(self):
        result = NotificationEdit.notificationEditMaxTempLessMinTemp()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditExtsEmpty(self):
        result = NotificationEdit.notificationEditExtsEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditExtsNone(self):
        result = NotificationEdit.notificationEditExtsNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditDoorSensorEmpty(self):
        result = NotificationEdit.notificationEditDoorSensorEmpty()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditTempSensorEmpty(self):
        result = NotificationEdit.notificationEditTempSensorEmpty()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditDoorSensorNone(self):
        result = NotificationEdit.notificationEditDoorSensorNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditTempSensorNone(self):
        result = NotificationEdit.notificationEditTempSensorNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSosEmailNone(self):
        result = NotificationEdit.notificationEditSosEmailNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSosEmail(self):
        result = NotificationEdit.notificationEditSosEmail()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSosEmails(self):
        result = NotificationEdit.notificationEditSosEmails()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSosEmailsOver(self):
        result = NotificationEdit.notificationEditSosEmailsOver()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSosEmailEmpty(self):
        result = NotificationEdit.notificationEditSosEmailEmpty()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSosEmailInvaildFormat(self):
        result = NotificationEdit.notificationEditSosEmailInvaildFormat()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSosEmailRepeat(self):
        result = NotificationEdit.notificationEditSosEmailRepeat()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSosEmailSelf(self):
        result = NotificationEdit.notificationEditSosEmailSelf()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditNotificationEmpty(self):
        result = NotificationEdit.notificationEditNotificationEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditNotificationNone(self):
        result = NotificationEdit.notificationEditNotificationNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditPushEmpty(self):
        result = NotificationEdit.notificationEditPushEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditPushNone(self):
        result = NotificationEdit.notificationEditPushNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditPushOff(self):
        result = NotificationEdit.notificationEditPushOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditPushOn(self):
        result = NotificationEdit.notificationEditPushOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditEmailEmpty(self):
        result = NotificationEdit.notificationEditEmailEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditEmailNone(self):
        result = NotificationEdit.notificationEditEmailNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditEmailOff(self):
        result = NotificationEdit.notificationEditEmailOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditEmailOn(self):
        result = NotificationEdit.notificationEditEmailOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsEmpty(self):
        result = NotificationEdit.notificationEditSmsEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsNone(self):
        result = NotificationEdit.notificationEditSmsNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsRegionEmpty(self):
        result = NotificationEdit.notificationEditSmsRegionEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsRegionNone(self):
        result = NotificationEdit.notificationEditSmsRegionNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsRegionOff(self):
        result = NotificationEdit.notificationEditSmsRegionOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsRegionOn(self):
        result = NotificationEdit.notificationEditSmsRegionOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsPoiEmpty(self):
        result = NotificationEdit.notificationEditSmsPoiEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsPoiNone(self):
        result = NotificationEdit.notificationEditSmsPoiNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsPoiOff(self):
        result = NotificationEdit.notificationEditSmsPoiOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsPoiOn(self):
        result = NotificationEdit.notificationEditSmsPoiOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsTempEmpty(self):
        result = NotificationEdit.notificationEditSmsTempEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsTempNone(self):
        result = NotificationEdit.notificationEditSmsTempNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsTempOff(self):
        result = NotificationEdit.notificationEditSmsTempOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsTempOn(self):
        result = NotificationEdit.notificationEditSmsTempOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsIllegalmoveEmpty(self):
        result = NotificationEdit.notificationEditSmsIllegalmoveEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsIllegalmoveNone(self):
        result = NotificationEdit.notificationEditSmsIllegalmoveNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsIllegalmoveOff(self):
        result = NotificationEdit.notificationEditSmsIllegalmoveOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsIllegalmoveOn(self):
        result = NotificationEdit.notificationEditSmsIllegalmoveOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsHeartbeatlostEmpty(self):
        result = NotificationEdit.notificationEditSmsHeartbeatlostEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsHeartbeatlostNone(self):
        result = NotificationEdit.notificationEditSmsHeartbeatlostNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSmsHeartbeatlostOff(self):
        result = NotificationEdit.notificationEditSmsHeartbeatlostOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSmsHeartbeatlostOn(self):
        result = NotificationEdit.notificationEditSmsHeartbeatlostOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSpeedlimitEmpty(self):
        result = NotificationEdit.notificationEditSpeedlimitEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSpeedlimitNone(self):
        result = NotificationEdit.notificationEditSpeedlimitEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSpeedlimit0(self):
        result = NotificationEdit.notificationEditSpeedlimit0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSpeedlimit(self):
        result = NotificationEdit.notificationEditSpeedlimit()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditSpeedlimitNegative(self):
        result = NotificationEdit.notificationEditSpeedlimitNegative()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditSpeedlimitOver(self):
        result = NotificationEdit.notificationEditSpeedlimitOver()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditContactemailEmpty(self):
        result = NotificationEdit.notificationEditContactemailEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditContactemailNone(self):
        result = NotificationEdit.notificationEditContactemailNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditContactemailPrimaryAccount(self):
        result = NotificationEdit.notificationEditContactemailPrimaryAccount()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditContactemailNoExist(self):
        result = NotificationEdit.notificationEditContactemailNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditContactmobileEmpty(self):
        result = NotificationEdit.notificationEditContactmobileEmpty()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditContactmobileNone(self):
        result = NotificationEdit.notificationEditContactmobileNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditContactmobilePrimaryAccount(self):
        result = NotificationEdit.notificationEditContactmobilePrimaryAccount()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditContactmobileNoExist(self):
        result = NotificationEdit.notificationEditContactmobileNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoicesendEmpty(self):
        result = NotificationEdit.notificationEditVoicesendEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoicesendNone(self):
        result = NotificationEdit.notificationEditVoicesendNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoicesendOff(self):
        result = NotificationEdit.notificationEditVoicesendOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoicesendOn(self):
        result = NotificationEdit.notificationEditVoicesendOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceNoParam(self):
        result = NotificationEdit.notificationEditVoiceNoParam()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceNone(self):
        result = NotificationEdit.notificationEditVoiceNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceRegionEmpty(self):
        result = NotificationEdit.notificationEditVoiceRegionEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceRegionNone(self):
        result = NotificationEdit.notificationEditVoiceRegionNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceRegionOff(self):
        result = NotificationEdit.notificationEditVoiceRegionOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceRegionOn(self):
        result = NotificationEdit.notificationEditVoiceRegionOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoicePoiEmpty(self):
        result = NotificationEdit.notificationEditVoicePoiEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoicePoiNone(self):
        result = NotificationEdit.notificationEditVoicePoiNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoicePoiOff(self):
        result = NotificationEdit.notificationEditVoicePoiOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoicePoiOn(self):
        result = NotificationEdit.notificationEditVoicePoiOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceTempEmpty(self):
        result = NotificationEdit.notificationEditVoiceTempEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceTempNone(self):
        result = NotificationEdit.notificationEditVoiceTempNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceTempOff(self):
        result = NotificationEdit.notificationEditVoiceTempOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceTempOn(self):
        result = NotificationEdit.notificationEditVoiceTempOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceIllegalmoveEmpty(self):
        result = NotificationEdit.notificationEditVoiceIllegalmoveEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceIllegalmoveNone(self):
        result = NotificationEdit.notificationEditVoiceIllegalmoveNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceIllegalmoveOff(self):
        result = NotificationEdit.notificationEditVoiceIllegalmoveOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceIllegalmoveOn(self):
        result = NotificationEdit.notificationEditVoiceIllegalmoveOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceHeartbeatlostEmpty(self):
        result = NotificationEdit.notificationEditVoiceHeartbeatlostEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceHeartbeatlostNone(self):
        result = NotificationEdit.notificationEditVoiceHeartbeatlostNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditVoiceHeartbeatlostOff(self):
        result = NotificationEdit.notificationEditVoiceHeartbeatlostOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditVoiceHeartbeatlostOn(self):
        result = NotificationEdit.notificationEditVoiceHeartbeatlostOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsNoParam(self):
        result = NotificationEdit.notificationEditOptionsNoParam()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsNone(self):
        result = NotificationEdit.notificationEditOptionsNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsUsbdisconnectEmpty(self):
        result = NotificationEdit.notificationEditOptionsUsbdisconnectEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsUsbdisconnectNone(self):
        result = NotificationEdit.notificationEditOptionsUsbdisconnectNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsUsbdisconnectOff(self):
        result = NotificationEdit.notificationEditOptionsUsbdisconnectOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionUsbdisconnectOn(self):
        result = NotificationEdit.notificationEditOptionUsbdisconnectOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsTempEmpty(self):
        result = NotificationEdit.notificationEditOptionsTempEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsTempNone(self):
        result = NotificationEdit.notificationEditOptionsTempNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsTempOff(self):
        result = NotificationEdit.notificationEditOptionsTempOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsTempOn(self):
        result = NotificationEdit.notificationEditOptionsTempOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsIllegalmoveEmpty(self):
        result = NotificationEdit.notificationEditOptionsIllegalmoveEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsIllegalmoveNone(self):
        result = NotificationEdit.notificationEditOptionsIllegalmoveNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsIllegalmoveOff(self):
        result = NotificationEdit.notificationEditOptionsIllegalmoveOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsIllegalmoveOn(self):
        result = NotificationEdit.notificationEditOptionsIllegalmoveOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsOverspeedEmpty(self):
        result = NotificationEdit.notificationEditOptionsOverspeedEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsOverspeedNone(self):
        result = NotificationEdit.notificationEditOptionsOverspeedNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsOverspeedOff(self):
        result = NotificationEdit.notificationEditOptionsOverspeedOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsOverspeedOn(self):
        result = NotificationEdit.notificationEditOptionsOverspeedOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsPoiEmpty(self):
        result = NotificationEdit.notificationEditOptionsPoiEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPoiNone(self):
        result = NotificationEdit.notificationEditOptionsPoiNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPoiOff(self):
        result = NotificationEdit.notificationEditOptionsPoiOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsPoiOn(self):
        result = NotificationEdit.notificationEditOptionsPoiOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsHeartbeatlostEmpty(self):
        result = NotificationEdit.notificationEditOptionsHeartbeatlostEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsHeartbeatlostNone(self):
        result = NotificationEdit.notificationEditOptionsHeartbeatlostNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsHeartbeatlostOff(self):
        result = NotificationEdit.notificationEditOptionsHeartbeatlostOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsHeartbeatlostOn(self):
        result = NotificationEdit.notificationEditOptionsHeartbeatlostOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsPowerfullEmpty(self):
        result = NotificationEdit.notificationEditOptionsPowerfullEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPowerfullNone(self):
        result = NotificationEdit.notificationEditOptionsPowerfullNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPowerfullOff(self):
        result = NotificationEdit.notificationEditOptionsPowerfullOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsPowerfullOn(self):
        result = NotificationEdit.notificationEditOptionsPowerfullOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsRegionEmpty(self):
        result = NotificationEdit.notificationEditOptionsRegionEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsRegionNone(self):
        result = NotificationEdit.notificationEditOptionsRegionNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsRegionOff(self):
        result = NotificationEdit.notificationEditOptionsRegionOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsRegionOn(self):
        result = NotificationEdit.notificationEditOptionsRegionOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificaitonEditOptionsPowerlowEmpty(self):
        result = NotificationEdit.notificaitonEditOptionsPowerlowEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPowerlowNone(self):
        result = NotificationEdit.notificationEditOptionsPowerlowNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPowerlowOff(self):
        result = NotificationEdit.notificationEditOptionsPowerlowOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsPowerlowOn(self):
        result = NotificationEdit.notificationEditOptionsPowerlowOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsStoppingEmpty(self):
        result = NotificationEdit.notificationEditOptionsStoppingEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsStoppingNone(self):
        result = NotificationEdit.notificationEditOptionsStoppingNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsStoppingOff(self):
        result = NotificationEdit.notificationEditOptionsStoppingOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsStoppingOn(self):
        result = NotificationEdit.notificationEditOptionsStoppingOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsPoweroffEmpty(self):
        result = NotificationEdit.notificationEditOptionsPoweroffEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPoweroffNone(self):
        result = NotificationEdit.notificationEditOptionsPoweroffNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsPoweroffOff(self):
        result = NotificationEdit.notificationEditOptionsPoweroffOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsPoweroffOn(self):
        result = NotificationEdit.notificationEditOptionsPoweroffOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsIllegalshakeEmpty(self):
        result = NotificationEdit.notificationEditOptionsIllegalshakeEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsIllegalshakeNone(self):
        result = NotificationEdit.notificationEditOptionsIllegalshakeNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_notificationEditOptionsIllegalshakeOff(self):
        result = NotificationEdit.notificationEditOptionsIllegalshakeOff()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_notificationEditOptionsIllegalshakeOn(self):
        result = NotificationEdit.notificationEditOptionsIllegalshakeOn()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')


class labelGetApiTest(unittest.TestCase):
    """获取标签列表"""

    def test_labelGetSuccess(self):
        result = LabelGet.labelGetSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelGetFail(self):
        result = LabelGet.labelGetFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_labelGetPageEmpty(self):
        result = LabelGet.labelGetPageEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelGetPageNone(self):
        result = LabelGet.labelGetPageNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelGetPage0(self):
        result = LabelGet.labelGetPage0()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelGetPageNegative(self):
        result = LabelGet.labelGetPageNegative()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelGetPageMax(self):
        result = LabelGet.labelGetPageMax()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelGetNoParam(self):
        result = LabelGet.labelGetNoParam()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')


class labelAddApiTest(unittest.TestCase):
    """添加标签"""

    def test_labelAddSuccess(self):
        result = LabelAdd.labelAddSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelAddFail(self):
        result = LabelAdd.labelAddFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_labelAddNameRepeat(self):
        result = LabelAdd.labelAddNameRepeat()
        self.assertEqual(result['status'], 918)
        self.assertEqual(result['message'], 'Name has existed.')

    def test_labelAddNameEmpty(self):
        result = LabelAdd.labelAddNameEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddNameOver(self):
        result = LabelAdd.labelAddNameOver()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddNameNone(self):
        result = LabelAdd.labelAddNameNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddColorEmpty(self):
        result = LabelAdd.labelAddColorEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddColorNoExist(self):
        result = LabelAdd.labelAddColorNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddColorNone(self):
        result = LabelAdd.labelAddColorNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddTidNoExist(self):
        result = LabelAdd.labelAddTidNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddTids(self):
        result = LabelAdd.labelAddTids()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelAddTidEmpty(self):
        result = LabelAdd.labelAddTidEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddTidNone(self):
        result = LabelAdd.labelAddTidNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddNoName(self):
        result = LabelAdd.labelAddNoName()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddNoColor(self):
        result = LabelAdd.labelAddNoColor()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelAddNoTid(self):
        result = LabelAdd.labelAddNoTid()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')


class labelEditApiTest(unittest.TestCase):
    """编辑标签"""

    def test_labelEditSuccess(self):
        result = LabelEdit.labelEditSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelEditFail(self):
        result = LabelEdit.labelEditFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_labelEditErrorId(self):
        result = LabelEdit.labelEditErrorId()
        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], 'Not found.')

    def test_labelEditNoParam(self):
        result = LabelEdit.labelEditNoParam()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelEditNameEmpty(self):
        result = LabelEdit.labelEditNameEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditNameNone(self):
        result = LabelEdit.labelEditNameNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditNameOver(self):
        result = LabelEdit.labelEditNameOver()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditColorEmpty(self):
        result = LabelEdit.labelEditColorEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditColorNone(self):
        result = LabelEdit.labelEditColorNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditColorNoExist(self):
        result = LabelEdit.labelEditColorNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditTidNoExist(self):
        result = LabelEdit.labelEditTidNoExist()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditTids(self):
        result = LabelEdit.labelEditTids()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelEditTidEmpty(self):
        result = LabelEdit.labelEditTidEmpty()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')

    def test_labelEditTidNone(self):
        result = LabelEdit.labelEditTidNone()
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['message'], 'Invalid request data format.')


class labelDelApiTest(unittest.TestCase):
    """删除标签"""

    def test_labelDelSuccess(self):
        result = LabelDel.labelDelSuccess()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Operation is successful.')

    def test_labelDelFail(self):
        result = LabelDel.labelDelFail()
        self.assertEqual(result['status'], 401)
        self.assertEqual(result['message'], 'Authenticated failed.')

    def test_labelDelErrorId(self):
        result = LabelDel.labelDelErrorId()
        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], 'Not found.')


class logoutApiTest(unittest.TestCase):
    """登出"""

    def test_logoutFail(self):
        result = logout.logoutFail()
        self.assertEqual(result["status"], 401)
        self.assertEqual(result["message"], 'Authenticated failed.')

    def test_logoutSuccess(self):
        result = logout.logoutSuccess()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], 'Operation is successful.')
