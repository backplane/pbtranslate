"""interactions with the macos clipboard / pasteboard"""

import subprocess  # nosec


def pb_getstr() -> str:
    """return the contents of the pasteboard"""
    result = subprocess.run(  # nosec
        ("/usr/bin/pbpaste", "-Prefer", "txt"),
        capture_output=True,
        encoding="utf-8",
        shell=False,
        check=True,
    )
    return result.stdout


def pb_setstr(value: str):
    """set the contents of the pasteboard"""
    subprocess.run(  # nosec
        ["/usr/bin/pbcopy"],
        capture_output=False,
        encoding="utf-8",
        check=True,
        shell=False,
        input=value,
    )
