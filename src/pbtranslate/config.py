"""declarative configurations"""

from typing import Literal, Optional, Sequence, TypeAlias

from basecfg import BaseCfg, opt

LogLevel: TypeAlias = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
log_levels: Sequence[LogLevel] = ("CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG")


class Config(BaseCfg):
    """Declarative Config Class for pbtranslate"""

    log_level: LogLevel = opt(
        default="INFO",
        choices=log_levels,
        parser=str.upper,
        doc="how verbosely to log to the console",
    )
    log_dir: Optional[str] = opt(
        default=None,
        doc="directory in which to write log files",
    )
    ollama_url: str = opt(
        doc="URL for the Ollama server",
        default="https://ollama.local/",
    )
    ollama_model: str = opt(
        doc="name of the model to use on the ollama server",
        default="llama3",
    )
    stdin: bool = opt(
        default=False,
        doc="read input text from the standard input, instead of the clipboard",
    )
    stdout: bool = opt(
        default=False,
        doc="write output to the standard out, instead of the clipboard",
    )
    target_language: str = opt(
        default="English",
        doc="language which the input text should be translated into",
    )
