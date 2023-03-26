import time
from plyer import notification
#Single day men needs to drink at least 3.7 litres of water for good health.
#Single Day women needs to drink at least 2.7 litres of water for good health.
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water Now!!!!!",
            message = "Single day men needs to drink at least 3.7 litres of water for good health. Single Day women needs to drink at least 2.7 litres of water for good health.",
            app_icon = "C:\\Users\\Dell\\Desktop\\Python files\\Python Projects linked with the my_drive\\Drinking Water Reminder\\Drinking_water_icon.ico",
            timeout = 6
        )
        time.sleep(10)
#Here we can make this program to run in the background by excecuting [pythonw ./py_file_name] code in the terminal. 
