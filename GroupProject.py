import threading
import multiprocessing

# Function for threading example
def threading_task(name):
    print(f"Thread {name} is running")

# Function for multiprocessing example
def multiprocessing_task(name):
    print(f"Process {name} is running")

def main():
    # Using threading
    threads = []
    for i in range(3):
        t = threading.Thread(target=threading_task, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("Threading example finished\n")
    
    # Using multiprocessing
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=multiprocessing_task, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print("Multiprocessing example finished")

if __name__ == "__main__":
    main()

"""
Benefits and Shortcomings of Threading and Multiprocessing:

Threading:
- Benefits:
  1. Low memory usage since threads share the same memory space.
  2. Good for I/O-bound tasks like file operations, network requests, or database queries.
  3. Faster communication between threads as they share memory.
- Shortcomings:
  1. Limited performance for CPU-bound tasks due to the Global Interpreter Lock (GIL).
  2. Risk of race conditions when multiple threads modify shared data.
  3. Deadlocks can occur if locks are not handled correctly.
- How to Address:
  - Use locks (threading.Lock) to prevent race conditions.
  - Use thread-local storage if each thread requires separate data.
  - Use thread pools (concurrent.futures.ThreadPoolExecutor) to manage threads efficiently.

Multiprocessing:
- Benefits:
  1. True parallel execution since each process runs in its own memory space.
  2. Ideal for CPU-intensive tasks like complex calculations and data processing.
  3. More fault-tolerant, as one process crashing doesn't affect others.
- Shortcomings:
  1. Higher memory usage since each process has its own memory space.
  2. Slower inter-process communication compared to threading.
  3. Requires data serialization (pickling) to share data between processes.
- How to Address:
  - Use multiprocessing.Manager to share data between processes safely.
  - Use shared memory (multiprocessing.shared_memory) for efficient data sharing.
  - Use process pools (multiprocessing.Pool) to manage multiple processes efficiently.

Choosing Between Them:
- Use threading for I/O-bound tasks where waiting is common (e.g., web scraping, downloading files).
- Use multiprocessing for CPU-bound tasks where heavy computation is needed (e.g., image processing, simulations).
- In some cases, a hybrid approach (both threading and multiprocessing) can be beneficial.
"""
