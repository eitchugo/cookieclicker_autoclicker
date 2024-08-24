# -*- coding: utf-8 -*-
"""
    cookieclicker_autoclicker.logger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Log handling
"""
import logging
import os

if not logging.getLogger().hasHandlers():
    logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] %(message)s'
    )
logging.getLogger().setLevel(os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger("cookieclicker_autoclicker")
