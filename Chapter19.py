""" Chapter 19 exercises  """
from threading import Thread
import time
import os

answer = None


def readposint():
    """verifies if input is a valid positive integer"""
    global start_time, answer
    start_time = time.time()
    answer = input("Enter a number:\n")
    time.sleep(0.001)

    try:
        is_int = int(answer)
    except:
        raise ValueError("{} is not an integer".format(answer))

    if is_int < 0:
        raise ValueError("{} is not a positive integer".format(is_int))

    print("{} is a valid response".format(is_int))


def time_out():
    """exit script if there is no input after 10 seconds"""
    time_limit = 10
    while True:
        time_taken = time.time() - start_time
        if answer is not None:
            break

        if time_taken > time_limit:
            print("Time's up !!! \n" f"You took {time_taken} seconds.")
            os._exit(1)
        time.sleep(0.001)


# call both functions at the same time
t1 = Thread(target=readposint)
t2 = Thread(target=time_out)
t1.start()
t2.start()
