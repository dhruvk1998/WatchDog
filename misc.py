import datetime
import time

def wait_for_working_hours(start_time, end_time):
    while True:
        now = datetime.datetime.now().time()
        start = datetime.datetime.strptime(start_time, "%H:%M").time()
        end = datetime.datetime.strptime(end_time, "%H:%M").time()
        start_plus_6_hours = datetime.datetime.combine(datetime.date.today(), now) + datetime.timedelta(seconds=10)
        if now < start:
            # working hours have not started yet, wait until start_time
            time_to_wait = (datetime.datetime.combine(datetime.date.today(), start) - datetime.datetime.now()).total_seconds()
            print(f"{now}.  Waiting {time_to_wait} seconds until working hours start...\n")
            time.sleep(time_to_wait)
        elif now >= end:
            # working hours are over, wait until tomorrow
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            start_tomorrow = datetime.datetime.combine(tomorrow, datetime.datetime.strptime(start_time, "%H:%M").time()).time()
            time_to_wait = (datetime.datetime.combine(tomorrow, start) - datetime.datetime.now()).total_seconds()
            print(f"{now}.  Working hours are over. Waiting {time_to_wait} seconds until tomorrow at {start_time}...\n")
            time.sleep(time_to_wait)
        else:
            # working hours are ongoing
            if start_plus_6_hours.time() > end:
                # it's already past the time to update leads, wait until tomorrow
                tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                start_tomorrow = datetime.datetime.combine(tomorrow, datetime.datetime.strptime(start_time, "%H:%M").time()).time()
                time_to_wait = (datetime.datetime.combine(tomorrow, start) - datetime.datetime.now()).total_seconds()
                print(f"{now}. Working hours are ongoing, but it's too late to update leads. Waiting {time_to_wait} seconds until tomorrow at {start_time}...\n")
                time.sleep(time_to_wait)
            else:
                # calculate the time to wait before updating leads
                time_to_wait = (start_plus_6_hours - datetime.datetime.now()).total_seconds()
                print(f"{now}. Working hours are ongoing. Waiting {time_to_wait} seconds before updating leads... \n")
                time.sleep(time_to_wait)
                # update the leads
                print(f"{start_plus_6_hours}. Updating leads... \n")
                # wait for another 6 hours before updating leads again
                time.sleep(10)
                print(f"{now}. Waiting for 6 hours within working hours... ")

def get_start_tomorrow(start_time):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return datetime.datetime.combine(tomorrow, datetime.datetime.strptime(start_time, "%H:%M").time()).time()

wait_for_working_hours("10:00", "19:00")

# Usage example: 
# start_time = "10:00"
# end_time = "19:00"
# start_tomorrow = get_start_tomorrow(start_time)
# print(f"The next working day starts at {start_tomorrow}")