print('这是一个插班同学补交的python实战1作业')

a = '这是全局变量，整个模块都可以使用'


class Test_demo:

    def setup(self):
        b = '这是一个函数内定义的局部变量'
        self.c = '这是一个测试类里面都有效都类变量'

    def test_a(self):
        print(a)  # a是全局变量所以模块里面都有效
        # print(b) #b是函数内定义的只在函数内有效，其他函数无法使用
        print(self.c)  # 这是在属于Test_demo类变量，所以这类里面的方法都有效



def test():
    try:
        raise ValueError('这是一个值错误')
    except ValueError as e:
        print(e)
        return
    finally:
        print('done')

test()


var_a=[1,2,5,6,9]
def my_max(var_a):
    result=0
    for i in var_a:
        if i>result:
            result=i
        else:
            continue
    return result
if __name__ == '__main__':
    print(my_max(var_a))

