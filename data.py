from pynput import mouse
import datetime
import math

start = []
stop = []
timestamp_start = 0
timestamp_stop = 0


def on_click(x, y, button, pressed):
    global timestamp_start
    global timestamp_stop
    if pressed:
        if len(start) == 0:
            start.append(x)
            start.append(y)
            timestamp_start = datetime.datetime.now()
            print(start)
            print("add stop...")
        else:
            if len(stop) == 0:
                stop.append(x)
                stop.append(y)
                timestamp_stop = datetime.datetime.now()
                print(stop)
                print("start: ", start, " at ", timestamp_start)
                print("stop: ", stop, " at ", timestamp_stop)
                traveltime = (timestamp_stop - timestamp_start).total_seconds()
                print("Write to csv...")
                toCsv(start, stop, traveltime)
                return False

def toCsv(start, stop, traveltime):
    global distance
    distance = math.dist(start, stop)
    new_row = ",".join([str(start[0]), str(start[1]), str(stop[0]), str(stop[1]), str(distance), str(traveltime)])
    print(new_row)
    with open('test.csv', 'a') as myfile:
        myfile.write(new_row + "\n")
        myfile.close()

with mouse.Listener(on_click=on_click) as listener:
    print("add start...")
    listener.join()
