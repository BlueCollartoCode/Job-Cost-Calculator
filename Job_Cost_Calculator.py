# =====================================
# JOB COST CALCULATOR
# Built by: BlueCollartoCode
# Version: 1.0
# Description: Generates professional job quotes
# for metal fabrication shops
# =====================================

from datetime import date  # imports the date tool so we can show todays date

# =====================================
# HELPER FUNCTION
# Asking for a number over and over until they give us one
# =====================================

def get_float(prompt):
    # keeps asking until the user types a valid number
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Please enter a number only. Example: 150.00")

def get_yes_no(prompt):
    # keeps asking until the user types yes or no
    while True:
        answer = input(prompt).lower()
        if answer in ["yes", "no"]:
            return answer
        print("  Please type yes or no only.")

def get_choice(prompt, choices):
    # keeps asking until the user picks a valid option
    while True:
        answer = input(prompt).lower()
        if answer in choices:
            return answer
        print(f"  Please type one of these options: {' or '.join(choices)}")

# =====================================
# SHOP SETUP
# Collect basic information about the shop
# =====================================

print("\n=====================================")
print("       JOB COST CALCULATOR")
print("         SHOP SETUP")
print("=====================================\n")

shop_name = input("Enter your shop name: ")
owner_name = input("Enter owner's name: ")

# =====================================
# SERVICE BLOCKS
# Each service checks if it's needed first
# If yes, asks if charging hourly or flat rate
# Either way ends with a single cost variable for the math later
# =====================================

print("\n--- SERVICES ---\n")

# DESIGN
design_needed = get_yes_no("Does this job require design work? (yes/no): ")
if design_needed == "yes":
    design_type = get_choice("Charge by hourly or flat rate? (hourly/flat): ", ["hourly", "flat"])
    if design_type == "hourly":
        design_rate = get_float("Enter design hourly rate: $")
        time_unit = get_choice("Enter time in hours or minutes? (hours/minutes): ", ["hours", "minutes"])
        if time_unit == "minutes":
            design_hours = get_float("Enter design time in minutes: ") / 60  # converts to hours
        else:
            design_hours = get_float("Enter design time in hours: ")
        design_cost = design_rate * design_hours  # hourly rate x hours = cost
    else:
        design_cost = get_float("Enter flat rate for design: $")  # flat rate goes straight to cost
else:
    design_cost = 0  # not needed so cost is zero, wont affect math later

# LASER CUTTING
laser_cutting_needed = get_yes_no("Does this job require laser cutting? (yes/no): ")
if laser_cutting_needed == "yes":
    laser_cutting_type = get_choice("Charge by hourly or flat rate? (hourly/flat): ", ["hourly", "flat"])
    if laser_cutting_type == "hourly":
        laser_cutting_rate = get_float("Enter laser cutting hourly rate: $")
        time_unit = get_choice("Enter time in hours or minutes? (hours/minutes): ", ["hours", "minutes"])
        if time_unit == "minutes":
            laser_cutting_hours = get_float("Enter laser cutting time in minutes: ") / 60  # converts to hours
        else:
            laser_cutting_hours = get_float("Enter laser cutting time in hours: ")
        laser_cutting_cost = laser_cutting_rate * laser_cutting_hours  # hourly rate x hours = cost
    else:
        laser_cutting_cost = get_float("Enter flat rate for laser cutting: $")  # flat rate goes straight to cost
else:
    laser_cutting_cost = 0  # not needed so cost is zero, wont affect math later

# WELDING
welding_needed = get_yes_no("Does this job require welding? (yes/no): ")
if welding_needed == "yes":
    welding_type = get_choice("Charge by hourly or flat rate? (hourly/flat): ", ["hourly", "flat"])
    if welding_type == "hourly":
        welding_rate = get_float("Enter welding hourly rate: $")
        time_unit = get_choice("Enter time in hours or minutes? (hours/minutes): ", ["hours", "minutes"])
        if time_unit == "minutes":
            welding_hours = get_float("Enter welding time in minutes: ") / 60  # converts to hours
        else:
            welding_hours = get_float("Enter welding time in hours: ")
        welding_cost = welding_rate * welding_hours  # hourly rate x hours = cost
    else:
        welding_cost = get_float("Enter flat rate for welding: $")  # flat rate goes straight to cost
else:
    welding_cost = 0  # not needed so cost is zero, wont affect math later

# =====================================
# JOB COSTS
# Collect all remaining costs for this specific job
# =====================================

print("\n--- JOB DETAILS ---\n")

customer_name = input("Enter customer name: ")

materials_cost = get_float("Enter materials cost: $")       # supplier quote
consumables_cost = get_float("Enter consumables cost: $")   # nitrogen, gases, etc
fixed_costs = get_float("Enter fixed costs: $")             # rent, utilities, etc
setup_fee = get_float("Enter setup fee: $")                 # machine prep time

# QUOTE FEE - some jobs charge for the quote itself
quote_fee = get_yes_no("Are you charging for this quote? (yes/no): ")
if quote_fee == "yes":
    quote_cost = get_float("Enter quote fee: $")
else:
    quote_cost = 0  # free quote

# RUSH JOB - adds an upcharge percentage on top of everything
rush_job = get_yes_no("Is this a rush job? (yes/no): ")
if rush_job == "yes":
    rush_percentage = get_float("Enter rush job upcharge percentage: ")  # example: 15 for 15%
else:
    rush_percentage = 0  # no rush upcharge

# REPEAT CUSTOMER - applies a discount percentage
repeat_customer = get_yes_no("Is this a repeat customer? (yes/no): ")
if repeat_customer == "yes":
    discount_percentage = get_float("Enter discount percentage: ")  # example: 10 for 10%
else:
    discount_percentage = 0  # no discount

# TAX - business to business customers are often tax exempt
tax_exempt = get_yes_no("Is this customer tax exempt? (yes/no): ")
if tax_exempt == "no":
    tax_rate = get_float("Enter tax rate percentage: ")  # example: 7 for 7%
else:
    tax_rate = 0  # tax exempt, no tax added

# PROFIT MARGIN - owner decides how much profit they want on this job
profit_margin = get_float("Enter your desired profit margin percentage: ")  # example: 25 for 25%

# =====================================
# MATH SECTION
# =====================================

# Step 1 - Add up all the base costs
subtotal = design_cost + laser_cutting_cost + welding_cost + quote_cost + materials_cost + consumables_cost + fixed_costs + setup_fee

# Step 2 - Apply repeat customer discount first
discount_amount = subtotal * (discount_percentage / 100)    # how much the discount is in dollars
subtotal_after_discount = subtotal - discount_amount        # subtract it

# Step 3 - Apply rush job upcharge
rush_amount = subtotal_after_discount * (rush_percentage / 100)  # how much the rush upcharge is in dollars
subtotal_after_rush = subtotal_after_discount + rush_amount      # add it

# Step 4 - Apply profit margin
profit_amount = subtotal_after_rush * (profit_margin / 100)  # how much profit in dollars
subtotal_after_profit = subtotal_after_rush + profit_amount  # add it

# Step 5 - Apply tax if not exempt
tax_amount = subtotal_after_profit * (tax_rate / 100)   # how much tax in dollars
final_total = subtotal_after_profit + tax_amount        # this is the final quote

# =====================================
# QUOTE OUTPUT
# Prints a clean professional quote to the screen
# =====================================

today = date.today().strftime("%m/%d/%Y")  # formats date as 03/04/2026

print("\n=====================================")
print(f"        {shop_name}")
print("         JOB COST QUOTE")
print("=====================================")
print(f"Date:         {today}")
print(f"Owner:        {owner_name}")
print(f"Customer:     {customer_name}")
print(f"Tax Exempt:   {tax_exempt.upper()}")
print("-------------------------------------")
print("SERVICES")

# Only prints a service line if it was actually used
if design_cost > 0:
    print(f"  Design                    ${design_cost:.2f}")
if laser_cutting_cost > 0:
    print(f"  Laser Cutting             ${laser_cutting_cost:.2f}")
if welding_cost > 0:
    print(f"  Welding                   ${welding_cost:.2f}")
if setup_fee > 0:
    print(f"  Setup Fee                 ${setup_fee:.2f}")

print("-------------------------------------")
print("COSTS")
print(f"  Materials                 ${materials_cost:.2f}")
print(f"  Consumables               ${consumables_cost:.2f}")
print(f"  Fixed Costs               ${fixed_costs:.2f}")

if quote_cost > 0:
    print(f"  Quote Fee                 ${quote_cost:.2f}")

print("-------------------------------------")
print(f"Subtotal                    ${subtotal:.2f}")

if discount_amount > 0:
    print(f"Repeat Customer Discount   -${discount_amount:.2f}")
if rush_amount > 0:
    print(f"Rush Job Upcharge          +${rush_amount:.2f}")

print(f"Profit ({profit_margin}%)              ${profit_amount:.2f}")

if tax_amount > 0:
    print(f"Tax ({tax_rate}%)                  ${tax_amount:.2f}")

print("=====================================")
print(f"TOTAL QUOTE                 ${final_total:.2f}")
print("=====================================")
print(f"Quote valid for 5-7 days")
print(f"Thank you for your business, {customer_name}!")
print("=====================================")
