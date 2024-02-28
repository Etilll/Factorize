import multiprocessing
from time import time
import concurrent.futures

def factorize_nomultiprocess(*number):
    table = []
    a, b, c, d = None, None, None, None
    timer = time()
    for item in number:
        new_list = []
        for i in range(1, item + 1):
            if item % i == 0:
                new_list.append(i)
        table.append(new_list)
        
    print(f"{time() - timer}")
    return table
      
def factorize(*number):
    a, b, c, d = None, None, None, None
    timer = time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        a, b, c, d = executor.map(calculate, number)
    
    print(f"{time() - timer}")
    return a, b, c, d
        
def calculate(number):
    llist = []
    for i in range(1, number + 1):
        if number % i == 0:
            llist.append(i)
            
    return llist

#a, b, c, d  = factorize_nomultiprocess(128, 255, 99999, 10651060)
a, b, c, d  = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
