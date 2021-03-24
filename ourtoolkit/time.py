import time

def measure_time(function, verbose=True, *args, **kwargs):
    start = time.perf_counter_ns()
    duration = (time.perf_counter_ns() - start)/10**6
    if verbose:
        print(f"The function {function.__name__} took {duration:.3f} miliseconds to run!")
    return duration
    
    
if __name__ == "__main__":
    import random
    n = int(input("Choose a big number: "))
    randomlist = []
    for i in range(0,n):
        randomlist.append(random.randint(1,n))
    
    print(measure_time(randomlist.sort))