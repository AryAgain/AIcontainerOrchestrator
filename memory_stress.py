import time

def allocate_memory():
    memory_hog = []
    while True:
        memory_hog.append(' ' * 10**7)  # Allocate 10MB each iteration
        time.sleep(0.1)  

if __name__ == "__main__":
    allocate_memory()