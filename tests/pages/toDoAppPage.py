from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class to_Do_App_Page():
    ## START Functions used for general purpose
    def __init__(self,app):
        '''Contructor'''
        self.driver = app.driver;

    def end_session(self):
        '''Stop Driver'''
        self.driver.quit()

    def reload_page(self):
        '''Reload Page'''
        self.driver.refresh()

    def find_by_css(self,css):
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_css_selector(css))
            except (NoSuchElementException, TimeoutException):

                return False
            return i

    def find_by_xpath(self,xpath):
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(xpath))
            except (NoSuchElementException, TimeoutException):

                return False
            return i

    def find_by_xpath_contains(self,xpathc):
            xpath = "//*[contains(text(),'"+xpathc+"')]"
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(xpath))
            except (NoSuchElementException, TimeoutException):

                return False
            return i

    def find_by_id(self,id):
            try:
                i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id(id))
            except (NoSuchElementException, TimeoutException):

                return False
            return i
    #END  Functions used for general purpose


    ## START get elemets
    def look_for_title(self):
        self.ITEM_TITLE = self.driver.title
        return self.ITEM_TITLE

    def look_for_page_title(self):
        self.ITEM_TITLE_PAGE = self.find_by_xpath("//h1[normalize-space()='Todo List']")
        return self.ITEM_TITLE_PAGE

    def look_for_text_box(self):
        #self.ITEM_TEXT_BOX = self.find_by_id('new_record')
        self.ITEM_TEXT_BOX = self.find_by_xpath("//input[@id='new_record']")
        return self.ITEM_TEXT_BOX

    def look_for_button_add(self):
        self.ITEM_BUTTON_ADD = self.find_by_xpath("//span[@class='MuiButton-label']")
        return self.ITEM_BUTTON_ADD

    def look_for_added_item(self,msj):
        try:
            i = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath("//body//div[@id='root']//ul//ul[1]//li[1]//div[1]//span[1]"))
        except (NoSuchElementException, TimeoutException):

            return False
        if msj in i.text:
            return i
        return False
        # self.ITEM_ADDED = self.find_by_xpath_contains()
        # return self.ITEM_ADDED
    def look_for_remove_button(self):
        self.ITEM_BUTTON_REMOVE = self.find_by_xpath("//span[contains(text(),'❌')]")
        return self.ITEM_BUTTON_REMOVE
    # END get elements


    ## START Functions used for specific steps

    def go_to_web_site(self):
        '''Go to ToDo app WebApp'''
        self.driver.maximize_window();
        self.driver.get("https://todo-app-cp-8c579.web.app/")
        return self.look_for_title()

    def send_msj(self,msj):
        if not self.look_for_text_box():return False
        self.find_by_xpath("//input[@id='new_record']").send_keys(str(msj))
        return True

    def click_add_button(self):
        if not self.look_for_button_add(): return False
        self.find_by_xpath("//span[@class='MuiButton-label']").click()
        #self.ITEM_BUTTON_ADD.click()
        return True

    def click_remove(self):
        if not self.look_for_remove_button(): return False
        self.ITEM_BUTTON_REMOVE.click()
        return True
    # END Functions used for specific steps