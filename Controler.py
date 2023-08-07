import threading
from ReaderBOT import ReaderBOT


reader1 = ReaderBOT("archivo1.csv", "salida1.csv", 1, 10)
# reader2 = ReaderBOT("archivo2.csv", "salida2.csv", 11, 20)
# reader3 = ReaderBOT("archivo3.csv", "salida3.csv", 21, 30)


def run_reader(reader):
    reader.extract_data_form_start_mesa_id_to_end_mesa_id()


thread1 = threading.Thread(target=run_reader, args=(reader1,))
# thread2 = threading.Thread(target=run_reader, args=(reader2,))
# thread3 = threading.Thread(target=run_reader, args=(reader3,))

thread1.start()
# thread2.start()
# thread3.start()

thread1.join()
# thread2.join()
# thread3.join()
