class Customer {
    constructor(name, email, phone) {
      this.name = name;
      this.email = email;
      this.phone = phone;
    }
  }
//   document.getID
  let salesActivity = [];
  
  // Add a new customer with field values entered by the user
  const customer1 = new Customer(prompt(name), prompt(email), prompt(phone));
  // Add customer1 to the salesActivity array as the first element of the first dimension
  salesActivity.push([customer1]);
  
  // Add a second customer with field values entered by the user
  const customer2 = new Customer(prompt("Enter customer name:"), prompt("Enter customer email:"), prompt("Enter customer phone:"));
  // Add customer2 to the salesActivity array as the second element of the first dimension
  salesActivity.push([customer2]);
  
  // Add a third customer with field values entered by the user
  const customer3 = new Customer(prompt("Enter customer name:"), prompt("Enter customer email:"), prompt("Enter customer phone:"));
  // Add customer3 to the salesActivity array as the third element of the first dimension
  salesActivity.push([customer3]);
  
  // You can then access the sales activity data for the first customer like this:
  console.log(salesActivity[0][0].name);
  console.log(salesActivity[0][0].email);
  console.log(salesActivity[0][0].phone);
  
  // You can also access the sales activity data for the second and third customers like this:
  console.log(salesActivity[1][0].name);
  console.log(salesActivity[1][0].email);
  console.log(salesActivity[1][0].phone);
  
  console.log(salesActivity[2][0].name);
  console.log(salesActivity[2][0].email);
  console.log(salesActivity[2][0].phone);
  