import thread
import threading
import time

def print_time(threadName, delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count += 1
        print "%s: %s" %(threadName, time.ctime(time.time()))

##try:
##    thread.start_new_thread(print_time, ("t1", 2))
##    thread.start_new_thread(print_time, ('t2', 4))
##    
##except:
##    print "error: unable to create thread"

exitFlag = 0
class myThread(threading.Thread):
    #overwriting __init__(Self[,args]) method to add more args
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)#calling self creating method
        self.name = name
        self.counter = counter
    #overwriting run(self[,args]) method to tell thread what to do when started
    def run(self):
        print "Starting " + self.name
        print_time1(self.name, self.counter, 5) #always print 5 times
        print "Exiting " + self.name
def print_time1(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time())) 
        counter -= 1

#create new threads
thread1 = myThread(1, 't1', 2)
thread2 = myThread(2, 't2', 3)

#Start new threads
thread1.start()
thread2.start()

#keep track of all threads
threads = []
threads.append(thread1)
threads.append(thread2)

#wait for all threads to complete
for t in threads:
    t.join()
print "exiting main thread\n"

