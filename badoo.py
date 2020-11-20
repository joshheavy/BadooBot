from selenium import webdriver
from secrets import username, password
from time import sleep 


class BadooBot():
    def __init__(self):
        self.browser = webdriver.Chrome()

    def login(self):
        self.browser.get('https://badoo.com/en/mobile')

        # find the signing button and click
        sg_btn = self.browser.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/div[2]/a')
        sg_btn.click()

        login_btn = self.browser.find_element_by_xpath('//*[starts-with(@id, "email")]')
        login_btn.send_keys('0717746413')

        pass_btn = self.browser.find_element_by_xpath('//*[starts-with(@id, "password")]')
        pass_btn.send_keys('konshens')

        signin_btn = self.browser.find_element_by_xpath('//*[@id="page"]/div[2]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button')
        signin_btn.click()

        later_btn = self.browser.find_element_by_xpath('//*[@id="simple-page"]/div[2]/section/div[3]/div/div[2]/div')
        later_btn.click()

    def like(self):
         like_btn = self.browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
         like_btn.click()


    def dislike(self):
       dslike_btn = self.browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
       dslike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    return 0

    def close_popup(self):
        popup = self.browser.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div')
        popup.click()


    def send_crush(self):
        crush = self.browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[3]/div[1]')
        crush.click()

    def crush_pop(self):
        accept_btn = self.browser.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[1]/section/div/div[2]/div')
        accept_btn.click()