// Initialize LeadSquared SDK
var ls_sdk = new LeadSquaredSDK({
    accessKey: "u$re4a5d95db6aed99c74ae8877bba01824",
    secretKey: "8a22e2fa3e4f3500dee9585c6731299491bfcbe0",
    apiBaseUrl: "https://api-in21.leadsquared.com/v2/"
});

// Define your custom schema name
var schemaName = "my_custom_schema";

// Define the filter to retrieve data from the schema
var filter = {
    "Column": "Name",
    "Operator": "EQUALS",
    "Value": "John Doe"
};

// Retrieve data from the schema using the filter
ls_sdk.data.retrieve(schemaName, filter, function(data) {
    // Parse the retrieved data as JSON
    var json = JSON.parse(data);

    // Create a 3-D array to store the retrieved data
    var dataArray = [];

    // Loop through the retrieved data and add each item as a new row to the array
    for (var i = 0; i < json.length; i++) {
        var item = json[i];

        // Create a new customer object using the retrieved data
        var customer = new Customer(item["Name"], item["Email"], item["Phone"]);

        // Add the customer data as a new row to the 3-D array
        var row = [customer.name, customer.email, customer.phone];
        dataArray.push(row);
    }

    // Use the 3-D array for further processing
    console.log(dataArray);
}, function(error) {
    // Handle any errors that occur during data retrieval
    console.log(error);
});
