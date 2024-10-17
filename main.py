from sys import argv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

if len(argv) <= 1:
    print('Usage: python main.py <folder_url>')
    exit(1)

FOLDER_URL = argv[1]

driver = webdriver.Chrome()
driver.get(FOLDER_URL)
driver.implicitly_wait(5)

try:
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        show_more = driver.find_element(By.CSS_SELECTOR, '[data-testid="show-more"]').click()
        sleep(2)
except NoSuchElementException:
    pass

medias = driver.find_elements(By.CSS_SELECTOR, '[data-testid="media-link"]')

for media in medias:
    href = media.get_attribute('href')
    title = media.find_element(By.CSS_SELECTOR, '[data-testid="media-title"]').text

    print(f'{href} | {title}')
