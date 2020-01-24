# coding=utf-8

import unittest
from time import time, sleep

import apiritif

import os
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as econd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bzt.resources.selenium_extras import FrameManager, WindowManager, LocatorsManager


class TestLocSc(unittest.TestCase):

    def setUp(self):
        self.driver = None
        options = webdriver.FirefoxOptions()
        profile = webdriver.FirefoxProfile()
        profile.set_preference('webdriver.log.file', '<somewhere>webdriver.log')
        self.driver = webdriver.Firefox(profile, firefox_options=options)
        self.driver.implicitly_wait(3.5)
        self.wnd_mng = WindowManager(self.driver)
        self.frm_mng = FrameManager(self.driver)
        self.loc_mng = LocatorsManager(self.driver)
        self.vars = {
            'name': 'Name',
            'red_pill': 'take_it',
        }
        apiritif.put_into_thread_store(func_mode=False, driver=self.driver)

    def _1_(self):
        with apiritif.smart_transaction('/'):
            self.driver.get('http://blazedemo.com/')

            element = self.loc_mng.get_element([{
                'xpath': "//input[@type='submit']",
            }])

            WebDriverWait(self.driver, 3.5).until(econd.visibility_of(element),
                                                  'Element \'xpath\':"//input[@type=\'submit\']" failed to appear within 3.5s')
            self.assertEqual(self.driver.title, 'BlazeDemo')

            element = self.loc_mng.get_element([{
                'xpath': '/html/body/div[2]/div/p[2]/a',
            }])
            ActionChains(self.driver).move_to_element(element).perform()

            element = self.loc_mng.get_element([{
                'xpath': '/html/body/div[3]/h2',
            }])
            ActionChains(self.driver).double_click(element).perform()

            element = self.loc_mng.get_element([{
                'xpath': '/html/body/div[3]/form/select[1]',
            }])
            ActionChains(self.driver).click_and_hold(element).perform()

            element = self.loc_mng.get_element([{
                'xpath': '/html/body/div[3]/form/select[1]/option[6]',
            }])
            ActionChains(self.driver).release(element).perform()

            element = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            Select(element).select_by_visible_text('London')

            element = self.loc_mng.get_element([{
                'css': 'body input.btn.btn-primary',
            }])
            element.send_keys(Keys.ENTER)

            element = self.loc_mng.get_element([{
                'id': 'address',
            }])
            self.assertEqual(element.get_attribute('value').strip(), '123 Beautiful st.'.strip())

            element = self.loc_mng.get_element([{
                'xpath': '/html/body/div[2]/form/div[1]/label',
            }])
            self.assertEqual(element.get_attribute('innerText').strip(), self.vars['name'].strip())

            element = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            WebDriverWait(self.driver, 3.5).until(econd.visibility_of(element),
                                                  "Element 'name':'toPort' failed to appear within 3.5s")

            element = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            element.send_keys('B')

            element = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            element.clear()
            element.send_keys('B')

            element = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            element.send_keys(Keys.ENTER)

            element = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            element.clear()
            element.send_keys(Keys.ENTER)

            element = self.loc_mng.get_element([{
                'xpath': '//div[3]/form/select[1]//option[3]',
            }])
            element.click()

            element = self.loc_mng.get_element([{
                'xpath': '//div[3]/form/select[2]//option[6]',
            }])
            element.click()
            self.wnd_mng.switch('0')
            self.driver.execute_script("window.open('some.url');")
            self.wnd_mng.switch('win_ser_local')
            self.wnd_mng.switch('win_ser_1')
            self.wnd_mng.switch('that_window')
            self.wnd_mng.close('1')
            self.wnd_mng.close('win_ser_local')
            self.wnd_mng.close('win_ser_1')
            self.wnd_mng.close('that_window')

            element = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            element.submit()
            self.driver.execute_script("alert('This is Sparta');")

            for i in range(10):
                if ((i % 2) == 0):
                    print(i)

            source = self.loc_mng.get_element([{
                'id': 'address',
            }])

            target = self.loc_mng.get_element([{
                'name': 'toPort',
            }])
            ActionChains(self.driver).drag_and_drop(source, target).perform()
            self.frm_mng.switch(self.loc_mng.get_element([{
                'name': 'my_frame',
            }]))
            self.frm_mng.switch('index=1')
            self.frm_mng.switch('relative=parent')

            edit_content = self.loc_mng.get_element([{
                'id': 'editor',
            }])

            if edit_content.get_attribute('contenteditable'):
                self.driver.execute_script(("arguments[0].innerHTML = '%s';" % 'lo-la-lu'), edit_content)
            else:
                raise NoSuchElementException(('The element (%s: %r) is not a contenteditable element' % edit_content))
            sleep(3.5)
            self.driver.delete_all_cookies()

            element = self.loc_mng.get_element([{
                'linktext': 'destination of the week! The Beach!',
            }])
            element.click()

            self.vars['Title'] = self.driver.title

            element = self.loc_mng.get_element([{
                'xpath': "//*[@id='basics']/h2",
            }])

            self.vars['Basic'] = element.get_attribute('innerText')

            element = self.loc_mng.get_element([{
                'xpath': "//*[@id='basics']/h1",
            }])

            self.vars['World'] = element.get_attribute('value')

            self.vars['Final'] = '{} {} by {}'.format(self.vars['Title'], self.vars['Basic'], self.vars['By'])
            self.driver.get('http:\\blazemeter.com')
            print(self.vars['red_pill'])
            self.driver.save_screenshot('screen.png')

            filename = os.path.join(os.getenv('TAURUS_ARTIFACTS_DIR'), ('screenshot-%d.png' % (time() * 1000)))
            self.driver.save_screenshot(filename)
            body = self.driver.page_source
            re_pattern = re.compile('contained_text')
            self.assertEqual(0, len(re.findall(re_pattern, body)), "Assertion: 'contained_text' found in BODY")

    def _2_empty(self):
        with apiritif.smart_transaction('empty'):
            pass

    def test_locsc(self):
        self._1_()
        self._2_empty()

    def tearDown(self):
        if self.driver:
            self.driver.quit()
