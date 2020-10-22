class Home:

    def __init__(self, driver):
        self.driver = driver

        self.shop_link_text = "Shop"
        self.arrivals_class_name = "woocommerce-LoopProduct-link"
        self.sliders_class = "n2-ss-slide-fill"

    def click_shop(self):
        self.driver.find_element_by_link_text(self.shop_link_text).click()

    def find_count_arrivals(self):
        arrivals_count = len(self.driver.find_elements_by_class_name(self.arrivals_class_name))
        return arrivals_count

    def count_sliders(self):
        count_sliders = len(self.driver.find_elements_by_class_name(self.sliders_class))
        return count_sliders

    def find_click_arrivals_img(self, position):
        self.driver.find_elements_by_class_name(self.arrivals_class_name)[position].click()

    def get_book_title_arrivals(self, position):
        find_name = self.driver.find_elements_by_class_name(self.arrivals_class_name)[position].text
        return find_name



