import pytest
from selenium import webdriver
from helpers.urls import URLs


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()
