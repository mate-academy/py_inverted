import pytest

import inverted


@pytest.fixture
def index():
    index = inverted.Index()
    index.index(1, "aa bb cc aa cc")
    index.index(2, "bb cc dd ee")
    index.index(3, "aa bb dd aa bb")
    return index


def test_all(index):
    assert set(index.all_words("aa", "bb")) == {1, 3}


def test_any(index):
    assert set(index.any_words("aa", "cc")) == {1, 2, 3}


def test_only_one(index):
    assert set(index.all_words("bb", "ee")) == {2}