import threading
import queue
from complex import Complex, is_prisonier
import numpy as np
from PIL import Image
from tqdm import tqdm
import time

dim = 2000
n_thread = 1

div = 2.5 / (dim/2)
width = dim
heigth = dim

c = Complex.from_algebra(-1.2, 0)


q = queue.Queue()
end = np.zeros((width,heigth, 3))
def worker():
    dones = 0
    while True:
        x,y = q.get()
        z0 = Complex.from_algebra(x*div,y*div)
        end[int(x+width/2),int(y+heigth/2)] = is_prisonier(z0, c)[1]
        dones+=1
        if dones % int(dim**2 / 30) == 0:
            print(f"[{threading.current_thread().getName()}] done {dones/n_thread/(dim**2)*100:.3}%")
        q.task_done()

for i in range(n_thread):
    threading.Thread(target=worker, daemon=True).start()

for x in tqdm(range(int(-width/2), int(width/2), 1)):
    for y in range(int(-heigth/2), int(heigth/2), 1):
        q.put((x,y))

q.join()
print('Fini les calules')
