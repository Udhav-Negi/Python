from win10toast import ToastNotifier
import time 

init_time = int(time.strftime("%M"))
while True:
    curr_time = int(time.strftime("%M"))
    if curr_time - init_time >= 1:
        print("inside if")
        init_time = int(time.strftime("%M"))
        toast = ToastNotifier()
        toast.show_toast(
            "Notification",
            "Drink Water",
            duration = 20,
            # icon_path = "icon.ico",
            threaded = True,
        )
    else :
        print("Inside else")