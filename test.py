import pytest
from main import replace_static


def test_option_is_string_istance():
    attendu = """<img src="{% static 'image/photo.png' %}" />"""
    result = replace_static('<img src="image/photo.png" />')
    assert result == attendu


def test_option_is_not_string_istance():
    with pytest.raises(AssertionError):
        replace_static(['<img src="image/photo.png" />'])
