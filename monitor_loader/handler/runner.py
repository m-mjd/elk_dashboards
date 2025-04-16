import time
import logging
from handler.webloader import create_driver, login_with_retry, load_dashboard, tab_name

logging.basicConfig(filename='Logs/app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def run(url, username, password, tab_number, name, zoom):
    tab_name(name)
    driver = create_driver(str(zoom))
    driver.get(url)

    while True:
        try:
            login_with_retry(driver, username, password, tab_number)

            load_dashboard(driver, url)

        except Exception as e:
            logging.error(
                f"Error: {e}\nSleeping for 10 seconds (for potential recovery)")
            time.sleep(20)
