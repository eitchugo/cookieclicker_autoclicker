# -*- coding: utf-8 -*-
"""
    cookieclicker_autoclicker.cli
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Main entry point for CLI calls to the autoclicker
"""
import sys
import time
import pyautogui
from signal import signal, SIGINT
from cookieclicker_autoclicker import __version__
from cookieclicker_autoclicker.logger import logger


def signal_handler(signum: int, frame: int) -> None:
    """
    Exits gracefully

    Params:
        signum (int): signal number that was captured
        frame (int): TODO
    """
    print("Exiting.")
    sys.exit(0)


def main() -> None:
    """
    Main CLI handler
    """
    logger.info(
        f"Cookieclicker auto-clicker mega-clicker ultra-clicker {__version__} init "
        "in 3 seconds")

    time.sleep(3)

    clicks = 500
    interval = 0.01
    seconds = clicks * interval

    ignore_cookie = None
    golden_cookies_images = [
        "data/cookieclicker_goldencookie1.png",
        "data/cookieclicker_goldencookie2.png",
        "data/cookieclicker_goldencookie3.png",
        "data/cookieclicker_goldencookie4.png",
        "data/cookieclicker_goldencookie5.png",
        "data/cookieclicker_goldencookie6.png"
    ]

    # exits gracefully if we hit CTRL+C or receive a SIGINT
    signal(SIGINT, signal_handler)

    logger.info(f"Clicking {clicks} times in {seconds} seconds interval...")
    while True:
        logger.debug("Beginning clicking loop.")
        try:
            pyautogui.click(
                clicks=clicks,
                interval=interval,
                button='left'
            )

        except KeyboardInterrupt:
            logger.info("CTRL+C pressed.")
            signal_handler(1, 1)

        except pyautogui.FailSafeException:
            logger.info("Screen corner failsafe activated, exiting.")
            signal_handler(1, 1)

        logger.debug("Clicking loop done for now.")

        if not ignore_cookie:
            for image in golden_cookies_images:
                try:
                    golden_cookie = pyautogui.locateCenterOnScreen(
                        image,
                        confidence=0.8)

                    logger.info("Golden cookie found on screen! Clicking it")
                    m_current_pos = pyautogui.position()
                    time.sleep(1)
                    pyautogui.click(
                        x=golden_cookie[0],
                        y=golden_cookie[1],
                        clicks=1,
                        button='left')

                    logger.info("Returning mouse to original position")
                    pyautogui.moveTo(m_current_pos[0], m_current_pos[1])

                except OSError:
                    logger.error(
                        "Error while reading file {image}, check path and permissions. Ignoring golden cookie for now.")
                    ignore_cookie = True

                except pyautogui.ImageNotFoundException:
                    logger.debug(
                        "Golden cookie not found on screen. "
                        "Returning to the loop.")
                    pass


if __name__ == "__main__":
    main()
