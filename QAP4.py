import datetime

# Default values
next_policy_number = 1944
basic_premium = 869.00
discount = 0.25
cost_extra_liability = 130.00
cost_glass_coverage = 86.00
cost_loaner_car = 58.00
hst_rate = 0.15
processing_fee = 39.99

# Validate province abbreviation
def validate_province(province):
    provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
    return province.upper() in provinces

# Validate payment method
def validate_payment_method(method):
    methods = ["FULL", "MONTHLY", "DOWN PAY"]
    return method.upper() in methods

# Get customer input
def get_customer_input():
    first_name = input("Enter customer's first name: ").title()
    last_name = input("Enter customer's last name: ").title()
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ").title()
    province = input("Enter customer's province (2-letter abbreviation): ").upper()
    while not validate_province(province):
        province = input("Invalid province abbreviation. Please enter a valid 2-letter abbreviation: ").upper()
    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")
    num_cars = int(input("Enter number of cars being insured: "))
    extra_liability = input("Do you want extra liability coverage? (Y/N): ").upper()
    glass_coverage = input("Do you want glass coverage? (Y/N): ").upper()
    loaner_car = input("Do you want loaner car coverage? (Y/N): ").upper()
    payment_method = input("Enter payment method (Full, Monthly, or Down Pay): ").upper()
    while not validate_payment_method(payment_method):
        payment_method = input("Invalid payment method. Please enter Full, Monthly, or Down Pay: ").upper()
    down_payment = 0
    if payment_method == "DOWN PAY":
        down_payment = float(input("Enter the amount of the down payment: "))
    claims = []
    while True:
        claim_number = input("Enter claim number (or enter 'q' to finish): ")
        if claim_number.lower() == 'q':
            break
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        claim_amount = float(input("Enter claim amount: "))
        claims.append((claim_number, claim_date, claim_amount))
    return (first_name, last_name, address, city, province, postal_code, phone_number, num_cars,
            extra_liability, glass_coverage, loaner_car, payment_method, down_payment, claims)

# Calculate total premium
def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    basic_premium = 869.00
    discount = 0.25
    total_premium = basic_premium + (num_cars - 1) * basic_premium * discount
    if extra_liability == 'Y':
        total_premium += 130.00 * num_cars
    if glass_coverage == 'Y':
        total_premium += 86.00 * num_cars
    if loaner_car == 'Y':
        total_premium += 58.00 * num_cars
    return total_premium

# Calculate total cost
def calculate_total_cost(total_premium, hst_rate, processing_fee):
    hst = total_premium * hst_rate
    total_cost = total_premium + hst + processing_fee
    return total_cost

# Calculate monthly payment
def calculate_monthly_payment(total_cost, down_payment=None):
    if down_payment:
        remaining_cost = total_cost - down_payment
        monthly_payment = (remaining_cost + 39.99) / 8
    else:
        monthly_payment = (total_cost + 39.99) / 8
    return monthly_payment

# Display receipt
def display_receipt(customer_data, total_premium, total_cost, monthly_payment):
    invoice_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print("\nReceipt:")
    print(f"Invoice Date: {invoice_date}")
    print(f"Policy Number: {next_policy_number}")
    print("Customer Information:")
    for key, value in customer_data.items():
        print(f"{key}: {value}")
    print("\nInsurance Premium Information:")
    print(f"Total Insurance Premium (Pre-tax): ${total_premium:.2f}")
    print(f"HST (15%): ${total_cost - total_premium:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print("\nPrevious Claims:")
    print(" Claim #   Claim Date   Amount")
    print("---------------------------------")
    for claim in customer_data["claims"]:
        print(f" {claim[0]}   {claim[1]}   ${claim[2]:,.2f}")

while True:
    customer_data = dict(zip(["first_name", "last_name", "address", "city", "province", "postal_code",
                              "phone_number", "num_cars", "extra_liability", "glass_coverage", "loaner_car",
                              "payment_method", "down_payment", "claims"], get_customer_input()))
    total_premium = calculate_premium(customer_data["num_cars"], customer_data["extra_liability"],
                                      customer_data["glass_coverage"], customer_data["loaner_car"])
    total_cost = calculate_total_cost(total_premium, hst_rate, processing_fee)
    monthly_payment = calculate_monthly_payment(total_cost, customer_data["down_payment"])
    display_receipt(customer_data, total_premium, total_cost, monthly_payment)
    print("\nPolicy data has been saved.")
    next_policy_number += 1
    if input("Enter 'q' to quit, or any other key to enter another customer: ").lower() == 'q':
        break