from  threading import*

#print(threading.current_thread().getName())

# def display():
#     for i in range(1,11):
#         print("child")


# t = Thread(target=display)
# t.start()
# for i in range(1,11):
#     print("main thred")

# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("child")

# t = MyThread()
# t.start()
# for i in range(10):
#     print("Main-thread1")



# import time
# def wish(name):
#     for i in range(10):
#         print("good evening :",end="")
#         time.sleep(2)
#         print(name)


# t1 = Thread(target=wish, args=("vivek",))
# t2 = Thread(target=wish,args=("tiwari",))
# t1.start()
# t2.start()

import time
#l = Lock()
l = Semaphore(2)
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good Evening : ", end="")
        time.sleep(2)
        print(name)
    l.release()


t1 = Thread(target=wish, args=("VIvek",))
t2 = Thread(target=wish,args=("tiwari",))
t3 = Thread(target=wish,args=("notateckin",))
t4 = Thread(target=wish,args=("do",))
t5 = Thread(target=wish,args=("notdo",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


