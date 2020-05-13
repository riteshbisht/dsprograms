from time import time

def calculate_time(func):
    def inner(*args, **kwargs):
        timestart = time()
        func(*args, **kwargs)
        timeend = time()
        print("Time Taken:- {} ".format(timeend -timestart))
    return inner
