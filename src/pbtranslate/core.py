"""core logic for the app"""

import sys

from .ai import translate
from .config import Config
from .pasteboard import pb_getstr, pb_setstr


def translate_input(config: Config):
    """translate the contents of the clipboard to english"""
    input_string = sys.stdin.read() if config.stdin else pb_getstr()
    translated = translate(config, input_string)
    if config.stdout:
        sys.stdout.write(translated + "\n")
        return
    pb_setstr(translated)
