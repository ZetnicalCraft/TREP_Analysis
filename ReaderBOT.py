import time
import pandas
import logging
from Extractor import Extractor

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class ReaderBOT:

    def __init__(self, name_of_archive_to_read: str, name_of_archive_to_save: str, start_mesa_id: int, end_mesa_id: int):
        self.name_of_archive_to_read = name_of_archive_to_read
        self.name_of_archive_to_save = name_of_archive_to_save
        self.start_mesa_id = start_mesa_id
        self.end_mesa_id = end_mesa_id
        self.extractor = Extractor(name_of_archive_to_read)

    def extract_data_form_start_mesa_id_to_end_mesa_id(self):
        logging.debug(f"Iniciando la extracción de datos desde la mesa: {self.start_mesa_id} a la {self.end_mesa_id - 1}")
        for mesa_id in range(self.start_mesa_id, self.end_mesa_id):  # (start, end) includes the start but not the end.
            start_time = time.perf_counter()
            logging.debug(f"Procesando mesa ID: {mesa_id}")
            page_souped = self.extractor.get_webpage_by_mesa_id(mesa_id)
            html_page_container = page_souped.find_all("td", {"class": "ng-binding"})
            archive_of_mesa_id = self.append_data_previously_extracted_to_archive_of_mesa_id(html_page_container)
            self.save_to_database_by_database_name(archive_of_mesa_id)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            logging.debug(f"Tiempo de procesamiento para Mesa ID {mesa_id}: {elapsed_time:.2f} segundos.")

    @staticmethod
    def append_data_previously_extracted_to_archive_of_mesa_id(html_page_container):
        archive_of_mesa_id = []
        for line_of_tag_td in range(44, 71):
            archive_of_mesa_id.append(html_page_container[line_of_tag_td].text)
        return archive_of_mesa_id

    def save_to_database_by_database_name(self, archive_of_mesa_id: []):
        data_frame = pandas.DataFrame(archive_of_mesa_id)
        data_frame = data_frame.transpose()
        data_frame.to_csv(self.name_of_archive_to_save, index=False)
