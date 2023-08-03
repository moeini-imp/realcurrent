import time

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
add_test=add(5,10)
multiply_test=multiply(3,7)
subtract_test=subtract(15,6)
test.append(add_test)
test.append(multiply_test)
test.append(subtract_test)
print(test)
end = time.time()
print("the running process took ",end - start," seconds")