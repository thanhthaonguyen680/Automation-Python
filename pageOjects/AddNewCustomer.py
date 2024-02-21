from selenium.webdriver.common.by import By
from Elements.locators import ADD_NEW_CUSTOMERS


class AddNewCustomer:
    def __init__(self, driver):
        self.driver = driver

    def cLick_on_customer_menu(self):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.CUSTOMER_MENU).click()

    def cLick_on_customer_list(self):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.CUSTOMER_MENU_LIST).click()

    def cLick_on_add_new(self):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.ADD_CUSTOMER_BUTTON).click()

    def input_email(self, email):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.EMAIL_FIELD).send_keys(email)

    def input_password(self, password):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.PASSWORD_FIELD).send_keys(password)

    def input_first_name(self, firstname):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.FIRST_NAME_FIELD).send_keys(firstname)

    def input_last_name(self, lastname):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.LAST_NAME_FIELD).send_keys(lastname)

    def select_gender(self):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.GENDER_MALE_RADIO_BUTTON).click()

    def select_gender(self):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.GENDER_FEMALE_RADIO_BUTTON).click()

    def input_day_of_birth(self, dayofbirth):
        self.driver.find_element(*ADD_NEW_CUSTOMERS.DATE_OF_BIRTH).send_keys(dayofbirth)

