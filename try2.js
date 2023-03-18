function wait_for_working_hours(start_time, end_time) {
    while (true) {
        var now = new Date();
        var start = new Date(now.toDateString() + " " + start_time);
        var end = new Date(now.toDateString() + " " + end_time);
        if (now < start) {
            // working hours have not started yet, wait until start_time
            var time_to_wait = (start - now) / 1000;
            console.log("Waiting " + time_to_wait + " seconds until working hours start...");
            setTimeout(() => {}, time_to_wait * 1000);
        } else if (now >= end) {
            // working hours are over, wait until tomorrow
            var tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
            var start_tomorrow = new Date(tomorrow.toDateString() + " " + start_time);
            var time_to_wait = (start_tomorrow - now) / 1000;
            console.log("Working hours are over. Waiting " + time_to_wait + " seconds until tomorrow...");
            setTimeout(() => {}, time_to_wait * 1000);
        } else {
            // working hours are ongoing
            var start_plus_6_hours = new Date(now.getTime() + 8 * 60 * 60 * 1000);
            if (start_plus_6_hours < now) {
                // it's already past the time to update leads, wait until tomorrow
                var tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
                var start_tomorrow = new Date(tomorrow.toDateString() + " " + start_time);
                var time_to_wait = (start_tomorrow - now) / 1000;
                console.log("Working hours are ongoing, but it's too late to update leads. Waiting " + time_to_wait + " seconds until tomorrow...");
                setTimeout(() => {}, time_to_wait * 1000);
            } else {
                // calculate the time to wait before updating leads
                var time_to_wait = (start_plus_6_hours - now) / 1000;
                console.log("Working hours are ongoing. Waiting " + time_to_wait + " seconds before updating leads...");
                setTimeout(() => {
                    // update the leads
                    console.log("Updating leads...");
                    // wait for another 6 hours before updating leads again
                    setTimeout(() => {}, 6 * 60 * 60 * 1000);
                }, time_to_wait * 1000);
                break;
            }
        }
    }
}

wait_for_working_hours("10:00", "19:00");
