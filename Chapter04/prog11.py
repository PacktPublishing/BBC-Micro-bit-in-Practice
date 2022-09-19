def ping(i):
    if i > 0:
        print("Ping - " + str(i))
        return pong(i-1)

def pong(i):
    if i > 0:
        print("Pong - " + str(i))
        return ping(i-1)

ping(10)