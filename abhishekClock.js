function wait_for_working_hours(start_time, end_time) {
  while (true) {
    var now = new Date();
    var start = new Date("01/01/1970 " + start_time);
    var end = new Date("01/01/1970 " + end_time);
    var wait_time = 6 * 60 * 60 * 1000; // 6 hours in milliseconds
    var start_plus_6_hours = new Date(now.getTime() + wait_time);
    if (now < start) {
      // working hours have not started yet, wait until start_time
      var time_to_wait = start - now;
      console.log(
        now +
          ". Waiting " +
          time_to_wait / 1000 +
          " seconds until working hours start..."
      );
      setTimeout(function () {}, time_to_wait);
    } else if (now >= end) {
      // working hours are over, wait until tomorrow
      var tomorrow = new Date(now.getTime() + 24 * 60 * 60 * 1000);
      var time_to_wait = tomorrow - now;
      console.log(
        now +
          ". Working hours are over. Waiting " +
          time_to_wait / 1000 +
          " seconds until tomorrow..."
      );
      setTimeout(function () {}, time_to_wait);
    } else {
      // working hours are ongoing
      var start_plus_6_hours = new Date(now.getTime() + wait_time);
      console.log(
        "Initiated on: " + now + ",\n\nEstimated Time: " + start_plus_6_hours
      );
      if (start_plus_6_hours < now) {
        // it's already past the time to update leads, wait until tomorrow
        var tomorrow = new Date(now.getTime() + 24 * 60 * 60 * 1000);
        var time_to_wait = tomorrow - now;
        console.log(
          now +
            ". Working hours are ongoing, but it's too late to update leads. Waiting " +
            wait_time / 1000 +
            " Hours until tomorrow... "
        );
        setTimeout(function () {}, time_to_wait);
      } else {
        // calculate the time to wait before updating leads
        var time_to_wait = start_plus_6_hours - now;
        console.log(
          now +
            ". Working hours are ongoing. Waiting " +
            wait_time / 1000 +
            " Hours before updating leads... "
        );
        setTimeout(function () {
          // update the leads
          console.log(now + ". Updating leads... ");
          // wait for another 6 hours before updating leads again
          setTimeout(function () {
            console.log(now + ". Waiting for 6 hours within working hours... ");
          }, wait_time);
        }, time_to_wait);
      }
    }
  }
}

wait_for_working_hours("10:00", "19:00");