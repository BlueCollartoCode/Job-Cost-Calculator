Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
# =====================================
# JOB COST CALCULATOR
# Built by: Justin Cope
# Version: 1.0
# =====================================

# --- SHOP SETUP ---
# Collect basic information about the shop
from datetime import date  # imports the date tool so we can show todays date
shop_name = input("Enter your shop name: ")
owner_name = input("Enter owner's name: ")

# --- SERVICE BLOCKS ---
# Each service checks if it's needed first
# If yes, asks if charging hourly or flat rate
# Either way, ends with a single cost variable for the math later

# DESIGN
design_needed = input("Does this job require design work? (yes/no): ")
if design_needed.lower() == "yes":
    design_type = input("Charge by hourly or flat rate? (hourly/flat): ")
    if design_type.lower() == "hourly":
        design_rate = float(input("Enter design hourly rate: $"))
        time_unit = input("Enter time in hours or minutes? (hours/minutes): ")
        if time_unit.lower() == "minutes":
            design_hours = float(input("Enter design time in minutes: ")) / 60
        else:
            design_hours = float(input("Enter design time in hours: "))
        design_cost = design_rate * design_hours  # hourly rate x hours = cost
    else:
        # flat rate goes straight to cost
        design_cost = float(input("Enter flat rate for design: $"))
else:
    design_cost = 0  # not needed so cost is zero, wont affect math later

# LASER CUTTING
laser_cutting_needed = input("Does this job require laser cutting? (yes/no): ")
if laser_cutting_needed.lower() == "yes":
    laser_cutting_type = input(
        "Charge by hourly or flat rate? (hourly/flat): ")
    if laser_cutting_type.lower() == "hourly":
        laser_cutting_rate = float(input("Enter laser cutting hourly rate: $"))
        time_unit = input("Enter time in hours or minutes? (hours/minutes): ")
        if time_unit.lower() == "minutes":
            laser_cutting_hours = float(
                input("Enter laser cutting time in minutes: ")) / 60
        else:
            laser_cutting_hours = float(
                input("Enter laser cutting time in hours: "))
        laser_cutting_cost = laser_cutting_rate * \
            laser_cutting_hours  # hourly rate x hours = cost
    else:
        # flat rate goes straight to cost
        laser_cutting_cost = float(
            input("Enter flat rate for laser cutting: $"))
else:
    laser_cutting_cost = 0  # not needed so cost is zero, wont affect math later

# WELDING
welding_needed = input("Does this job require welding? (yes/no): ")
if welding_needed.lower() == "yes":
    welding_needed_type = input(
        "Charge by hourly or flat rate? (hourly/flat): ")
    if welding_needed_type.lower() == "hourly":
        welding_rate = float(input("Enter welding hourly rate: $"))
        time_unit = input("Enter time in hours or minutes? (hours/minutes): ")
        if time_unit.lower() == "minutes":
            welding_hours = float(
                input("Enter welding time in minutes: ")) / 60
        else:
            welding_hours = float(input("Enter welding time in hours: "))
        welding_cost = welding_rate * welding_hours  # hourly rate x hours = cost
    else:
        # flat rate goes straight to cost
        welding_cost = float(input("Enter flat rate for welding: $"))
else:
    welding_cost = 0  # not needed so cost is zero, wont affect math later

# --- JOB COSTS ---
# Collect all remaining costs for this specific job
customer_name = input("Enter customer name: ")

materials_cost = float(input("Enter materials cost: $"))  # supplier quote
# nitrogen, gases, etc
consumables_cost = float(input("Enter consumables cost: $"))
fixed_costs = float(input("Enter fixed costs: $"))  # rent, utilities, etc
setup_fee = float(input("Enter setup fee: $"))  # machine prep time

# QUOTE FEE - some jobs charge for the quote itself
quote_fee = input("Are you charging for this quote? (yes/no): ")
if quote_fee.lower() == "yes":
    quote_cost = float(input("Enter quote fee: $"))
else:
    quote_cost = 0  # free quote

# RUSH JOB - adds an upcharge percentage on top of everything
rush_job = input("Is this a rush job? (yes/no): ")
if rush_job.lower() == "yes":
    rush_percentage = float(
        input("Enter rush job upcharge percentage: "))  # example: 15 for 15%
else:
    rush_percentage = 0  # no rush upcharge

# REPEAT CUSTOMER - applies a discount percentage
repeat_customer = input("Is this a repeat customer? (yes/no): ")
if repeat_customer.lower() == "yes":
    discount_percentage = float(
        input("Enter discount percentage: "))  # example: 10 for 10%
else:
    discount_percentage = 0  # no discount

# TAX - business to business customers are often tax exempt
tax_exempt = input("Is this customer tax exempt? (yes/no): ")
if tax_exempt.lower() == "no":
    tax_rate = float(input("Enter tax rate percentage: "))  # example: 7 for 7%
else:
    tax_rate = 0  # tax exempt, no tax added

# PROFIT MARGIN - owner decides how much profit they want on this job
profit_margin = float(
    input("Enter your desired profit margin percentage: "))  # example: 25 for 25%

# --- MATH SECTION ---

# Step 1 - Add up all the base costs
subtotal = design_cost + laser_cutting_cost + welding_cost + quote_cost + \
    materials_cost + consumables_cost + fixed_costs + setup_fee

# Step 2 - Apply repeat customer discount first
# how much the discount is in dollars
discount_amount = subtotal * (discount_percentage / 100)
subtotal_after_discount = subtotal - discount_amount  # subtract it

# Step 3 - Apply rush job upcharge
# how much the rush upcharge is in dollars
rush_amount = subtotal_after_discount * (rush_percentage / 100)
subtotal_after_rush = subtotal_after_discount + rush_amount  # add it

# Step 4 - Apply profit margin
profit_amount = subtotal_after_rush * \
    (profit_margin / 100)  # how much profit in dollars
subtotal_after_profit = subtotal_after_rush + profit_amount  # add it

# Step 5 - Apply tax if not exempt
tax_amount = subtotal_after_profit * \
    (tax_rate / 100)  # how much tax in dollars
final_total = subtotal_after_profit + tax_amount  # this is the final quote

# --- QUOTE OUTPUT ---
# Prints a clean professional quote to the screen

today = date.today().strftime("%m/%d/%Y")  # formats date as 03/04/2026

print("=====================================")
print(f"           {shop_name}")
print(f"           JOB COST QUOTE")
print("=====================================")
print(f"Date:         {today}")
print(f"Owner:        {owner_name}")
print(f"Customer:     {customer_name}")
print(f"Tax Exempt:   {tax_exempt.upper()}")
print("-------------------------------------")
print("SERVICES")
... 
... # Only prints a service line if it was actually used
... if design_cost > 0:
...     print(f"  Design                    ${design_cost:.2f}")
... if laser_cutting_cost > 0:
...     print(f"  Laser Cutting             ${laser_cutting_cost:.2f}")
... if welding_cost > 0:
...     print(f"  Welding                   ${welding_cost:.2f}")
... if setup_fee > 0:
...     print(f"  Setup Fee                 ${setup_fee:.2f}")
... 
... print("-------------------------------------")
... print("COSTS")
... print(f"  Materials                 ${materials_cost:.2f}")
... print(f"  Consumables               ${consumables_cost:.2f}")
... print(f"  Fixed Costs               ${fixed_costs:.2f}")
... 
... if quote_cost > 0:
...     print(f"  Quote Fee                 ${quote_cost:.2f}")
... 
... print("-------------------------------------")
... print(f"Subtotal                    ${subtotal:.2f}")
... 
... if discount_amount > 0:
...     print(f"Repeat Customer Discount   -${discount_amount:.2f}")
... if rush_amount > 0:
...     print(f"Rush Job Upcharge          +${rush_amount:.2f}")
... 
... print(f"Profit ({profit_margin}%)              ${profit_amount:.2f}")
... 
... if tax_amount > 0:
...     print(f"Tax ({tax_rate}%)                  ${tax_amount:.2f}")
... 
... print("=====================================")
... print(f"TOTAL QUOTE                 ${final_total:.2f}")
... print("=====================================")
... print(f"Quote valid for 5-7 days")
... print(f"Thank you for your business, {customer_name}!")
... print("=====================================")
