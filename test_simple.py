from selene import browser
import pytest


#
# @pytest.fixture
# def user_id():
#     return 123
#
# def test_first(user_id):
#     assert user_id == 123
#


def test_bb(open_browser, click_back):
    browser.element('.input-block')