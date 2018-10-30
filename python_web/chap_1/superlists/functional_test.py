#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/10/30 9:11
@filename:functional_test
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
