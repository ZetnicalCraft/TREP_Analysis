import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Extractor:

    def __init__(self, name_of_archive_to_read: str):
        self.options = ChromeOptions()
        self.options.add_argument("--headless=new")
        self.max_seconds_to_wait = 10
        self.name_of_archive_to_read = name_of_archive_to_read
        self.url_to_extract = ""

    def set_url_to_extract_by_mesa_id(self, mesa_id: int):
        data_frame = pandas.read_csv(self.name_of_archive_to_read, header=None)
        wished_line = data_frame.iloc[mesa_id-1]
        self.url_to_extract = str(wished_line[0])

    def get_webpage_by_mesa_id(self, mesa_id: int):
        self.set_url_to_extract_by_mesa_id(mesa_id)
        driver = webdriver.Chrome(options=self.options)
        page_soup = None

        while True:
            try:
                driver.get(self.url_to_extract)
                waiter = webdriver.support.wait.WebDriverWait(driver, self.max_seconds_to_wait)
                waiter.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, '[ng-repeat="pid in data.pids"]')))
                page_soup = BeautifulSoup(driver.page_source, "html.parser")
                break
            except TimeoutException:
                print("Excepción: No se encontraron elementos dentro del tiempo de espera. Reintentando...")
            finally:
                driver.quit()

        return page_soup
