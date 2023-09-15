import pytest
from selene import browser
from selene import be, have


def test_searching(open, wh):

    browser.element('#APjFqb').should(be.blank).type('8udfsdufsd0fsdf').press_enter()
    browser.element('.card-section').should(have.text('Убедитесь, что все слова написаны без ошибок'))
