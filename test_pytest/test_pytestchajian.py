import pytest


@pytest.mark.parametrize("name",["哈利","赫敏"])
def test_mm(name):
    print(name)