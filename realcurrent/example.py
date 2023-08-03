# example.py

from concurrent import concurrent, execute_concurrent
import time

start = time.time()
@concurrent
def add(a, b):
    for i in range(100000):
        b=b+a
    return a + b

@concurrent
def multiply(a, b):
    for i in range(1000):
        b=b*a
    return a * b

@concurrent
def subtract(a, b):
    for i in range(1000):
        b=b-a
    return a - b

if __name__ == "__main__":
    funcs = [add, multiply, subtract]
    args = [(5, 10), (3, 7), (15, 6)]

    results = execute_concurrent(funcs, args)
    print(results)
    end = time.time()
    print("the running process took ",end - start," seconds")
