from selene import browser
import pytest

@pytest.fixture
def open():
    browser.open('https://google.com')
@pytest.fixture
def wh():
    browser.config.window_width = 800
    browser.config.window_height = 600

    yield
    print('finish')