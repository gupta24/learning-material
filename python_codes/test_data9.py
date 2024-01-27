import time

def my_gen(num):
    ind = 1
    while ind <= num:
        yield ind ** 2
        ind += 1
    
    message = "sqrt for given item is done!"
    yield message
    


for sqrt_item in my_gen(10):
    print(sqrt_item)
    #time.sleep(2)
    