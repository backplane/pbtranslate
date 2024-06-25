"""test core functions"""

from typing import Final, Sequence, TypedDict

import pytest

from pbtranslate.ai import translate

Trial = TypedDict(
    "Trial",
    {
        "english": str,
        "dutch": str,
        "french": str,
        "german": str,
        "spanish": str,
    },
)


TRANSLATION_TRIALS: Final[Sequence[Trial]] = [
    {
        "english": "Hello, how are you?",
        "dutch": "hallo, hoe gaat het met jouw",
        "french": "Bonjour, comment ça va?",
        "german": "Hallo, wie geht es dir?",
        "spanish": "Hola, ¿cómo estás?",
    },
    {
        "english": "Thank you",
        "dutch": "dank je",
        "french": "Merci",
        "german": "Danke",
        "spanish": "Gracias",
    },
    {
        "english": "I love you",
        "dutch": "ik hou van jou",
        "french": "Je t'aime",
        "german": "Ich liebe dich",
        "spanish": "Te quiero",
    },
]


@pytest.mark.parametrize("trial", TRANSLATION_TRIALS)
def test_translate(conf, trial):
    """test the translate_string function by giving it trials"""
    en_phrase = trial.pop("english")
    for _, foreign_phrase in trial.items():
        result = translate(conf, foreign_phrase)
        assert result.lower().strip(".") == en_phrase.lower()
