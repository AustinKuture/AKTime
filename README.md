# AKTime

用于程序运行时统计各函数的运行时间，使用时只需要导入aktime中的TimeCalcu即可。给要统计运行时间的方法加上@time_cacu装饰器，程序结束时"调用read_resul()会以图表的形式展示各方法的运行时间。

**安装**

```python
pip install aktime
```



**示例**

```python
import time
from aktime import TimeCalcu


@TimeCalcu.time_cacu
def time1():

    for i in range(10):
        time.sleep(0.1)

@TimeCalcu.time_cacu
def time2():
    for i in range(25):
        time.sleep(0.1)

def main():
    time1()
    time2()


if __name__ == '__main__':
    main()
    TimeCalcu.read_result()
```

**效果**

```
+--------------------------------+----------------------+
|           Func name            |       Run time       |
+--------------------------------+----------------------+
|            time2()             |       2.57864        |
|            time1()             |       1.03123        |
| ------------------------------ | -------------------- |
|           Total Time           |       3.60987        |
+--------------------------------+----------------------+
```



