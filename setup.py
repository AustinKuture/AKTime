#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Kuture
# Mail: kuture@163.com
# Blog: http://www.kuture.com.cn
# Created Time:  2020-7-8 12:00:00
#############################################


from setuptools import setup, find_packages

setup(
    name = "aktime",
    version = "0.1.0",
    keywords = ("pip", "aktime","TimeCalcu", "timetool", "kuture"),
    description = "Function time calculator",
    long_description = "Function time calculator",
    license = "MIT Licence",

    url = "https://github.com/fengmm521/pipProject",
    author = "Kuture",
    author_email = "kuture@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['prettytable']
)