# import sys

# # Add a new customer with field values
# customer1 = {
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "phone": "+1-123-456-7890"
# }
# # Add customer1 to the salesActivity array as the first element of the first dimension
# salesActivity = [[customer1]]

# # Add a second customer with field values
# customer2 = {
#     "name": "Jane Smith",
#     "email": "jane.smith@example.com",
#     "phone": "+1-234-567-8901"
# }
# # Add customer2 to the salesActivity array as the second element of the first dimension
# salesActivity.append([customer2])

# # Add a third customer with field values
# customer3 = {
#     "name": "Bob Johnson",
#     "email": "bob.johnson@example.com",
#     "phone": "+1-345-678-9012"
# }
# # Add customer3 to the salesActivity array as the third element of the first dimension
# salesActivity.append([customer3])

# # You can then access the sales activity data for the first customer like this:
# print(salesActivity[0][0]["name"])  # Output: "John Doe"
# print(salesActivity[0][0]["email"])  # Output: "john.doe@example.com"
# print(salesActivity[0][0]["phone"])  # Output: "+1-123-456-7890"

# # You can also access the sales activity data for the second and third customers like this:
# print(salesActivity[1][0]["name"])  # Output: "Jane Smith"
# print(salesActivity[1][0]["email"])  # Output: "jane.smith@example.com"
# print(salesActivity[1][0]["phone"])  # Output: "+1-234-567-8901"

# print(salesActivity[2][0]["name"])  # Output: "Bob Johnson"
# print(salesActivity[2][0]["email"])  # Output: "bob.johnson@example.com"
# print(salesActivity[2][0]["phone"])  # Output: "+1-345-678-9012"


class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

sales_activity = []

# Add a new customer with field values entered by the user
customer1 = Customer(input("Enter customer name: "), input("Enter customer email: "), input("Enter customer phone: "))
# Add customer1 to the salesActivity array as the first element of the first dimension
sales_activity.append([customer1])

# Add a second customer with field values entered by the user
customer2 = Customer(input("Enter customer name: "), input("Enter customer email: "), input("Enter customer phone: "))
# Add customer2 to the salesActivity array as the second element of the first dimension
sales_activity.append([customer2])

# Add a third customer with field values entered by the user
customer3 = Customer(input("Enter customer name: "), input("Enter customer email: "), input("Enter customer phone: "))
# Add customer3 to the salesActivity array as the third element of the first dimension
sales_activity.append([customer3])

# You can then access the sales activity data for the first customer like this:
print(sales_activity[0][0].name)
print(sales_activity[0][0].email)
print(sales_activity[0][0].phone)

# You can also access the sales activity data for the second and third customers like this:
print(sales_activity[1][0].name)
print(sales_activity[1][0].email)
print(sales_activity[1][0].phone)

print(sales_activity[2][0].name)
print(sales_activity[2][0].email)
print(sales_activity[2][0].phone)
