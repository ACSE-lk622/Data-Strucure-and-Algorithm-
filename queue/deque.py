from collections import deque
import queue as q 
from multiprocessing import Queue
customQueue = deque(maxlen=3)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4) #if size is full , it will overide the first element
print(customQueue)
print(customQueue.popleft())
print(customQueue)



customqueue2 = Queue(maxsize= 3)
customqueue2.put(1)
customqueue2.get(1)

list = [1,5,3,6]
value = list.pop()
print(list)