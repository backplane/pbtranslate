#!/usr/bin/env python3
"""
utility for translating the clipboard to the user's language
"""

import sys

import baselog

from .config import Config, log_levels
from .core import translate_input


def main() -> int:
    """
    entrypoint for module execution, returns int for sys.exit
    """
    conf = Config(
        prog=__package__,
        prog_description="utility for language translation in the clipboard",
    )
    logger = baselog.BaseLog(
        __package__,
        log_dir=conf.log_dir,
        console_log_level=conf.log_level,
    )
    if log_levels.index(conf.log_level) >= log_levels.index("DEBUG"):
        conf.logcfg(logger)

    translate_input(conf)

    return 0


if __name__ == "__main__":
    sys.exit(main())
