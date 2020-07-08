#coding=utf-8

"""
    @header TimeCalcu.py
    @abstract   
    
    @MyBlog: http://www.kuture.com.cn
    @author  Created by Kuture on 2020/7/6
    @version 1.0.0 2020/7/6 Creation()
    
    @Copyright © 2020年 Mr.Li All rights reserved
"""
import math
import datetime
import prettytable as pt
from io import StringIO


counts = 1
nums = 1
sio = StringIO()


def time_cacu(func):
    def wrapper(*args, **kw):
        start_time = datetime.datetime.now()
        res = func(*args, **kw)
        over_time = datetime.datetime.now()
        global counts, nums, sio

        if sio.closed:
            sio = StringIO()

        # 将记录的耗时信息写入内存中
        if func.__name__ != 'read_result':
            sio.writelines('{} {:.5f}\n'.format(func.__name__, (over_time-start_time).total_seconds()))

            # 进度打印
            result = str(math.log(counts, 2))
            temp = result[result.rfind('.'):]
            if len(temp) <= 2:
                pri_num = 1 if int(5 / nums) <= 0 else int(5 / nums)
                print('▇' * pri_num, end='')
                nums += 1
            counts += 1
        # else:
        #     print('{} {:.5f}\n'.format('Statistic Method Time:', (over_time-start_time).total_seconds()))
        return res
    return wrapper


# 读取统计结果
@time_cacu
def read_result(display=True):

    print('\n')
    # 记录各方法耗时
    statis = {}
    # 从内存中读取记录信息并处理
    content = sio.getvalue().split('\n')
    for lines in content:

        if len(lines) <= 0: continue
        lines = lines.split(' ')
        if list(statis.keys()).count(lines[0]) == 0:
            statis[lines[0]] = float(lines[1])
        else:
            temp_count = statis[lines[0]]
            temp_count += float(lines[1])
            statis[lines[0]] = temp_count

    # 表格打印
    tb = pt.PrettyTable()
    tb.field_names = ["Func name", "Run time"]
    total_time = []

    # 列表排序
    statis = sorted(statis.items(), key=lambda d: d[1], reverse=True)

    for key, value in statis:
        total_time.append(value)
        tb.add_row(['{}()'.format(key), '{:.5f}'.format(value)])

    tb.add_row(['-'*30, '-'*20])
    tb.add_row(['Total Time', sum(total_time)])

    if display: print(tb)
    sio.close()

    return sum(total_time)


if __name__ == '__main__':
    read_result()