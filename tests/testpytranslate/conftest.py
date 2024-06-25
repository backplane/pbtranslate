"""fixtures for the tests"""

import pytest

from pbtranslate.config import Config


@pytest.fixture
def conf():
    """fixture representing an empty pbtranslate config"""
    return Config()
