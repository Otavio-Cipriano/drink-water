import time
# import sched
from win10toast import ToastNotifier
toaster = ToastNotifier()

# event_schedule = sched.scheduler(time.time, time.sleep)

def message():
    toaster.show_toast("Drink Water",
    "Lembre-se de se manter " +
    "hidratado! Beba pelo menos 250 ml de água a cada duas " +
    "horas para manter seu corpo funcionando bem. Cuide-se! 💧", icon_path= 'water.ico', 
    duration=5)
    exit()

# def do_something():
#     message()
#     event_schedule.enter(7200, 1, do_something)

# event_schedule.enter(7200, 1, do_something)
# event_schedule.run()

message()
