import time
import threading
start = time.time()

def add(a, b):
    for i in range(1000000):
        b=b+a
    return a + b


def multiply(a, b):
    for i in range(1000):
        b=b*a
    return a * b


def subtract(a, b):
    for i in range(1000):
        b=b-a
    return a - b

test=[]

add_test=threading.Thread(target=add,args=[5,10])
multiply_test=threading.Thread(target=multiply,args=[7,3])
subtract_test=threading.Thread(target=subtract,args=[15,6])
add_test.start(),multiply_test.start(),subtract_test.start()
test.append(add_test)
test.append(multiply_test)
test.append(subtract_test)
print(test)
end = time.time()
print("the running process took ",end - start," seconds")