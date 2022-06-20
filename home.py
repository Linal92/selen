#задание 1

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
# driver.execute_script("window.scrollTo(0, 600)")
#
# read_more = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.button.product_type_simple.ajax_add_to_cart').click()
#
# reviews = driver.find_element_by_css_selector('#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a').click()
#
# star = driver.find_element_by_css_selector('#commentform > p.comment-form-rating > p > span > a.star-5').click()
#
# coment = driver.find_element_by_id('comment').send_keys('Nice book!')
#
# name = driver.find_element_by_id('author').send_keys('A1')
#
# mail = driver.find_element_by_id('email').send_keys('mail@mail.ru')
#
# sub = driver.find_element_by_id('submit').click()
#
# time.sleep(3)
#
# driver.quit()