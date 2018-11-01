#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/1 10:54
@filename:function_test
"""
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title