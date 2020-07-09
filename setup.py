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
    version = "0.1.2",
    keywords = ("pip", "aktime","TimeCalcu", "timetool", "kuture"),
    description = "Function time calculator",
    long_description = "用于程序运行时统计各函数的运行时间，使用时只需要导入aktime中的"
                       "TimeCalcu即可。给要统计运行时间的方法加上@time_cacu装饰器，程序结束时"
                       "调用read_resul()会以图表的形式展示各方法的运行时间。",
    license = "MIT Licence",

    url = "https://github.com/AustinKuture/AKTime.git",
    author = "Kuture",
    author_email = "kuture@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['prettytable']
)