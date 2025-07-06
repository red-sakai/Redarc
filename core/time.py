import time
import threading

start_time = time.time()

def wait(seconds):
    time.sleep(seconds)

def now():
    return round(time.time() - start_time, 2)

def schedule_after(delay, callback):
    threading.Timer(delay, callback).start()

def schedule_every(interval, callback):
    def loop():
        while True:
            time.sleep(interval)
            callback()
    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
