import pytest
from selene import browser
from selene import be, have


def test_one(open, wh):

    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene was inspired by Selenide from Java world'))
