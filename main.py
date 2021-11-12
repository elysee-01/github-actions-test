import re

REG = re.compile(
    """(?P<source>src|href)=("|')(?P<path>(css|js|\.\./|video|image|font-awesome|build|asset)(s)?[\S]+)("|')"""
)


def replace_static(content):
    assert isinstance(content, str), "str instance is required"
    return REG.sub('''\g<source>="{% static '\g<path>' %}"''', content)
