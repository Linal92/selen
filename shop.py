# задание 4

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
# shop = driver.find_element_by_css_selector('#menu-item-40 > a').click()
#
# book = driver.find_element_by_css_selector('#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img').click()
#
# title = driver.find_element_by_css_selector('#product-181 > div.summary.entry-summary > h1')
# title_text = title.text
# assert title_text == 'HTML5 Forms'
#
# driver.quit()

# задание 5

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
# shop = driver.find_element_by_css_selector('#menu-item-40 > a').click()
#
# filt = driver.find_element_by_css_selector('#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a').click()
#
# cart = driver.find_elements_by_class_name('price')
# if len(cart) == 3:
#     print('В категории HTML 3 товара')
# else:
#     print('ERROR')
#
# driver.quit()

# задание 6

# import time
#
# import driver as driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# shop = driver.find_element_by_css_selector('#menu-item-40 > a').click()
#
# sel = driver.find_element_by_class_name('orderby')
# sel1 = sel.get_attribute('value')
# if sel1 == 'menu_order':
#     print('OK')
# else:
#     print('not ok')
#
# select = Select(sel)
# select.select_by_value('price-desc')
#
# sel2 = driver.find_element_by_class_name('orderby')
# sel3 = sel2.get_attribute('value')
# if sel3 == 'price-desc':
#     print('OK')
# else:
#     print('not ok')
#
# driver.quit()

#задание 7

# import time
#
# import driver as driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# shop = driver.find_element_by_css_selector('#menu-item-40 > a').click()
#
# andr = driver.find_element_by_css_selector('#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3').click()
#
# old = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span')
# old_text = old.text
# new = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span')
# new_text = new.text
#
# assert old_text == '₹600.00'
# assert new_text == '₹450.00'
#
# book_cover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-169 > div.images > a > img')))
# book_cover.click()
#
# book_cover_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a')))
# book_cover_close.click()
#
# driver.quit()

# задание 8

# import time
#
# import driver as driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
#
# driver.get("http://practice.automationtesting.in/")
#
# shop = driver.find_element_by_css_selector('#menu-item-40 > a').click()
#
# add_bas = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
#
# time.sleep(3)
#
# item = driver.find_element_by_css_selector('#wpmenucartli > a > span.cartcontents')
# item_text = item.text
# price = driver.find_element_by_css_selector('#wpmenucartli > a > span.amount')
# price_text = price.text
#
# assert item_text == '1 Item'
# assert price_text == '₹180.00'
#
# bas = driver.find_element_by_css_selector('#wpmenucartli > a').click()
#
# sub = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span'), "₹180.00"))
# tot = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span'), "₹189.00"))
#
# driver.quit()

#задание 9

# import time
#
# import driver as driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
#
# driver.get("http://practice.automationtesting.in/")
#
# shop = driver.find_element_by_css_selector('#menu-item-40 > a').click()
#
# add_bas = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
#
# time.sleep(3)
#
# driver.execute_script("window.scrollTo(0, 300)")
#
# add_bas1 = driver.find_element_by_css_selector('#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
#
# bas = driver.find_element_by_css_selector('#wpmenucartli > a').click()
#
# time.sleep(3)
#
# dil = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a').click()
#
# time.sleep(3)
#
# undo = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div.woocommerce-message > a').click()
#
# ad = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
# ad.clear()
# ad.send_keys('3')
#
# up = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button').click()
#
# ad1 = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
# ad1_text = ad1.get_attribute('value')
# assert ad1_text == '3'
#
# time.sleep(3)
#
# ap = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button').click()
#
# coup = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > ul > li')
# coup_text = coup.text
# assert coup_text == 'Please enter a coupon code.'
#
# driver.quit()

#задание 10

import time

import driver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_css_selector('#menu-item-40 > a').click()

driver.execute_script("window.scrollTo(0, 300)")

add_bas = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()

time.sleep(2)

bas = driver.find_element_by_css_selector('#wpmenucartli > a').click()

pro = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > div > a')))
pro.click()

first = wait.until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))
first.send_keys('A1')

last = driver.find_element_by_id('billing_last_name').send_keys('A2')

mail = driver.find_element_by_id('billing_email').send_keys('A3@mail.ru')

phone = driver.find_element_by_id('billing_phone').send_keys('1251252135')

country = driver.find_element_by_css_selector('#s2id_billing_country > a').click()

find = driver.find_element_by_id('s2id_autogen1_search').send_keys('russia')

rus = driver.find_element_by_class_name('select2-result-label').click()

ad = driver.find_element_by_id('billing_address_1').send_keys('A4')

town = driver.find_element_by_id('billing_city').send_keys('A5')

state = driver.find_element_by_id('billing_state').send_keys('A6')

zip = driver.find_element_by_id('billing_postcode').send_keys('A7')

driver.execute_script("window.scrollTo(0, 600)")

chek = driver.find_element_by_id('payment_method_cheque').click()

order = driver.find_element_by_id('place_order').click()

text1 = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
text2 = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td'), "Check Payments"))

driver.quit()