import pygetwindow as gw
from screeninfo import get_monitors
import time
import logging

logging.basicConfig(filename='Logs/app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_displays_config():
    monitors = get_monitors()
    displays = [(monitor.x, monitor.y, monitor.width, monitor.height)
                for monitor in monitors]
    logging.info("Retrieved displays configuration.")
    return displays


def ensure_on_display(window_title, display_number):
    try:
        displays_config = get_displays_config()
        if display_number < 1 or display_number > len(displays_config):
            logging.error(f"Invalid display number: {
                          display_number}. Must be between 1 and {len(displays_config)}.")
            time.sleep(10)
            return

        windows = gw.getWindowsWithTitle(window_title)
        if not windows:
            logging.warning(f"Window with title '{window_title}' not found.")
            return False

        target_display = displays_config[display_number - 1]
        target_x, target_y, target_width, target_height = target_display
        window = windows[0]

        if not (target_x <= window.left < target_x + target_width):
            logging.info(f"Window '{window_title}' is not on Display {
                         display_number}. Moving...")
            window.moveTo(target_x, target_y)
            window.resizeTo(target_width, target_height)
            logging.info(f"Window '{window_title}' moved to Display {
                         display_number}.")
        else:
            logging.info(f"Window '{window_title}' is already on Display {
                         display_number}.")
            return True

    except Exception as e:
        logging.error(f"Error in checking or moving the window: {e}")

