from source.speccontroler import Controler
import time

spec = Controler()

dataList = []
for t in range(0, 10*60, 5):
    spec.acquire()
    dataList.append(spec.data)
    time.sleep(5*60)

# save the data
