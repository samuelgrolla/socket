from threading import Thread #importiamo il thread
import time,datetime 

def thread1():
  print("Thread 1 iniziato") #inizio del thread 1
  time.sleep(10)
  print("Thread 1 finito") #fine del thread 1
  

def thread2():
  print("Thread 2 iniziato") #inizio del thread 2
  time.sleep(4)
  print("Thread 2 finito") #fine del thread 2

print("Main iniziato")  #inizio del Main

start_time=time.time()
t1 = Thread(target=thread1) #thread1 targato
t2 = Thread(target=thread2)#thread2 targato
t1.start()
t2.start()
time.sleep(2)
end_time=time.time()

print(f"Main finito in {end_time-start_time}") #messaggio di fine Main