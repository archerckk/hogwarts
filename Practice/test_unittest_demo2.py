import unittest


class Test_demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('执行类方法setup')

    def setUp(self) -> None:
        print('执行普通setup')

    def tearDown(self) -> None:
        print('执行普通teardown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('执行类方法teardown')

    def test_demo1(self):
        print('测试用例1')
        self.assertEqual(1, 2, '两个值不相等')

    def test_demo2(self):
        print('测试用例2')

        self.assertEqual(1, 1, '两个值不相等')


class Test_demo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('执行类方法setup')

    def setUp(self) -> None:
        print('执行普通setup')

    def tearDown(self) -> None:
        print('执行普通teardown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('执行类方法teardown')

    def test_demo1(self):
        print('测试用例1')
        self.assertEqual(1, 2, '两个值不相等')

    def test_demo2(self):
        print('测试用例2')

        self.assertEqual(1, 1, '两个值不相等')


if __name__ == '__main__':
    unittest.main()  # 方式1

    # suites = unittest.TestSuite()
    # suites.addTest(Test_demo("test_demo1"))
    # unittest.TextTestRunner().run(suites)

    # suite2=unittest.TestLoader().loadTestsFromTestCase(Test_demo)
    # suite1=unittest.TestLoader().loadTestsFromTestCase(Test_demo2)
    # suites=unittest.TestSuite([suite1])
    # unittest.TextTestRunner().run(suites)
