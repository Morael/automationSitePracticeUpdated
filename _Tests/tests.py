from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from _Pages.homePage import Home
from _Pages.shopPage import Shop


class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Ja/PycharmProjects/Practice_automation/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test01_home_3sliders_only(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")

        sliders = Home(driver)
        sliders.click_shop()
        sliders = Shop(driver)
        sliders.click_home()
        sliders = Home(driver)
        sliders_count = sliders.count_sliders()
        self.assertEqual(sliders_count, 3, "Wrong number of sliders.")
        time.sleep(1)

    def test02_home_3arrivals_only(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        arrivals = Home(driver)
        arrivals.click_shop()
        arrivals = Shop(driver)
        arrivals.click_home()
        arrivals = Home(driver)
        arrivals_number = arrivals.find_count_arrivals()
        self.assertEqual(arrivals_number, 3, "class has different number of arrivals")

        time.sleep(1)

    def test03_home_arrivals_img_navigate(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        images = Home(driver)
        images.click_shop()
        images = Shop(driver)
        images.click_home()
        images = Home(driver)
        images_number = images.find_count_arrivals()
        self.assertEqual(images_number, 3, "class has different number of arrivals")
        images.find_click_arrivals_img(0)
        time.sleep(5)
        images = Shop(driver)
        self.assertEqual(images.find_add_to_basket_button(), images.is_add_basket_button_active(),"button is not displayed or enabled")

        time.sleep(1)

    def test04_home_arrivals_img_description(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        description = Home(driver)
        description.click_shop()
        description = Shop(driver)
        description.click_home()
        description = Home(driver)
        description_number = description.find_count_arrivals()
        self.assertEqual(description_number, 3, "class has different number of arrivals")
        description.find_click_arrivals_img(0)
        description = Shop(driver)
        self.assertEqual(description.find_add_to_basket_button(), description.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        description.click_description()
        description.check_description()

        time.sleep(1)

    def test05_home_arrivals_img_review(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        review = Home(driver)
        review.click_shop()
        review = Shop(driver)
        review.click_home()
        review = Home(driver)
        review_number = review.find_count_arrivals()
        self.assertEqual(review_number, 3, "class has different number of arrivals")
        review.find_click_arrivals_img(0)
        review = Shop(driver)
        self.assertEqual(review.find_add_to_basket_button(), review.is_add_basket_button_active(), "button is not displayed or enabled")
        review.click_reviews()
        review.check_reviews()

        time.sleep(1)

    def test06_home_arrivals_img_add_to_basket(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        basket = Home(driver)
        basket.click_shop()
        basket = Shop(driver)
        basket.click_home()
        basket = Home(driver)
        basket_number = basket.find_count_arrivals()
        self.assertEqual(basket_number, 3, "class has different number of arrivals")
        basket.find_click_arrivals_img(0)
        basket = Shop(driver)
        self.assertEqual(basket.find_add_to_basket_button(), basket.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        basket_product_number = basket.basket_number_of_products()
        basket.input_number_of_products(1)
        basket.click_add_to_basket_button()
        self.assertEqual(basket.basket_number_of_products(), basket_product_number + 1,
                         "number of products in basket is wrong")
        self.assertEqual(basket.check_price_of_product() * 1, basket.check_cost_in_basket(),
                         "cost of added products is not calculated well")

        time.sleep(1)

    def test07_home_arrivals_basket_more(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        more_books = Home(driver)
        more_books.click_shop()
        more_books = Shop(driver)
        more_books.click_home()
        more_books = Home(driver)
        more_books_number = more_books.find_count_arrivals()
        self.assertEqual(more_books_number, 3, "class has different number of arrivals")
        more_books.find_click_arrivals_img(0)
        more_books = Shop(driver)
        self.assertEqual(more_books.find_add_to_basket_button(), more_books.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        updated_basket = more_books.basket_number_of_products()
        more_books.input_number_of_products(1)
        more_books.click_add_to_basket_button()
        self.assertEqual(more_books.basket_number_of_products(), updated_basket + 1, "number of products in basket is wrong")
        updated_basket = more_books.basket_number_of_products()
        self.assertEqual(more_books.check_price_of_product() * updated_basket, more_books.check_cost_in_basket(),
                         "cost of added products is not calculated well")
        more_books.input_number_of_products(more_books.get_max_products_from_stock() + 1)
        more_books.click_add_to_basket_button()
        self.assertEqual(more_books.prompt_warning_product_number(),
                         f"Wartość nie może być większa niż {more_books.get_max_products_from_stock()}.",
                         "Warning prompts are different!")

        time.sleep(1)

    def test08_home_arrivals_basket_items(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        basket_item = Home(driver)
        basket_item.click_shop()
        basket_item = Shop(driver)
        basket_item.click_home()
        basket_item = Home(driver)
        basket_item_number = basket_item.find_count_arrivals()
        self.assertEqual(basket_item_number, 3, "class has different number of arrivals")
        basket_item.find_click_arrivals_img(0)
        basket_item = Shop(driver)
        self.assertEqual(basket_item.find_add_to_basket_button(), basket_item.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        updated_item = basket_item.basket_number_of_products()
        basket_item.input_number_of_products(1)
        basket_item.click_add_to_basket_button()
        self.assertEqual(basket_item.basket_number_of_products(), updated_item + 1,
                         "number of products in basket is wrong")
        updated_basket = basket_item.basket_number_of_products()
        self.assertEqual(basket_item.check_price_of_product() * updated_basket, basket_item.check_cost_in_basket(),
                         "cost of added products is not calculated well")
        basket_item.click_on_basket_in_menu()
        self.assertEqual(driver.current_url, "http://practice.automationtesting.in/basket/", "Wrong page address!")

        time.sleep(1)

    def test09_home_arrivals_basket_items_coupon(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()

        coupon = Home(driver)
        coupon.click_shop()
        coupon = Shop(driver)
        coupon.click_home()
        coupon = Home(driver)
        basket_item_number = coupon.find_count_arrivals()
        self.assertEqual(basket_item_number, 3, "class has different number of arrivals")
        coupon.find_click_arrivals_img(0)
        coupon = Shop(driver)
        self.assertEqual(coupon.find_add_to_basket_button(), coupon.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        updated_item = coupon.basket_number_of_products()
        coupon.input_number_of_products(1)
        coupon.click_add_to_basket_button()
        self.assertEqual(coupon.basket_number_of_products(), updated_item + 1,
                         "number of products in basket is wrong")
        updated_basket = coupon.basket_number_of_products()
        self.assertEqual(coupon.check_price_of_product() * updated_basket, coupon.check_cost_in_basket(),
                         "cost of added products is not calculated well")
        coupon.click_on_basket_in_menu()
        self.assertEqual(driver.current_url, "http://practice.automationtesting.in/basket/", "Wrong page address!")
        coupon.add_coupon_code("krishnasakinala")
        self.assertEqual(coupon.check_coupon_discount_value(), "50.00",
                         "Coupon discount krishnasakinala has value different than 50.00")
        self.assertEqual(coupon.check_coupon_correctness_from_total(), 50.0, "Wrong coupon calculations.")
        coupon.remove_coupon()
        coupon.remove_book_from_basket()

        time.sleep(1)

    def test10_home_basket_items_coupon_less_450(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()
        # driver.refresh()

        less_450 = Home(driver)
        less_450.click_shop()
        less_450 = Shop(driver)
        less_450.click_home()
        less_450 = Home(driver)
        basket_item_number = less_450.find_count_arrivals()
        self.assertEqual(basket_item_number, 3, "class has different number of arrivals")
        less_450.find_click_arrivals_img(2)
        less_450 = Shop(driver)
        self.assertEqual(less_450.find_add_to_basket_button(), less_450.is_add_basket_button_active(), "button is not displayed or enabled")
        updated_item = less_450.basket_number_of_products()
        less_450.input_number_of_products(1)
        less_450.click_add_to_basket_button()
        self.assertEqual(less_450.basket_number_of_products(), updated_item + 1, "number of products in basket is wrong")
        updated_basket = less_450.basket_number_of_products()
        self.assertEqual(less_450.check_price_of_product() * updated_basket, less_450.check_cost_in_basket(), "cost of added products is not calculated well")
        less_450.click_on_basket_in_menu()
        self.assertEqual(driver.current_url, "http://practice.automationtesting.in/basket/", "Wrong page address!")
        less_450.add_coupon_code("krishnasakinala")
        less_450.coupon_warning_text_displayed()
        self.assertEqual(less_450.coupon_warning_text(), "The minimum spend for this coupon is ₹450.00.", "Can't find a warning prompt for products < 450.")

        time.sleep(3)

    def test11_home_basket_item_remove_book(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()
        # driver.refresh()

        remove = Home(driver)
        remove.click_shop()
        remove = Shop(driver)
        remove.click_home()
        remove = Home(driver)
        basket_item_number = remove.find_count_arrivals()
        self.assertEqual(basket_item_number, 3, "class has different number of arrivals")
        remove.find_click_arrivals_img(2)
        remove = Shop(driver)
        self.assertEqual(remove.find_add_to_basket_button(), remove.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        updated_item = remove.basket_number_of_products()
        remove.input_number_of_products(1)
        remove.click_add_to_basket_button()
        self.assertEqual(remove.basket_number_of_products(), updated_item + 1,
                         "number of products in basket is wrong")
        updated_basket = remove.basket_number_of_products()
        self.assertEqual(remove.check_price_of_product() * updated_basket, remove.check_cost_in_basket(),
                         "cost of added products is not calculated well")
        remove.click_on_basket_in_menu()
        self.assertEqual(driver.current_url, "http://practice.automationtesting.in/basket/", "Wrong page address!")
        remove.remove_book_from_basket()
        self.assertFalse(remove.check_remove_book_button(), "Remove Button is still visible !")

        time.sleep(3)

    def test12_home_basket_item_add_book(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()
        # driver.refresh()

        add_rem_book = Home(driver)
        add_rem_book.click_shop()
        add_rem_book = Shop(driver)
        add_rem_book.click_home()
        add_rem_book = Home(driver)
        basket_item_number = add_rem_book.find_count_arrivals()
        self.assertEqual(basket_item_number, 3, "class has different number of arrivals")
        add_rem_book.find_click_arrivals_img(2)
        add_rem_book = Shop(driver)
        self.assertEqual(add_rem_book.find_add_to_basket_button(), add_rem_book.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        updated_item = add_rem_book.basket_number_of_products()
        add_rem_book.input_number_of_products(1)
        add_rem_book.click_add_to_basket_button()
        self.assertEqual(add_rem_book.basket_number_of_products(), updated_item + 1,
                         "number of products in basket is wrong")
        updated_basket = add_rem_book.basket_number_of_products()
        self.assertEqual(add_rem_book.check_price_of_product() * updated_basket, add_rem_book.check_cost_in_basket(),
                         "cost of added products is not calculated well")
        add_rem_book.click_on_basket_in_menu()
        self.assertEqual(driver.current_url, "http://practice.automationtesting.in/basket/", "Wrong page address!")
        add_rem_book.check_basket_input_quantity()
        add_rem_book.raise_basket_input_quantity(3)
        add_rem_book.lower_basket_input_quantity(1)
        add_rem_book.check_update_button_is_displayed()
        add_rem_book.click_basket_update_cart_button()

        time.sleep(3)

    def test13_home_basket_book_final_price(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()
        # driver.refresh()

        final_price = Home(driver)
        final_price.click_shop()
        final_price = Shop(driver)
        final_price.click_home()
        final_price = Home(driver)
        basket_item_number = final_price.find_count_arrivals()
        self.assertEqual(basket_item_number, 3, "class has different number of arrivals")
        arrival_book_name = final_price.get_book_title_arrivals(2)
        final_price.find_click_arrivals_img(2)
        final_price = Shop(driver)
        self.assertEqual(final_price.find_add_to_basket_button(), final_price.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        updated_item = final_price.basket_number_of_products()
        final_price.input_number_of_products(1)
        final_price.click_add_to_basket_button()
        self.assertEqual(final_price.basket_number_of_products(), updated_item + 1,
                         "number of products in basket is wrong")
        updated_basket = final_price.basket_number_of_products()
        self.assertEqual(final_price.check_price_of_product() * updated_basket, final_price.check_cost_in_basket(),
                         "cost of added products is not calculated well")
        final_price.click_on_basket_in_menu()
        book_in_basket = final_price.name_of_first_book_in_basket()
        self.assertIn(book_in_basket, arrival_book_name, "Wrong book's title in the basket !")
        final_price.check_basket_input_quantity()
        final_price.lower_basket_input_quantity(5)
        final_price.raise_basket_input_quantity(2)
        final_price.click_basket_update_cart_button()
        time.sleep(2)
        self.assertEqual(final_price.check_total_basket_product_grid(), final_price.count_multiple_product_price(2), "Values in the upper grid are counted wrong !")

        time.sleep(3)

    def test14_home_basket_update(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        driver.delete_all_cookies()
        driver.refresh()

        final_price = Home(driver)
        final_price.click_shop()
        final_price = Shop(driver)
        final_price.click_home()
        final_price = Home(driver)
        basket_item_number = final_price.find_count_arrivals()
        self.assertEqual(basket_item_number, 3, "class has different number of arrivals")
        arrival_book_name = final_price.get_book_title_arrivals(2)
        final_price.find_click_arrivals_img(2)
        final_price = Shop(driver)
        self.assertEqual(final_price.find_add_to_basket_button(), final_price.is_add_basket_button_active(),
                         "button is not displayed or enabled")
        updated_item = final_price.basket_number_of_products()
        final_price.input_number_of_products(1)
        final_price.click_add_to_basket_button()
        self.assertEqual(final_price.basket_number_of_products(), updated_item + 1,
                         "number of products in basket is wrong")
        updated_basket = final_price.basket_number_of_products()
        self.assertEqual(final_price.check_price_of_product() * updated_basket, final_price.check_cost_in_basket(),
                         "cost of added products is not calculated well")
        final_price.click_on_basket_in_menu()
        book_in_basket = final_price.name_of_first_book_in_basket()
        self.assertIn(book_in_basket, arrival_book_name, "Wrong book's title in the basket !")
        final_price.check_basket_input_quantity()
        final_price.lower_basket_input_quantity(5)
        final_price.raise_basket_input_quantity(2)
        final_price.click_basket_update_cart_button()

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed.")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Ja/PycharmProjects/Practice_automation/_Reports"))

