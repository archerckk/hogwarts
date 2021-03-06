'''
课后作业1
1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例

课后作业2
控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
减法依赖加法， 除法依赖乘法

课后作业3
注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。
'''
import pytest


class Calculator:

    def add(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'
        return a + b

    def mul(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'
        return a * b

    def sub(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'

        return a - b

    def div(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'
        elif b == 0:
            return '被除数不能为0'

        return a / b
