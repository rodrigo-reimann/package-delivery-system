from truck import Truck
from data_loader import loadPackageData, loadDistanceData, loadAddressData
from hash_table import HashTable
from logistics import perform_delivery_round


# Initialize hash table and load data
hash_table = HashTable(size=10)
loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/TSP-Routing/WGUPS-package copy.csv')

# Create an iterable package list
package_list = hash_table.get_all_packages()

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
print(f"\ntruck 1 current time: {trucks[0].current_time} truck 2 current time: {trucks[1].current_time}")
print("Total Mileage for Each Truck:")
for truck in trucks:
    print(f"Truck {truck.truck_id}: {truck.total_distance} miles")
print("")

# Load second rounds
for pkg in package_list:
    if pkg.package_id in [25, 32, 6]:
        trucks[0].add_package(pkg)

for pkg in package_list:
    if pkg.package_id in [28, 2, 33, 9, 27, 35]:
        trucks[1].add_package(pkg)  

# Second delivers
perform_delivery_round(trucks, distance_data, address_to_index, hash_table)
print(f"\ntruck 1 current time: {trucks[0].current_time} truck 2 current time: {trucks[1].current_time}")
print("Total Mileage for Each Truck:")
for truck in trucks:
    print(f"Truck {truck.truck_id}: {truck.total_distance} miles")
print("") 


# GUI
def get_delivery_status(package_id, hash_table):
    # Replace this with actual logic to retrieve status
    package = hash_table.lookup(package_id)
    if package:
        return f"Package ID: {package.package_id}, Status: {package.status}, Delivery Time: {package.delivery_time}"
    else:
        return "Package not found."

def get_total_mileage(trucks):
    # Replace this with actual logic to retrieve total mileage
    return sum(truck.total_distance for truck in trucks) 

def main_menu():
    while True:
        print("\nDelivery System Menu:")
        print("1. Check Package Delivery Status")
        print("2. Check Total Mileage")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

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
            print("Exiting the delivery system.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main_menu()