import threading
from ReaderBOT import ReaderBOT


reader1 = ReaderBOT("url1.csv", "data1.csv", 328, 10001)
# reader2 = ReaderBOT("url1.csv", "data2.csv", 201, 401)
# reader3 = ReaderBOT("url1.csv", "data3.csv", 401, 601)
# reader4 = ReaderBOT("url1.csv", "data4.csv", 601, 801)


def run_reader(reader):
    reader.extract_data_form_start_mesa_id_to_end_mesa_id()


thread1 = threading.Thread(target=run_reader, args=(reader1,))
# thread2 = threading.Thread(target=run_reader, args=(reader2,))
# thread3 = threading.Thread(target=run_reader, args=(reader3,))
# thread4 = threading.Thread(target=run_reader, args=(reader4,))

thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()

thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
