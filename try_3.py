import datetime
import time

def wait_for_working_hours(start_time, end_time):
    while True:
        now = datetime.datetime.now().time()
        start = datetime.datetime.strptime(start_time, "%H:%M").time()
        end = datetime.datetime.strptime(end_time, "%H:%M").time()
        if now < start:
            # working hours have not started yet, wait until start_time
            time_to_wait = (datetime.datetime.combine(datetime.date.today(), now) - datetime.datetime.now()).total_seconds()
            print(f"Waiting {time_to_wait} seconds until working hours start...")
            time.sleep(time_to_wait)
        elif now >= end:
            # working hours are over, wait until tomorrow
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            start_tomorrow = datetime.datetime.combine(tomorrow, start).time()
            time_to_wait = (datetime.datetime.combine(tomorrow, now) - datetime.datetime.now()).total_seconds()
            print(f"Working hours are over. Waiting {time_to_wait} seconds until tomorrow...")
            time.sleep(time_to_wait)
        else:
            # working hours are ongoing
            start_plus_6_hours = datetime.datetime.combine(datetime.date.today(), now) + datetime.timedelta(minutes=3)
            if start_plus_6_hours < datetime.datetime.now():
                # it's already past the time to update leads, wait until tomorrow
                tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                start_tomorrow = datetime.datetime.combine(tomorrow, start).time() 
                time_to_wait = (datetime.datetime.combine(tomorrow, now) - datetime.datetime.now()).total_seconds()
                print(f"Working hours are ongoing, but it's too late to update leads. Waiting {time_to_wait} seconds until tomorrow...")
                time.sleep(time_to_wait)
            else:
                # calculate the time to wait before updating leads
                time_to_wait = (start_plus_6_hours - datetime.datetime.now()).total_seconds()
                print(f"Working hours are ongoing. Waiting {time_to_wait} seconds before updating leads...")
                time.sleep(time_to_wait)
                # update the leads
                print("Updating leads...")
                # wait for another 6 hours before updating leads again
                time.sleep(6 * 60 * 60)
                print("Waiting for 6 hours within working hours...")

wait_for_working_hours("10:00", "19:00")