import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper
@timer
def exampleF(n):
    time.sleep(n)

exampleF(2)   # exampleF ran in 2.000286340713501 time