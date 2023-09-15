from selene import browser
import pytest


@pytest.fixture
def open_browser():
    browser.open("https://github.com/IkonnikovQA/python_6_2")

@pytest.fixture(open_browser)
def click_back():
    browser.element("#actions-tab")