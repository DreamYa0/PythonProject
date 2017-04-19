# -*- coding: utf-8 -*-
from TestPython.api import ApiMethod
from TestPython.api import Mycookies

geoUrl = "/api/v1/regions"
type = "post"
cookie = Mycookies.Cookies


# 无cookie
def geoNocookie():
    data = {
        'name': '无cookie',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data)


# 创建圆形围栏
def geoCircleSuccess():
    data = {
        'name': '创建圆形围栏1',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 创建多边形围栏
def geoPolygonSuccess():
    data = {
        'name': '创建多边形围栏w02e1',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# name名字重复
def geoNameRepeat():
    data = {
        'name': '创建圆形围栏1',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改name为1位
def geoNameMin():
    data = {
        'name': '1',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改name为50位
def geoNameMax():
    data = {
        'name': 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvb',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改name为51位
def geoNameOut():
    data = {
        'name': 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改name为空字符串
def geoNameEmpty():
    data = {
        'name': '',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改name为None
def geoNameNone():
    data = {
        'name': None,
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改name为int
def geoNameInt():
    data = {
        'name': 123,
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 不传name
def geoNameNo():
    data = {
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# shape为不存在的值
def geoShapeNoExist():
    data = {
        'name': 'shape为不存在的值',
        'shape': 2,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改shape为字符串
def geoShapeStr():
    data = {
        'name': '修改shape为字符串',
        'shape': '1',
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改shape为空字符串
def geoShapeEmpty():
    data = {
        'name': 'c0d5d',
        'shape': '',
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改shape为None
def geoShapeNone():
    data = {
        'name': '修改shape为None',
        'shape': None,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# shape和围栏类型不匹配
def geoShapeIncorrect():
    data = {
        'name': 'shape和围栏类型不匹配',
        'shape': 0,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 不传shape
def geoShapeNo():
    data = {
        'name': '不传shape',
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 多边形围栏的值为空
def geoPolygonEmpty():
    data = {
        'name': '多边形围栏的值为空',
        'shape': 1,
        'polygon': [],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 圆形围栏的值为空
def geoCicleEmpty():
    data = {
        'name': '圆形围栏的值为空',
        'shape': 0,
        'circle': {},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 多边形围栏值为None
def geoPolygonNone():
    data = {
        'name': '多边形围栏值为None',
        'shape': 1,
        'polygon': None,
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 圆形围栏值为None
def geoCicleNone():
    data = {
        'name': '圆形围栏值为None',
        'shape': 0,
        'circle': None,
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 围栏的值和类型不匹配
def geoTypeInvalid():
    data = {
        'name': '<>?sd5f',
        'shape': 0,
        'polygon': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 不传围栏类型
def geoTypeNo():
    data = {
        'name': '不传围栏类型',
        'shape': 0,
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改enter_alert为0
def geoEnterAlert0():
    data = {
        'name': '0sd5f5',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 0,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改enter_alert为不存在的值
def geoEnterAlertNoExist():
    data = {
        'name': '8qw9e7',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 2,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改enter_alert为字符串
def geoEnterAlertStr():
    data = {
        'name': '12d1f23',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': '1',
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改enter_alert为空字符串
def geoEnterAlertEmpty():
    data = {
        'name': '03d2sf',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': '',
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改enter_alert为None
def geoEnterAlertNone():
    data = {
        'name': 'q3we1',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': None,
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 不传enter_alert
def geoEnterAlertNo():
    data = {
        'name': '23wer1223',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'out_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改out_alert为0
def geoOutAlert0():
    data = {
        'name': '89r8q9r',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 0,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改out_alert为不存在的值
def geoOutAlertNoExist():
    data = {
        'name': '05df3',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 2,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改out_alert为字符串
def geoOutAlertStr():
    data = {
        'name': '54r5e53r',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': '1',
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改out_alert为空字符串
def geoOutAlertEmpty():
    data = {
        'name': '6qw45e6',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': '',
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改out_alert为None
def geoOutAlertNone():
    data = {
        'name': '0csd0c22',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': None,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 不传out_alert
def geoOutAlertNo():
    data = {
        'name': '2sd12f13',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'schedule': {'type': 0},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改schedule为2
def geoSchedule2():
    data = {
        'name': 'w12f2ef',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改schedule为3
def geoSchedule3():
    data = {
        'name': '65ef55',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 3, 'hours': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23'},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改schedule为4
def geoSchedule4():
    data = {
        'name': '5qwe4556',
        'shape': 0,
        'circle': {'radius': 156.20, 'latitude': 110199299.03028621, 'longitude': 374528575.6587982},
        'enter_alert': 1,
        'out_alert': 1,
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
                     },
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改schedule为空值
def geoScheduleEmpty():
    data = {
        'name': '8qe7989',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 修改schedule为None
def geoScheduleNone():
    data = {
        'name': '2d1f22df',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': None,
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 不传schedule
def geoScheduleNo():
    data = {
        'name': 'xcv2zv3',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# enter_alert和out_alert为0时，传tid
def geoTidNoNotifications():
    data = {
        'name': '1f2v1f5',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 0,
        'out_alert': 0,
        'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653},
        'tids': ['898600D6101400027737']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# tids为字符串
def geoTidStr():
    data = {
        'name': 'wev15',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653},
        'tids': '898600D6101400027737'
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# tids为空list
def geoTidEmpty():
    data = {
        'name': 'hfgthk2',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653},
        'tids': []
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 错误的tid
def geoTidNoExist():
    data = {
        'name': 'yti5455y',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653},
        'tids': ['898600D61014000277']
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# tids为None
def geoTidNone():
    data = {
        'name': 'bett5',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653},
        'tids': None
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)


# 不传tids
def geoTidNo():
    data = {
        'name': '2qw1e23',
        'shape': 1,
        'polygon': [
            {'latitude': 80495565.29416555, 'longitude': 408793862.3428345},
            {'latitude': 80493779.30159469, 'longitude': 408795407.2952270},
            {'latitude': 80493136.34271201, 'longitude': 408791776.6571045},
            {'latitude': 80495708.17329645, 'longitude': 408792008.3999634}
        ],
        'enter_alert': 1,
        'out_alert': 1,
        'schedule': {'type': 2, 'end_time': 1479464653, 'start_time': 1479464653}
    }
    return ApiMethod.testMethod(geoUrl, type, data, cookie)
