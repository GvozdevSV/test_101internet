import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://piter-online.net')
driver.maximize_window()
adress = driver.find_element(By.CSS_SELECTOR, 'input[class="app141 app148 app147 app143 app160 app142"]')
adress.send_keys('Тестовая линия')
time.sleep(1)
adress.send_keys(Keys.RETURN)
home = driver.find_element(By.CSS_SELECTOR, 'input[class="app141 app148 app147 app143 app160"]')
home.send_keys('1')
time.sleep(1)
home.send_keys(Keys.RETURN)
choose_appartment = driver.find_element(By.CSS_SELECTOR, '.app183 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1)')
choose_appartment.click()
search_tarif_button = driver.find_element(By.CSS_SELECTOR, 'div[class="app205 app237 app233 app228 app217 app234"]')
search_tarif_button.click()
time.sleep(1)
close_pop_up_button = driver.find_element(By.CSS_SELECTOR, 'div[datatest="close_popup1_from_quiz_input_tel"]')
close_pop_up_button.click()
count = 5
while count != 0:
    connect_tariff_button = driver.find_elements(By.CSS_SELECTOR, 'div[datatest="providers_form_inspect_connect_tariff_button"]')
    random_element_connect_tariff_button = connect_tariff_button[random.randint(0, len(connect_tariff_button) - 1)]
    random_element_connect_tariff_button.click()
    time.sleep(1)
    order_input_name = driver.find_element(By.CSS_SELECTOR, 'input[datatest="providers_provider_order_input_name"]')
    order_input_name.send_keys('Автотест')
    order_input_tel = driver.find_element(By.CSS_SELECTOR, 'input[datatest="providers_provider_order_input_tel"]')
    order_input_tel.send_keys('1111111111')
    input_connect_button = driver.find_element(By.CSS_SELECTOR, 'div[data-test="order_form_input_connect_button"]')
    time.sleep(2)
    input_connect_button.click()
    time.sleep(1)
    driver.get('https://piter-online.net/leningradskaya-oblast/rates?house_id=4270758')
    count -=1





