"""interactions with the ollama server"""

from typing import Final

import ollama

from .config import Config

TRANSLATE_PROMPT: Final = (
    "Translate the following text to {target_language}. "
    "If the text is already in {target_language}, leave it unchanged and output it as-is. "
    "Provide only the translated text or the original text "
    "without any additional explanations, comments, or quoting."
    "\n\n"
    "Text: {input_text}\n"
)


# logger: Final = logging.getLogger(__name__)


class OllamaAPI:
    """LLM API"""

    def __init__(self, host) -> None:
        self.client = ollama.Client(host)

    def query(self, query: str, model: str) -> str:
        """query the server"""
        response = self.client.chat(
            model=model,
            messages=[{"role": "user", "content": query}],
        )
        return response["message"]["content"].strip()


def translate(config: Config, value: str) -> str:
    """translate the given string to english"""
    value = value.strip()
    llm = OllamaAPI(host=config.ollama_url)
    translated = llm.query(
        TRANSLATE_PROMPT.format(
            input_text=value,
            target_language=config.target_language,
        ),
        model=config.ollama_model,
    )
    return translated
