# Drinking water notification system by cwh 
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water", 
            message = "Drink water now", 
            app_icon = "./icon.ico",
            timeout = 2
        )
        time.sleep(6)

