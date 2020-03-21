link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_test_button_is_present(driver):

    driver.get(link)
    driver.find_element_by_css_selector(".add-to-basket .btn").is_displayed()
