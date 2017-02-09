# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies
from TestPython.api.POI_GEO import GEO

geo_id = str(GEO.geoSuccess()['data'][0]['id'])
regionEditUrl = "/api/v1/regions/" + geo_id
type = "put"
cookie = Mycookies.Cookies


# 无cookie修改
def regionEditFail():
    data = {
        'name': 'test',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(regionEditUrl, type, data)


# 无参数传递
def regionEditNoParam():
    data = {}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改name为1位
def regionEditNameMin():
    data = {'name': 'Q'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改name为重复的名字
def regionEditNameRepeat():
    data = {'name': 'Q'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改name为50位
def regionEditNameMax():
    data = {'name': 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvb'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改name为51位
def regionEditNameOut():
    data = {'name': 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改name为空字符串
def regionEditNameEmpty():
    data = {'name': ''}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改name为None
def regionEditNameNone():
    data = {'name': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改name为int
def regionEditNameInt():
    data = {'name': 123}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# shape为不存在的值
def regionEditShapeNoExist():
    data = {'shape': 2}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改shape为字符串
def regionEditShapeStr():
    data = {'shape': '1'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改shape为空字符串
def regionEditShapeEmpty():
    data = {'shape': ''}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改shape为None
def regionEditShapeNone():
    data = {'shape': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# shape和围栏类型不匹配
def regionEditShapeIncorrect():
    data = {
        'shape': 0,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ]
    }
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 多边形围栏的值为空
def regionEditPolygonEmpty():
    data = {'shape': 1, 'polygon': []}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 圆形围栏的值为空
def regionEditCicleEmpty():
    data = {'shape': 0, 'circle': {}}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 多边形围栏值为None
def regionEditPolygonNone():
    data = {'shape': 1, 'polygon': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 圆形围栏值为None
def regionEditCicleNone():
    data = {'shape': 0, 'circle': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 围栏的值和类型不匹配
def regionEditTypeInvalid():
    data = {'shape': 1, 'polygon': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982}}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改enter_alert为0
def regionEditEnterAlert0():
    data = {'shape': 0, 'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
            'enter_alert': 0}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改enter_alert为不存在的值
def regionEditEnterAlertNoExist():
    data = {'enter_alert': 2}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改enter_alert为字符串
def regionEditEnterAlertStr():
    data = {'enter_alert': '1'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改enter_alert为空字符串
def regionEditEnterAlertEmpty():
    data = {'enter_alert': ''}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改enter_alert为None
def regionEditEnterAlertNone():
    data = {'enter_alert': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改out_alert为0
def regionEditOutAlert0():
    data = {'out_alert': 0}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改out_alert为不存在的值
def regionEditOutAlertNoExist():
    data = {'out_alert': 2}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改out_alert为字符串
def regionEditOutAlertStr():
    data = {'out_alert': '1'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改out_alert为空字符串
def regionEditOutAlertEmpty():
    data = {'out_alert': ''}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改out_alert为None
def regionEditOutAlertNone():
    data = {'out_alert': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改schedule为2
def regionEditSchedule2():
    data = {'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653}}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改schedule为3
def regionEditSchedule3():
    data = {'schedule': {'type': 3, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'}}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改schedule为4
def regionEditSchedule4():
    data = {
        'schedule': {'type': 4, 'week': [
            {'dow': 0, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
            {'dow': 1, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
            {'dow': 1, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
            {'dow': 2, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
            {'dow': 3, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
            {'dow': 4, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
            {'dow': 5, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
            {'dow': 6, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'}
        ]
                     }
    }
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改schedule为空值
def regionEditScheduleEmpty():
    data = {'schedule': {}}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 修改schedule为None
def regionEditScheduleNone():
    data = {'schedule': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# enter_alert和out_alert为0时，传tid
def regionEditTidNoNotifications():
    data = {'enter_alert': 0, 'out_alert': 0, 'tids': ['898600D6101400027737']}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# tids为字符串
def regionEditTidStr():
    data = {'tids': '898600D6101400027737'}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# tids为空list
def regionEditTidEmpty():
    data = {'tids': []}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# 错误的tid
def regionEditTidNoExist():
    data = {'tids': ['898600D61014000277']}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)


# tids为None
def regionEditTidNone():
    data = {'tids': None}
    return ApiMethod.testMethod(regionEditUrl, type, data, cookie)
