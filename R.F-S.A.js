class Customer {
  constructor(name, email, phone) {
    this.name = name;
    this.email = email;
    this.phone = phone;
  }
}

// Get the schema names from leadsquared
const name_schema = "your_lead_name_schema_name";
const email_schema = "your_lead_email_schema_name";
const phone_schema = "your_lead_phone_schema_name";

const sales_activity = [];

// Add a new customer with field values from leadsquared
const customer1 = new Customer(
  lead.get_attribute_value(name_schema),
  lead.get_attribute_value(email_schema),
  lead.get_attribute_value(phone_schema)
);
// Add customer1 to the salesActivity array as the first element of the first dimension
sales_activity.push([customer1]);

// Add a second customer with field values from leadsquared
const customer2 = new Customer(
  lead.get_attribute_value(name_schema),
  lead.get_attribute_value(email_schema),
  lead.get_attribute_value(phone_schema)
);
// Add customer2 to the salesActivity array asthe second element of the first dimension
sales_activity[0].push(customer2);

// Add a third customer with field values from leadsquared
const customer3 = new Customer(
lead.get_attribute_value(name_schema),
lead.get_attribute_value(email_schema),
lead.get_attribute_value(phone_schema)
);
// Add customer3 to the salesActivity array as the first element of the second dimension
sales_activity.push([customer3]);

// Add a fourth customer with field values from leadsquared
const customer4 = new Customer(
lead.get_attribute_value(name_schema),
lead.get_attribute_value(email_schema),
lead.get_attribute_value(phone_schema)
);
// Add customer4 to the salesActivity array as the second element of the second dimension
sales_activity[1].push(customer4);

// Print the sales activity array to the console
console.log(sales_activity);