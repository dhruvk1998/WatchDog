// async function wait_for_working_hours(start_time, end_time) {
//     while (true) {
//       var now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
//       var start = new Date().setHours(parseInt(start_time.split(':')[0]), parseInt(start_time.split(':')[1]), 0, 0);
//       var end = new Date().setHours(parseInt(end_time.split(':')[0]), parseInt(end_time.split(':')[1]), 0, 0);
//       if (start <= new Date() && new Date() <= end) {
//         return;
//       }
//       else {
//         async function update_leads() {
//           var i = 0;
//           while (i < 10) {
//             console.log("Waiting for working hours...");
//             await new Promise(r => setTimeout(r, 60000));
//             i += 1;
//           }
//           // calculate the time to wait before updating leads
//           var start_plus_6_hours = new Date().setHours(parseInt(start_time.split(':')[0]) + 6, parseInt(start_time.split(':')[1]), 0, 0);
//           var time_to_wait = (start_plus_6_hours - new Date()) / 1000;
//           // wait for the required time
//           console.log("Waiting for 6 hours within working hours...");
//           await new Promise(r => setTimeout(r, time_to_wait * 1000));
//           // update the leads
//           console.log("Updating leads after 6 hours within working hours...");
//         }
//         await update_leads();
//       }
//     }
//   }
  
//   wait_for_working_hours("10:00", "19:00");



function wait_for_working_hours(start_time, end_time) {
    while (true) {
        let now = new Date().toLocaleTimeString();
        let start = new Date("1970-01-01T" + start_time + "Z").toLocaleTimeString();
        let end = new Date("1970-01-01T" + end_time + "Z").toLocaleTimeString();
        
        if (now >= start && now <= end) {
            update_leads();
        }
        else {
            console.log("Waiting for working hours...");
            sleep(60 * 1000); // wait for 1 minute
        }
    }
}

function update_leads() {
    let i = 0;
    while (i < 10) {
        console.log("Waiting for working hours...");
        sleep(60 * 1000); // wait for 1 minute
        i++;
    }
    let start = new Date("1970-01-01T" + start_time + "Z").toLocaleTimeString();
    let start_plus_6_hours = new Date("1970-01-01T" + start + "Z");
    start_plus_6_hours.setHours(start_plus_6_hours.getHours() + 6);
    let time_to_wait = (start_plus_6_hours - new Date()) / 1000; // in seconds
    console.log("Waiting for 6 hours within working hours...");
    sleep(time_to_wait * 1000); // wait for the required time
    console.log("Updating leads after 6 hours within working hours...");
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

wait_for_working_hours("10:00", "19:00");
