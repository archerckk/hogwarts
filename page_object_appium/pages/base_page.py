import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [
        # (By.ID, 'image_cancel')
    ]
    _error_count = 0
    _max_error_count = 10
    _parames = {}
    _path = ''

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

        if self._path == '':
            self._step = [{}]
        else:
            self._step = self._get_action_datas(self._path)

    def _find(self, by, locator=None):
        try:
            self._error_count = 0
            print(by, locator)
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                             locator)
            return element
        except Exception as e:
            if self._error_count >= self._max_error_count:
                raise e
            for black in self._black_list:
                black_find_result_list = self._driver.find_elements(black)
                self._error_count += 1
                if len(black_find_result_list) > 0:
                    black_find_result_list[0].click()
                    return self._find(by, locator)
            raise e

    def _send(self, value, by, locator=None):
        try:
            self._find(by, locator).send_keys(value)
        except Exception as e:
            if self._error_count >= self._max_error_count:
                raise e
            for black in self._black_list:
                black_find_result_list = self._driver.find_elements(black)
                self._error_count += 1
                if len(black_find_result_list) > 0:
                    black_find_result_list[0].click()
                    return self._find(by, locator)
            raise e

    def _get_action_datas(self, path=None):
        with open(path, encoding='utf-8')as f:
            steps: list[dict] = yaml.safe_load(f)
            return steps

    def _steps(self, steps: dict):
        for step in steps:
            if 'by' in step.keys():
                element = self._find(step['by'], step['locator'])

                if 'click' == step['action']:
                    element.click()
                elif 'send' == step['action']:
                    content: str = step['value']
                    print(content)
                    for param in self._parames:
                        print(self._parames)
                        print(param)
                        content = content.replace('{%s}' % param, self._parames[param])
                    element.send_keys(content)
