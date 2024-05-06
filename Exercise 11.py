import time 
t = time.localtime()
init_time = time.strftime("%H-%M-%S", t)
init_time = int(init_time[0] + init_time[1])

while True:
    curr_time = time.strftime("%H", time.localtime())
    if int(curr_time) - int(init_time) == 2:
        print("Drink water Please!")
        init_time = time.strftime("%H", t)