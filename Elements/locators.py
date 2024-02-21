from selenium.webdriver.common.by import By
class LOGIN_LOCATORS:
    USERNAME_INPUT = (By.ID, 'Email')
    PASSWORD_INPUT = (By.ID, 'Password')
    LOGIN_BUTTON = (By.XPATH, "//button[@class='button-1 login-button']")

class ADD_NEW_CUSTOMERS:
    CUSTOMER_MENU = (By.XPATH, "//a[@href='#']//p[contains(text(), 'Customers')]")
    CUSTOMER_MENU_LIST = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(), 'Customers')]")
    ADD_CUSTOMER_BUTTON = (By.XPATH, "//a[@class='btn btn-primary']")
    EMAIL_FIELD =(By.ID, "Email")
    PASSWORD_FIELD =(By.ID, "Password")
    FIRST_NAME_FIELD =(By.ID, "FirstName")
    LAST_NAME_FIELD = (By.ID, "LastName")
    GENDER_MALE_RADIO_BUTTON = (By.ID, "Gender_Male")
    GENDER_FEMALE_RADIO_BUTTON = (By.ID, "Gender_Female")
    DATE_OF_BIRTH = (By.ID, "DateOfBirth")
    COMPANY_NAME = (By.ID, "Company")
    IS_TAX_EXEMPT = (By.ID, "IsTaxExempt")
    CUSTOMER_ROLE = (By.ID, "SelectedCustomerRoleIds_label")
    ADMINISTRATORS = (By.XPATH,"//li[contains(text(),'Administrators')]")
    REGISTERED = "//li[contains(text(),'Registered')]"
    VENDORS = "//li[contains(text(),'Vendors')]"
    GUESTS = "//li[contains(text(),'Guests')]"
    FORUM_MODERATORS = "//li[contains(text(),'Forum Moderators')]"
    MANAGE_OF_VENDOR = (By.ID, "VendorId")
    ADMIN_COMMENT = "//textarea[@id='AdminComment']"
    SAVE_BUTTON = "//button[@name='save']"






