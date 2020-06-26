'''
1、补全计算器（加减乘除）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、conftest.py中创建fixture 完成setup和teardown
4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
'''


class Calculator:

    def add(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'
        return a + b

    def sub(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'

        return a - b

    def mul(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'
        return a * b

    def div(self, a, b):
        if type(a) not in [int, float]:
            return '参数传入有误'
        elif type(b) not in [int, float]:
            return '参数传入有误'
        elif b == 0:
            return '被除数不能为0'

        return a / b
