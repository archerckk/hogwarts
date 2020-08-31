from time import sleep

from appium import webdriver
import yaml
from selenium.webdriver.common.by import By


class TestDemo:

    def setup(self):
        with open('phone.yml')as f:
            desired_caps = yaml.safe_load(f)['mumu_xueqiu']
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search_price(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name"][@text="阿里巴巴"]').click()
        current_price = self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/current_price']").text

        assert float(current_price) > 200

    def test_search_attribute(self):
        home_search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        home_search_enable = home_search_ele.is_enabled()
        home_search_location = home_search_ele.location
        home_search_ele_rect = home_search_ele.rect
        home_search_ele_width = home_search_ele_rect['width']
        home_search_ele_height = home_search_ele_rect['height']
        print(f'搜索框是否可用：{home_search_enable}')
        print('首页搜索框的name属性为：', home_search_ele.get_attribute('text'))
        print('首页搜索框的坐标位置为：', home_search_location)
        print(f'首页搜索框的宽为：{home_search_ele_width},高为：{home_search_ele_height}')
        home_search_ele.click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        alibaba_text = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name"]'
                                                         '[@text="阿里巴巴"]')
        alibaba_text_displayed = alibaba_text.is_displayed()
        print("阿里巴巴是否可见：", alibaba_text_displayed)
        if alibaba_text_displayed:
            print('搜索成功')
        else:
            print('索索失败')

    def test_xpath_father_son_element_locate(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name"][@text="阿里巴巴"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/title_container"]'
                                          '//android.widget.TextView[3]').click()
        no_user_text = self.driver.find_element_by_xpath("//*[@text='阿里巴巴官方账号']").text
        print("查找的账号：",no_user_text)
        assert no_user_text == '阿里巴巴官方账号'

    def test_uiautomator_use(self):
        # 通过父类的tab的id查找子类当中带有【行情】关键字的tab文案
        self.driver.find_element_by_android_uiautomator(
            'resourceId("android:id/tabs").childSelector(text("行情"))').click()
        # 定位到tab的icon的id，然后通过兄弟元素的文案【交易】定位到这个icon
        self.driver.find_element_by_android_uiautomator(
            'resourceId("com.xueqiu.android:id/tab_icon").fromParent(text("交易"))').click()
        sleep(3)

    def test_scorll_find_ele(self):
        title_hot = 'resourceId("com.xueqiu.android:id/title_text").text("推荐")'
        self.driver.find_element_by_android_uiautomator(title_hot).click()
        print('点击推荐')

        scorll_text = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("老李茶馆").instance(0));'
        self.driver.find_element_by_android_uiautomator(scorll_text).click()
        print('点击【老李茶馆】')
        assert '老李茶馆'in self.driver.page_source