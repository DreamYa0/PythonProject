# -*- coding: utf-8 -*-
import os
from TestPython.interfaceTest.common import configHttp
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from TestPython.interfaceTest.common import Mylog

localConfigHttp = configHttp.ConfigHttp()
log = Mylog.MyLog.get_log()
logger = log.get_logger()
proDir = os.path.split(os.path.realpath(__file__))[0]


# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, "testFile", xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


# 从xml文件中读取sql语句
database = {}


def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table


def get_xml_dict(database_name, table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict


def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql
