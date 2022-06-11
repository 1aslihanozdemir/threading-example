from threading import Thread
import time


def thread_function(number):
    for i in range(number):
        print(str(i))
        time.sleep(1)

def function(number):
    for i in range(number):
        print(i)
        time.sleep(1)

num = int(input("sayı giriniz: "))
tf = Thread(target = thread_function,args=(num,))
tf.start()
f = Thread(target=function,args=(num,))
f.start()
