#multi-process.py

#Example from Engineer Man on YouTube: "Threading vs Multiprocessing in Python" 165,570 views, Aug 19, 2018
#https://youtu.be/ecKWiaHCEKs
#Also: NeuralNine on YouTube: "Multiprocessing in Python" 12,489 views Jun 26, 2021
#https://youtu.be/GT10PnUFLlE


#Threading:
# - A new thread is spawned within the existing process
# - Starting a thread is faster than starting a process
# - Memory is shared between all threads
# - Mutexes often necessary to control access to shared data
# - One GIL (Global Interpreter Lock) for all threads

#Multiprocessing:
# - A new process is started independent from the first process
# - Starting a process is slower than starting a thread
# - Memory is not shared between processes
# - Mutexes not necessary (unless threading in the new process)
# - One GIL (Global Interpreter Lock) for each process

from multiprocessing import Process
import os
import math

def calc():
    for i in range(0, 4000000):
        math.sqrt(i)

if __name__ == '__main__': #necessary entry point if using multiprocess in Windows
    
    processes = []

    for i in range(os.cpu_count()):
        print('registering process %d' % i)
        processes.append(Process(target=calc))

    for process in processes:
        process.start()

    for process in processes:
        process.join()