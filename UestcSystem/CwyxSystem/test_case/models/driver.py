# coding=utf-8
from selenium.webdriver import Remote
from  selenium import webdriver


def browser():
    driver = webdriver.Firefox()
    host = '' // 运行主机IP地址和端口号
    dc = {'browserName': 'Firefox'}
    driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
