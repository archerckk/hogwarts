def function_no_args():
    '这是一个没有传参的函数，函数只打印一句话'
    print('这是一个没有传参的函数')


def function_have_args(x):
    '这是一个有传参的函数，函数打印【hello 加传入的参数】'
    print(f'hello {x}')


def function_no_return():
    """
    这是一个没有写返回值的函数
    :return:默认返回的值为None
    """
    print('这是一个没有写返回值的函数')


def function_have_return():
    """
    这是一个有返回值的函数
    :return:返回内容为：【这是一个有返回值的函数"】的字符串
    """
    return '这是一个有返回值的函数'
