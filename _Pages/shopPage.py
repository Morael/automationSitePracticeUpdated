from selenium.webdriver.common.keys import Keys


class Shop:

    def __init__(self, driver):
        self.driver = driver

        self.home_link_text = "Home"
        self.add_to_basket_button_class = "single_add_to_cart_button"
        self.description_button_class = "description_tab"
        self.description_id = "tab-description"
        self.reviews_button_class = "li.reviews_tab"
        self.reviews_id = "reviews"
        self.number_in_basket = "cartcontents"
        self.number_in_stock = ".stock.in-stock "
        self.input_product_number_field = "quantity"
        self.basket_price = "amount"
        self.product_price = "price"
        self.basket_coupon_code = "coupon_code"
        self.basket_apply_coupon = "apply_coupon"
        self.basket_subtotal_selector = "#page-34 > div > div.woocommerce > div.cart-collaterals > div > table > tbody > tr.cart-subtotal > td > span"
        self.basket_discount_selector = "#page-34 > div > div.woocommerce > div.cart-collaterals > div > table > tbody > tr.order-total > td > strong > span"
        self.basket_tax_cost_selector = "#page-34 > div > div.woocommerce > div.cart-collaterals > div > table > tbody > tr.tax-rate.tax-rate-roaming-tax-1 > td > span"
        self.basket_total_cost_selector = "#page-34 > div > div.woocommerce > div.cart-collaterals > div > table > tbody > tr.order-total > td > strong > span"
        self.coupon_discount_value_selector = "#page-34 > div > div.woocommerce > div.cart-collaterals > div > table > tbody > tr.cart-discount.coupon-krishnasakinala > td > span"
        self.coupon_warning_text_class = "woocommerce-error"
        self.coupon_warning_text_displayed_selector = "#page-34 > div > div.woocommerce > ul"
        self.remove_coupon_class = "woocommerce-remove-coupon"
        self.remove_book_class = "remove"
        self.check_basket_input_quantity_select = "input.input-text.qty.text"
        self.button_update_class = "update_cart"
        self.product1_price_grid_selector = "td.product-price"
        self.product1_name_grid_selector = "td.product-name"
        self.product1_price_grid_class = "product-subtotal"

    def click_home(self):
        self.driver.find_element_by_link_text(self.home_link_text).click()

    def find_add_to_basket_button(self):
        self.driver.find_element_by_class_name(self.add_to_basket_button_class).is_displayed()

    def is_add_basket_button_active(self):
        self.driver.find_element_by_class_name(self.add_to_basket_button_class).is_enabled()

    def click_add_to_basket_button(self):
        self.driver.find_element_by_class_name(self.add_to_basket_button_class).click()

    def click_description(self):
        self.driver.find_element_by_class_name(self.description_button_class).click()

    def check_description(self):
        self.driver.find_element_by_id(self.description_id)

    def click_reviews(self):
        self.driver.find_element_by_css_selector(self.reviews_button_class).click()

    def check_reviews(self):
        self.driver.find_element_by_id(self.reviews_id)

    def basket_number_of_products(self):
        basket_number = self.driver.find_element_by_class_name(self.number_in_basket).text.split()
        return int(basket_number[0])

    def get_max_products_from_stock(self):
        max_products = self.driver.find_element_by_css_selector(self.number_in_stock).text.split()
        return int(max_products[0])

    def input_number_of_products(self, amount_of_product):
        self.driver.find_element_by_name(self.input_product_number_field).clear()
        self.driver.find_element_by_name(self.input_product_number_field).send_keys(amount_of_product)

    def prompt_warning_product_number(self):
        prompt = self.driver.find_element_by_name(self.input_product_number_field).get_attribute("validationMessage")
        return prompt

    def check_cost_in_basket(self):
        basket_cost = self.driver.find_element_by_class_name(self.basket_price).text.split("₹")
        return float(basket_cost[1].replace(",", ""))

    def check_price_of_product(self):
        product_price = self.driver.find_element_by_class_name(self.product_price).text.split("₹")
        return float(product_price[1])

    def click_on_basket_in_menu(self):
        self.driver.find_element_by_class_name(self.basket_price).is_displayed()
        self.driver.find_element_by_class_name(self.basket_price).click()

    def add_coupon_code(self, code):
        self.driver.find_element_by_id(self.basket_coupon_code).clear()
        self.driver.find_element_by_id(self.basket_coupon_code).send_keys(code)
        self.driver.find_element_by_name(self.basket_apply_coupon).click()

    def check_coupon_discount_value(self):
        discount = self.driver.find_element_by_css_selector(self.coupon_discount_value_selector).text.split("₹")
        return discount[1]

    def check_coupon_correctness_from_total(self):
        sub_total = self.driver.find_element_by_css_selector(self.basket_subtotal_selector).text.split("₹")
        tax_cost = self.driver.find_element_by_css_selector(self.basket_tax_cost_selector).text.split("₹")
        total = self.driver.find_element_by_css_selector(self.basket_total_cost_selector).text.split("₹")
        return float(sub_total[1]) + float(tax_cost[1]) - float(total[1])

    def coupon_warning_text(self):
        warning = self.driver.find_element_by_class_name(self.coupon_warning_text_class).text
        return warning

    def coupon_warning_text_displayed(self):
        self.driver.find_element_by_class_name(self.coupon_warning_text_class).is_displayed()

    def remove_coupon(self):
        self.driver.find_element_by_class_name(self.remove_coupon_class).click()

    def remove_book_from_basket(self):
        self.driver.find_element_by_class_name(self.remove_book_class).click()

    def check_remove_book_button(self):
        self.driver.find_element_by_class_name(self.remove_book_class).is_displayed()

    def check_basket_input_quantity(self):
        self.driver.find_element_by_css_selector(self.check_basket_input_quantity_select).is_displayed()

    def raise_basket_input_quantity(self, times):
        for x in range(0, times):
            self.driver.find_element_by_css_selector(self.check_basket_input_quantity_select).send_keys(Keys.ARROW_UP)

    def lower_basket_input_quantity(self, times):
        for y in range(0, times):
            self.driver.find_element_by_css_selector(self.check_basket_input_quantity_select).send_keys(Keys.ARROW_DOWN)

    def check_update_button_is_displayed(self):
        self.driver.find_element_by_name(self.button_update_class).is_displayed()

    def click_basket_update_cart_button(self):
        self.driver.find_element_by_name(self.button_update_class).click()

    def name_of_first_book_in_basket(self):
        book_title = self.driver.find_element_by_css_selector(self.product1_name_grid_selector).text
        return book_title

    def first_product_price_basket(self):
        single_price = self.driver.find_element_by_css_selector(self.product1_price_grid_selector).text.split("₹")
        return single_price[1]

    def check_total_basket_product_grid(self):
        total_1_product = self.driver.find_elements_by_class_name(self.product1_price_grid_class)[1].text.split("₹")
        return float(total_1_product[1])

    def count_multiple_product_price(self, amount):
        single_price = self.driver.find_element_by_css_selector(self.product1_price_grid_selector).text.split("₹")
        return float(single_price[1]) * amount

    def clear_basket_input_quantity(self):
        self.driver.find_element_by_class_name(self.input_product_number_field).clear()

