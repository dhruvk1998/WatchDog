import datetime
import time


def wait_for_working_hours(start_time, end_time):
    while True:
        start = datetime.datetime.strptime(start_time, "%H:%M").time()
        now = datetime.datetime.now(tz=None).time()
        end = datetime.datetime.strptime(end_time, "%H:%M").time()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        wait_time = datetime.timedelta(hours=6)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        start_plus_6_hours = datetime.datetime.combine(tomorrow, now) + datetime.timedelta(hours=6)
        time_to_wait = (datetime.datetime.combine(tomorrow, now) - datetime.datetime.now())
        if now < start:
            # working hours have not started yet, wait until start_time
            time_to_wait = (datetime.datetime.combine(datetime.date.today(), start)- datetime.datetime.combine(datetime.date.today(), now)).total_seconds()
            print(f"{now}.  Waiting {time_to_wait} seconds until working hours start...")
            time.sleep(time_to_wait)
        elif now >= end:
            # working hours are over, wait until tomorrow
            # start_tomorrow = datetime.datetime.combine(tomorrow, start).time()
            time_to_wait = (datetime.datetime.combine(tomorrow, now) - datetime.datetime.now()).total_seconds()
            print(f"{now}.  Working hours are over. Waiting {time_to_wait} seconds until tomorrow... ")
            time.sleep(time_to_wait)
        else:
            # working hours are ongoing
            estimated_time = datetime.datetime.combine(datetime.date.today(), start) + datetime.timedelta(days=1) 
            print(f"Initiated on: {now},\n\nEstimated Time: {estimated_time}\n")
            if start_plus_6_hours < datetime.datetime.now():
                # it's already past the time to update leads, wait until tomorrow
                # start_tomorrow = datetime.datetime.combine(tomorrow, start).time()
                time_to_wait = (datetime.datetime.combine(tomorrow, now)- datetime.datetime.now(tz=None)).total_seconds()
                print(f"{now}. Working hours are ongoing, but it's too late to update leads. Waiting {start_plus_6_hours} Hours until tomorrow... ")
                time.sleep(time_to_wait)
            else:
                # calculate the time to wait before updating leads
                time_to_wait = (start_plus_6_hours - datetime.datetime.now(tz=None)).total_seconds()
                print(f"{timestamp}. Working hours are ongoing. Waiting {wait_time} Hours before updating leads... ")
                time.sleep(6*60*60)
                # update the leads
                print(f"{now}. Updating leads... ")
                # wait for another 6 hours before updating leads again
                time.sleep(6 * 60 * 60)
                print(f"{now}. Waiting for 6 hours within working hours... ")


wait_for_working_hours("10:00", "19:00")