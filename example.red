print("Starting")
wait(2)
print("Waited 2 seconds")

every(1):
    print("Tick", now())

after(5):
    print("Boom! After 5 seconds")
