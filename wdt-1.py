import datetime
import time

def wait_for_working_hours(start_time, end_time):
    while True:
        now = datetime.datetime.now().time()
        start = datetime.datetime.strptime(start_time, "%H:%M").time()
        end = datetime.datetime.strptime(end_time, "%H:%M").time()
        if start <= now <= end:
            def update_leads():
                    i = 0
                    while i < 10:
                        print("Waiting for working hours...")
                        time.sleep(60)
                        i += 1
                    # calculate the time to wait before updating leads
                    if datetime.datetime.combine(datetime.date.today(), end) < datetime.datetime.now():
                        continue  # working hours are over, skip to the next iteration of the loop
                    start_plus_6_hours = datetime.datetime.combine(datetime.date.today(), start) + datetime.timedelta(hours=36000)
                    if start_plus_6_hours < datetime.datetime.now():
                        continue  # it's already past the time to update leads, skip to the next iteration of the loop
                    time_to_wait = (start_plus_6_hours - datetime.datetime.now()).total_seconds()
                    # wait for the required time
                    print("Waiting for 6 hours within working hours...")
                    time.sleep(time_to_wait)
                    # update the leads
                    print("Updating leads after 6 hours within working hours...")
            update_leads()


wait_for_working_hours("10:00", "10:25")


'''
if datetime.datetime.combine(datetime.date.today(), end) < datetime.datetime.now():
    continue  # working hours are over, skip to the next iteration of the loop
start_plus_6_hours = datetime.datetime.combine(datetime.date.today(), start) + datetime.timedelta(hours=6)
if start_plus_6_hours < datetime.datetime.now():
    continue  # it's already past the time to update leads, skip to the next iteration of the loop
time_to_wait = (start_plus_6_hours - datetime.datetime.now()).total_seconds()
'''