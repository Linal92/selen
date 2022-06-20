#задание 2

# import time
#
# import driver as driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
#
# driver.get("http://practice.automationtesting.in/")
#
# ac = driver.find_element_by_css_selector('#menu-item-50 > a').click()
#
# mail = driver.find_element_by_css_selector('#reg_email').send_keys('123qwe123@mail.ru')
#
# pas = driver.find_element_by_id('reg_password').send_keys('q1!w2@e3#')
#
# reg = driver.find_element_by_css_selector('#customer_login > div.u-column2.col-2 > form > p.woocomerce-FormRow.form-row > input.woocommerce-Button.button').click()
#
# driver.quit()

# задание 3

# import time
#
# import driver as driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
#
# driver.get("http://practice.automationtesting.in/")
#
# ac = driver.find_element_by_css_selector('#menu-item-50 > a').click()
#
# user = driver.find_element_by_id('username').send_keys('123qwe123@mail.ru')
#
# pas = driver.find_element_by_id('password').send_keys('q1!w2@e3#')
#
# log = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button').click()
#
# out = driver.find_element_by_css_selector('#page-36 > div > div.woocommerce > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a')
# out_text = out.text
# assert out_text == 'Logout'
#
# driver.quit()