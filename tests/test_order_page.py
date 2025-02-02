import pytest
import allure

from page_objects.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import *


class TestOrderPageOrder:

    @allure.title('Проверка флоу позитивного сценария оформления заказа')
    @pytest.mark.parametrize('button, test_data', [(MainPageLocators.order_button_in_header, TestData.test_data_user1),
                                                   (MainPageLocators.order_button_in_main, TestData.test_data_user2)])
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_displaying_of_button_check_status_of_order()
