# Student ID: 010629417
# Name: Rodrigo Reimann Baston

from truck import Truck
from data_loader import loadPackageData, loadDistanceData, loadAddressData
from hash_table import HashTable
from logistics import perform_delivery_round
import datetime


# Initialize hash table and load data
hash_table = HashTable(size=10)
loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/TSP-Routing/WGUPS-package copy.csv')

# Create an iterable package list
package_list = hash_table.get_all_packages()

# Load distance and address data from csv
distance_data = loadDistanceData('/Users/rodrigo/Documents/repos/TSP-Routing/WGUPS-distance-matrix.csv')
address_to_index = loadAddressData('/Users/rodrigo/Documents/repos/TSP-Routing/WGUPS-address.csv')

# Initialize trucks
trucks = [Truck(1), Truck(2)]

# Load first round
for pkg in package_list:
    if pkg.package_id in [13, 39, 14, 15, 16, 34, 19, 20, 21, 7, 29, 4, 40, 1, 30, 8]:
        trucks[0].add_package(pkg)

for pkg in package_list:
    if pkg.package_id in [22, 26, 24, 18, 11, 23, 12, 31, 17, 36, 37, 5, 38, 3, 10]:
        trucks[1].add_package(pkg)

# First delivers
perform_delivery_round(trucks, distance_data, address_to_index, hash_table)

# Load second rounds
for pkg in package_list:
    if pkg.package_id in [25, 32, 6]:
        trucks[0].add_package(pkg)

for pkg in package_list:
    if pkg.package_id in [28, 2, 33, 9, 27, 35]:
        trucks[1].add_package(pkg)  

# Second delivers
perform_delivery_round(trucks, distance_data, address_to_index, hash_table)
              
# After all deliveries are complete, print the delivery time for each package
print("\nDelivery Times for Each Package:")
for package in hash_table.get_all_packages():
    print(f"Package ID: {package.package_id}, Delivery Time: {package.delivery_time}")

# GUI
def get_delivery_status(package_id, hash_table):
    # Retrieve package status
    package = hash_table.lookup(package_id)
    if package:
        return (f"Package ID: {package.package_id}\n" 
                f"Delivery Address: {package.address}\n"
                f"Delivery Deadline: {package.deadline}\n"
                f"Delivery City: {package.city}\n"
                f"Delivery Zip Code: {package.zip_code}\n"
                f"Package Weight: {package.weight}lbs\n"
                f"Delivery Status: {package.status}\n"
                f"Delivery Time: {package.delivery_time}"
                )
    else:
        return "Package not found."

def get_total_mileage(trucks):
    # Retrieve total mileage
    return sum(truck.total_distance for truck in trucks) 

def print_package_status_in_time_window(package_list, start_time_str, end_time_str):
    # Convert input strings to datetime objects for comparison
    start_time = datetime.datetime.strptime(start_time_str, '%I:%M %p').time()
    end_time = datetime.datetime.strptime(end_time_str, '%I:%M %p').time()

    print(f"\nPackage status between {start_time_str} and {end_time_str}:")

    for package in package_list:
        # Only include packages that have a delivery time set
        if package.delivery_time and isinstance(package.delivery_time, datetime.datetime):
            package_time = package.delivery_time.time()
            if start_time <= package_time <= end_time:
                print(f"Package ID: {package.package_id}, Status: {package.status}, Delivery Time: {package.delivery_time.strftime('%I:%M %p')}")


def main_menu():
    # GUI main menu
    while True:
        print("\nDelivery System Menu:")
        print("1. Check Package Delivery Status")
        print("2. Check Total Mileage")
        print("3. Print Package Status in Time Window")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            package_id = input("Enter Package ID: ")
            if package_id.isdigit():
                status = get_delivery_status(int(package_id), hash_table)
                print(status)
            else:
                print("Invalid package ID. Please try again.")
        elif choice == '2':
            mileage = get_total_mileage(trucks)
            print(f"Total mileage traveled by all trucks: {mileage} miles")
        elif choice == '3':
            start_time_str = input("Enter the start time (HH:MM AM/PM): ")
            end_time_str = input("Enter the end time (HH:MM AM/PM): ")
            print_package_status_in_time_window(package_list, start_time_str, end_time_str)
        elif choice == '4':
            print("Exiting the delivery system.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run main menu function after deliveries
main_menu()