import plyer
import time
from plyer import notification
import sys



def alert_bg(title_to_alert,msg,display_time,sleep_time):
    print(f"starting alert for {title_to_alert} background process")
    i=0
    while True:
        plyer.notification.notify(title=title_to_alert,message=msg,timeout = display_time)
        time.sleep(sleep_time *60)
        print(time.ctime())
        i=i+1
        if i ==10:
            break

def main():
    try:
        title_to_alert = input("Enter title for the notification:")
        msg = input("enter message to pop up for notification: ")
        display_time = int(input("enter how much time you want notification to stay: "))
        sleep_time = int(input("enter interval for notification in minutes: "))
        alert_bg(title_to_alert,msg,display_time, sleep_time)
    except:
        print("enter valid input")
        sys.exit()



main()
