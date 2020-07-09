#coding=utf-8

"""
    @header TimeCalcu.py
    @abstract   
    
    @MyBlog: http://www.kuture.com.cn
    @author  Created by Kuture on 2020/7/6
    @version 1.0.0 2020/7/6 Creation()
    
    @Copyright © 2020年 Mr.Li All rights reserved
"""
import os
import datetime
import prettytable as pt
from io import StringIO


counts = 1
nums = 1
error_status = None
sio = StringIO()
split_logo = '<_kuture_>'
code_location = None


def time_calcu(func):
    def wrapper(*args, **kw):

        global counts, nums, sio, error_status, code_location
        start_time = datetime.datetime.now()
        # 捕获异常
        try:
            # 方法定位
            code_location = '{}: {}'.format(os.path.basename(func.__code__.co_filename),
                                            func.__code__.co_firstlineno+1)
            res = func(*args, **kw)

        except Exception as error:
            res = error
            error_status = error
        else:
            error_status = 'o^_^o'
        over_time = datetime.datetime.now()

        #
        if sio.closed:
            sio = StringIO()

        # 将记录的耗时信息写入内存中
        if func.__name__ != 'read_result':

            sio.writelines('{}{}{:.5f}{}{}{}{}\n'.format(func.__name__,
                                                     split_logo,
                                                     (over_time-start_time).total_seconds(),
                                                     split_logo,
                                                     error_status,
                                                     split_logo,
                                                     code_location))

            # 进度打印
            # result = str(math.log(counts, 2))
            # temp = result[result.rfind('.'):]
            # if len(temp) <= 2:
            #     pri_num = 1 if int(5 / nums) <= 0 else int(5 / nums)
            #     print('▇' * pri_num, end='')
            #     nums += 1
            #     # print(result)
            # counts += 1
        # else:
        #     print('{} {:.5f}\n'.format('Statistic Method Time:', (over_time-start_time).total_seconds()))
        return res
    return wrapper


# 读取统计结果
@time_calcu
def time_statistic(display=True):

    print('\n')
    # 记录各方法耗时
    statis = {}
    # 错误标识
    msg_error_count = 0
    # 从内存中读取记录信息并处理
    content = sio.getvalue().split('\n')
    for lines in content:

        if len(lines) <= 0: continue
        lines = lines.split(split_logo)
        if list(statis.keys()).count(lines[0]) == 0:
            statis[lines[0]] = [float(lines[1]), 1, lines[2], lines[3]]
            if lines[2] != 'o^_^o':
                msg_error_count += 1
        else:
            # 时间统计
            time_count = statis[lines[0]][0]
            time_count += float(lines[1])
            # 调用统计
            num_count = statis[lines[0]][1]
            num_count += 1
            # 错误统计
            if lines[2] != 'o^_^o':
                msg_error_count += 1
            statis[lines[0]] = [time_count, num_count, lines[2], lines[3]]

    # 表格打印
    tb = pt.PrettyTable()
    if msg_error_count == 0:
        tb.field_names = ["Func name", "Counts",  "Run time", ]
    else:
        tb.field_names = ["Func name", "Counts", "Run time", 'Error', 'Location']

    total_time = []
    total_count = []

    # 列表排序
    statis = sorted(statis.items(), key=lambda d: d[1][0], reverse=True)

    # 制作表格
    for key, value in statis:

        total_time.append(value[0])
        total_count.append(value[1])
        if msg_error_count == 0:
            tb.add_row(['{}()'.format(key),
                        value[1],
                        '{:.5f}'.format(value[0])])
            tb.add_row(['-' * 30, '-' * 10, '-' * 10])  # 分割符
        else:
            tb.add_row(['{}()'.format(key),
                        value[1],
                        '{:.5f}'.format(value[0]),
                        '' if value[2]=='o^_^o'else'{}...'.format(value[2][:20]),
                        ''if value[2]=='o^_^o'else value[3]])
            tb.add_row(['-'*30, '-'*10, '-'*10, '-'*25, '-'*30])  # 分割符
    # 汇总
    if msg_error_count == 0:
        tb.add_row(['Sum', sum(total_count), '{:.5f}'.format(sum(total_time))])
    else:
        tb.add_row(['Sum', sum(total_count), '{:.5f}'.format(sum(total_time)), '', ''])

    if display: print(tb)
    sio.close()

    return sum(total_time)




