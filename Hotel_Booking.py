# Ronit Bhandari
# Student ID: s4109169
# Highest part attempted: Full implementation of the booking management system.

# Design Structure  : Following is the Python program that has been designed and developed to give a menu-based application for managing bookings, apartments, and extra items. It was designed using dictionaries for efficient data management and adopting a modular approach where every task was assigned to a different function. Issues of concern in design included rigorous input validation along with appropriate user response. In the case of implementation, testing was done incrementally in order to spot issues and debug appropriately. It was maintainable because of the modular structure it had; adding a few features, such as persistent storage for the data, would have given it a lot more practical applications. In general, it was very useful and instructive, as it showed ways to apply Python concepts to real-life problems.
"""
References:
[1] "Errors and Exceptions," Python.org, . Available: https://docs.python.org/3/tutorial/errors.html.
"""


from datetime import datetime

# Initialize guests with their reward points and booking history
# Using a dictionary for fast lookups, unique keys, and clear organization of related data.
guests = {
    "Alyssa": {"reward_points": 20, "booking_history": []},
    "Luigi": {"reward_points": 32, "booking_history": []}
}

# Using a dictionary to map apartment IDs to their rate and capacity for efficient data retrieval.
apartments = {
    "U12swan": {"rate": 95.0, "capacity": 2},
    "U209duck": {"rate": 106.7, "capacity": 4},
    "U49goose": {"rate": 145.2, "capacity": 3}
}

# Using a dictionary to map supplementary_items to their rate  for efficient data retrieval.
supplementary_items = {
    "car_park": 25.0,
    "breakfast": 21.0,
    "toothpaste": 5.0,
    "extra_bed": 50.0
}

# This Function validates the date format (d/m/yyyy)
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        # Reference for error handling: [1]
        return False

#This function allow users to enter their name
def get_guest_name():
    return input("Enter the guest's name: ").strip()

#this function ask users to enter the number of guest
def get_number_of_guests():
    while True:
        try:
            return int(input("Enter the number of guests: "))
        except ValueError:
            # Reference for error handling: [1]
            print("Invalid input. Please enter an integer.")

# allow  user to enter the apartment ID.
def get_apartment_id():
    return input("Enter the apartment ID (e.g., U12swan): ").strip()

# Repeatedly prompt the user for a valid date until the input is correct.
def get_date(prompt):
    while True:
        date_str = input(f"Enter the {prompt} date (d/m/yyyy): ").strip()
        if validate_date(date_str):
            # Reference for error handling: [1]
            return date_str
        print("Invalid date format. Please use d/m/yyyy.")


 # This Function handles the addition of supplementary items to a booking.
 # Collects user input for each item and its quantity  and stores them in a list.
def get_supplementary_items():
    supplementary_items_list = []
    # Continuously prompt user to add supplementary items until they choose 'n' (no).
    while True:
        add_item = input("Do you want to order a supplementary item? (y/n): ").strip().lower()
        if add_item == 'n':
            break
        if add_item == 'y':
            item_id = input("Enter the supplementary item ID: ").strip()
            if item_id in supplementary_items:
                price = supplementary_items[item_id]
                while True:
                    try:
                        quantity = int(input(f"Enter the quantity for {item_id}: ").strip())
                        if quantity < 1:
                            print("Quantity must be at least 1.")
                        else:
                            supplementary_items_list.append((item_id, quantity, price))
                            print(f"Supplementary item added: {item_id}, Quantity: {quantity}, Price: ${price:.2f}")
                            break
                    except ValueError:
                        # Reference for error handling: [1]
                        print("Invalid input. Please enter a valid integer for the quantity.")
            else:
                print("Invalid supplementary item ID. Please try again.")
    return supplementary_items_list


 # This Function  display a formatted booking receipt.
 # Prints out all the details of the booking and any supplementary items ordered.
def display_receipt(guest_name, number_of_guests, apartment_id, apartment_rate, checkin_date, checkout_date, length_of_stay, booking_date, total_cost, reward_points, supplementary_items_list):
    print("=========================================================")
    print("Pythonia Serviced Apartments - Booking Receipt")
    print("=========================================================")
    print(f"Guest Name: {guest_name}")
    print(f"Number of guests: {number_of_guests}")
    print(f"Apartment ID: {apartment_id}")
    print(f"Apartment rate: ${apartment_rate:.2f} (AUD)")
    print(f"Check-in date: {checkin_date}")
    print(f"Check-out date: {checkout_date}")
    print(f"Length of stay: {length_of_stay} (nights)")
    print(f"Booking date: {booking_date}")
    if supplementary_items_list:
        print("-------------------------------------------------------------------------------")
        print("Supplementary items")
        sub_total = 0
        for item_id, quantity, price in supplementary_items_list:
            cost = quantity * price
            print(f"Item ID: {item_id}")
            print(f"Quantity: {quantity}")
            print(f"Price: ${price:.2f}")
            print(f"Cost: ${cost:.2f}")
            sub_total += cost
        print(f"Sub-total: ${sub_total:.2f}")
        print("--------------------------------------------------------------------------------")
    print(f"Total cost: ${total_cost:.2f} (AUD)")
    print(f"Earned rewards: {reward_points} (points)")
    print("Thank you for your booking! We hope you will have an enjoyable stay.")
    print("=========================================================")

 # This Function handle the entire booking process.
# Collects user input for guest details, apartment choice, supplementary items, and calculates total cost and rewards.
def make_booking():
    guest_name = get_guest_name()
    number_of_guests = get_number_of_guests()
    apartment_id = get_apartment_id()

    if apartment_id not in apartments:
        print("Invalid apartment ID. Please try again.")
        return

    apartment_rate = apartments[apartment_id]["rate"]
    apartment_capacity = apartments[apartment_id]["capacity"]

    checkin_date = get_date("check-in")
    checkout_date = get_date("check-out")

    while True:
        try:
            length_of_stay = int(input("Enter the length of stay (in nights): "))
            if length_of_stay < 1:
                print("Length of stay must be at least 1 night.")
            else:
                break
        except ValueError:
            # Reference for error handling: [1]
            print("Invalid input. Please enter a valid integer for the length of stay.")

    booking_date = get_date("booking")

    if guest_name not in guests:
        guests[guest_name] = {
            "reward_points": 0,
            "booking_history": []
        }

    if number_of_guests > apartment_capacity:
        print(f"Warning: This apartment can accommodate up to {apartment_capacity} guests.")
        extra_beds_needed = (number_of_guests - apartment_capacity + 1) // 2
        if extra_beds_needed > 0:
            if extra_beds_needed > 2:
                print("You can only order up to 2 extra beds.")
                extra_beds_needed = 2
            while extra_beds_needed > 0:
                extra_beds = input(f"Do you want to order {extra_beds_needed} extra bed(s)? (y/n): ").strip().lower()
                if extra_beds == 'y':
                    cost_per_bed = supplementary_items["extra_bed"]
                    cost = cost_per_bed * extra_beds_needed
                    confirm = input(f"Extra bed(s) cost ${cost:.2f}. Confirm order? (y/n): ").strip().lower()
                    if confirm == 'y':
                        supplementary_items_list = [("extra_bed", extra_beds_needed, cost_per_bed)]
                        print(f"Extra bed(s) added to your order.")
                        break
                    else:
                        print("Item cancelled.")
                        extra_beds_needed = 0
                        supplementary_items_list = []
                else:
                    print("Extra bed(s) not ordered.")
                    break
            if extra_beds_needed > 0:
                print("Booking cannot proceed. Returning to the main menu.")
                return
        else:
            supplementary_items_list = []
    else:
        supplementary_items_list = []

    supplementary_items_list.extend(get_supplementary_items())

    supplementary_total = sum(quantity * price for item_id, quantity, price in supplementary_items_list)
    total_cost = (apartment_rate * length_of_stay) + supplementary_total

    reward_points = round(total_cost)

    if guest_name in guests:
        current_points = guests[guest_name]["reward_points"]
        if current_points >= 100:
            deduction = (current_points // 100) * 10
            total_cost -= deduction
            guests[guest_name]["reward_points"] -= (current_points // 100) * 100
            print(f"Reward points deduction: ${deduction:.2f}. New total cost: ${total_cost:.2f}.")
        guests[guest_name]["reward_points"] += reward_points

    guests[guest_name]["booking_history"].append({
        "apartment_id": apartment_id,
        "supplementary_items": supplementary_items_list,
        "total_cost": total_cost,
        "reward_points": reward_points
    })

    display_receipt(guest_name, number_of_guests, apartment_id, apartment_rate, checkin_date, checkout_date, length_of_stay, booking_date, total_cost, reward_points, supplementary_items_list)

    # Return to the main menu after the booking process
    print("Booking complete. Returning to the main menu.")
    return

# Prompts for and updates apartment details in the `apartments` dictionary with validation.
def add_update_apartment():
    while True:
        user_input = input("Enter apartment information (id rate capacity) or 'cancel' to return: ").strip()
        if user_input.lower() == 'cancel':
            return
        try:
            apartment_id, rate, capacity = user_input.split()
            rate = float(rate)
            capacity = int(capacity)
            if not apartment_id.startswith('U') or not apartment_id[1:].isdigit() or not apartment_id[2:].isalpha():
                print("Invalid apartment ID format.")
                continue
            apartments[apartment_id] = {"rate": rate, "capacity": capacity}
            print(f"Apartment '{apartment_id}' updated with rate ${rate:.2f} and capacity {capacity}.")
            return
        except ValueError:
            print("Invalid input format. Please enter: id rate capacity")

# Prompts for and updates supplementary item details in the `supplementary_items` dictionary with validation
def add_update_supplementary_items():
    while True:
        user_input = input("Enter supplementary items (item_id price, ... ) or 'cancel' to return: ").strip()
        if user_input.lower() == 'cancel':
            return
        items = user_input.split(',')
        valid_items = []
        valid = True
        for item in items:
            parts = item.strip().split()
            if len(parts) != 2:
                print("Invalid format. Each item should be in the format 'item_id price'.")
                valid = False
                break
            item_id, price_str = parts
            try:
                price = float(price_str)
                if price <= 0:
                    print(f"Invalid price {price_str}. Prices must be positive numbers.")
                    valid = False
                    break
                valid_items.append((item_id, price))
            except ValueError:
                print(f"Invalid price {price_str}. Prices must be numbers.")
                valid = False
                break
        if valid:
            for item_id, price in valid_items:
                supplementary_items[item_id] = price
            print("Supplementary items updated successfully.")
            return

def display_guests():
    if not guests:
        print("No guests to display.")
        return
    for guest_name, data in guests.items():
        print(f"Guest Name: {guest_name}, Reward Points: {data['reward_points']}")

def display_apartments():
    if not apartments:
        print("No apartments to display.")
        return
    for apartment_id, details in apartments.items():
        print(f"Apartment ID: {apartment_id}, Rate: ${details['rate']:.2f} (AUD), Capacity: {details['capacity']}")

def display_supplementary_items():
    if not supplementary_items:
        print("No supplementary items to display.")
        return
    for item_id, price in supplementary_items.items():
        print(f"Item ID: {item_id}, Price: ${price:.2f}")

def display_guest_booking_history():
    guest_name = input("Enter the guest's name: ").strip()
    if guest_name not in guests:
        print("Guest not found.")
        return
    print(f"This is the booking and order history for {guest_name}.")
    for i, order in enumerate(guests[guest_name]["booking_history"], 1):
        apartment_id = order["apartment_id"]
        items = order["supplementary_items"]
        total_cost = order["total_cost"]
        reward_points = order["reward_points"]
        print(f"Order {i}")
        print(f"{items}")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Earned Rewards: {reward_points}")


#   Displays the main menu of the program and prompts the user to select an option. Executes the corresponding 
#       function based on the user's choice. The menu includes options for making bookings, updating information, 
#     displaying data, and exiting the program.
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Make a booking")
        print("2. Add/update information of an apartment unit")
        print("3. Add/update information of supplementary items")
        print("4. Display existing guests")
        print("5. Display existing apartment units")
        print("6. Display existing supplementary items")
        print("7. Display a guest booking and order history")
        print("8. Exit the program")

        option = input("Please select an option (1-8): ").strip()
        if option == '1':
            make_booking()
        elif option == '2':
            add_update_apartment()
        elif option == '3':
            add_update_supplementary_items()
        elif option == '4':
            display_guests()
        elif option == '5':
            display_apartments()
        elif option == '6':
            display_supplementary_items()
        elif option == '7':
            display_guest_booking_history()
        elif option == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 8.")

# Run the main menu loop
if __name__ == "__main__":
    main_menu()

