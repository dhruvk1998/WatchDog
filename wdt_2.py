import datetime
import time 

def update_leads(start_time, end_time):
    while True:
        now = datetime.datetime.now().time()        #activity_time = @{Lead:mx_Accounts_Activity,} 
        start = datetime.datetime.strptime(start_time, "%H:%M").time()
        end = datetime.datetime.strptime(end_time, "%H:%M").time()
        # if the current time is already within the working hours, do nothing
        if start <= now <= end:
            # calculate the time to wait before updating leads
            end_plus_6_hours = datetime.datetime.combine(datetime.date.today(), end) + datetime.timedelta(hours=6)
            time_to_wait = (end_plus_6_hours - datetime.datetime.now()).total_seconds()
            # wait for the required time
            print("Waiting for 6 hours after the current time...")
            time.sleep(time_to_wait)
            # update the leads
            print("Updating leads after 6 hours of current time...")
        else:
            return


update_leads("10:00", "19:00")