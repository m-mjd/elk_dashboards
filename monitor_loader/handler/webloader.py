import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from handler.monitoring import ensure_on_display as monitor

logging.basicConfig(filename='Logs/app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

panel_name = None


def load_title(driver, panel_name):
    driver.execute_script(f"document.title = '{panel_name}';")





def tab_name(name):
    global panel_name
    panel_name = name
    return panel_name


def create_driver(zoom):
    firefox_options = Options()
    firefox_options.set_preference(
        "layout.css.devPixelsPerPx", str(zoom))
    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(10)
    logging.info("Driver created.")
    return driver



def login_with_retry(driver, username, password, tab_number, max_retries=10, wait_time=30):

    retries = 0
    while retries < max_retries:
        try:
            driver.find_element(By.NAME, "username").click()
            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").click()
            driver.find_element(By.NAME, "password").send_keys(password)
            time.sleep(1.5)

            driver.find_element(
                By.CLASS_NAME, "css-cf8eum-euiButtonDisplayContent").click()
            time.sleep(2)

            tab_handle(driver, tab_number)

            logging.info("Login successful.")
            return
        except NoSuchElementException:
            retries += 1

            logging.warning(f"Didn't find elements... Sleeping {
                            wait_time} sec (Retry {retries}/{max_retries})")
            tab_handle(driver, tab_number)
            time.sleep(wait_time)

    logging.error(f"Failed to find elements after {max_retries} retries.")
    return


def tab_handle(driver, tab_number):
    load_title(driver, panel_name)
    while not monitor(driver.title, tab_number):
        driver.set_window_size(200, 100)
    driver.fullscreen_window()
    logging.info("Tab handle executed.")


def load_dashboard(driver, url):
    driver.get(url)
    driver.fullscreen_window()
    load_title(driver, panel_name)
    logging.info(f"Dashboard loaded from {url}.")
