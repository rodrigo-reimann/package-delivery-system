from package import Package
from truck import Truck
from data_loader import loadPackageData, loadDistanceData, loadAddressData
from hash_table import HashTable
import datetime

# Greedy algorithm
def find_nearest(current_index, unvisited, distance_data, address_to_index):
    nearest = None
    min_distance = float('inf')
    for location in unvisited:
        index = address_to_index[location]
        distance = distance_data[current_index][index]
        if distance < min_distance:
            min_distance = distance
            nearest = location
    return nearest

# Get the package destinations in a truck
def get_package_destinations(truck):
    return set(package.address for package in truck.packages)

def deliver_packages(truck, distance_data, address_to_index, hash_table):
    current_location = 'HUB'  # Starting point
    unvisited = get_package_destinations(truck)  # Destinations to visit

    while unvisited:
        current_index = address_to_index[current_location]
        nearest = find_nearest(current_index, unvisited, distance_data, address_to_index)

        # Calculate the distance to the nearest location
        distance_to_nearest = distance_data[current_index][address_to_index[nearest]]
        if distance_to_nearest == 0.0 and current_index != address_to_index[nearest]:
            distance_to_nearest = distance_data[address_to_index[nearest]][current_index]

        # # Debug: Show current and next location, and the distance
        # print(f"Current location: {current_location}, Next location: {nearest}, Distance: {distance_to_nearest} miles")
        
        # Update the truck's total distance and current time for this leg of the journey
        truck.travel_distance(distance_to_nearest)

        
        # Now 'deliver' the packages (update their status)
        deliver_to(truck, nearest, hash_table, truck.current_time)
        
        # Remove the delivered destination from unvisited
        unvisited.remove(nearest)
        
        # Update the current location to the nearest for the next iteration
        current_location = nearest

    # After delivering all packages, return to the hub and update the distance
    return_to_hub(truck, distance_data, address_to_index)


def deliver_to(truck, destination, hash_table, delivery_time):
    for package in truck.packages:
        if package.address == destination:
            package.update_status('delivered', delivery_time)  # Update package status
            hash_table.update_package_status(package.package_id, 'delivered', delivery_time)
            # Debug print: Package delivery time
            print(f"Package {package.package_id} delivered at {delivery_time}")

# Check if all packages in the package hash table have been delivered
def all_packages_delivered(hash_table):
    for pkg in hash_table.get_all_packages():
        if pkg.status != 'delivered':
            return False
    return True

# Deliver, return to hub, and clear delivered packages
def perform_delivery_round(trucks, distance_data, address_to_index, hash_table):
    for truck in trucks:
        if truck.packages:
            deliver_packages(truck, distance_data, address_to_index, hash_table)
            return_to_hub(truck, distance_data, address_to_index)
            truck.clear_delivered_packages()

def return_to_hub(truck, distance_data, address_to_index):
    # Assume 'HUB' is at index 0 in distance matrix
    hub_index = address_to_index['HUB']
    current_location_index = address_to_index[truck.current_location]

    # Calculate the distance from the current location back to the hub
    distance_to_hub = distance_data[current_location_index][hub_index]

    # Update the total distance traveled by the truck
    truck.travel_distance(distance_to_hub)

    # Reset the current location to 'HUB'
    truck.current_location = 'HUB'


def main():
    # Initialize hash table and load data
    hash_table = HashTable(size=10)
    loadPackageData(hash_table, '/Users/rodrigo/Documents/repos/TSP-Routing/WGUPS-package copy.csv')

    # Create an iterable package list
    package_list = hash_table.get_all_packages()

    distance_data = loadDistanceData('/Users/rodrigo/Documents/repos/TSP-Routing/WGUPS-distance-matrix.csv')
    address_to_index = loadAddressData('/Users/rodrigo/Documents/repos/TSP-Routing/WGUPS-address.csv')

    # Initialize trucks
    trucks = [Truck(1), Truck(2)]





    # Load
    for pkg in package_list:
        if pkg.package_id in [13, 39, 14, 15, 16, 34, 19, 20, 21, 7, 29, 4, 40, 1, 30, 8]:
            trucks[0].add_package(pkg)

    for pkg in package_list:
        if pkg.package_id in [22, 26, 24, 18, 11, 23, 12, 31, 17, 36, 27, 35, 37, 5, 38, 3, 10]:
            trucks[1].add_package(pkg)

    '''DELIVER'''
    perform_delivery_round(trucks, distance_data, address_to_index, hash_table)
    print(f"\ntruck 1 current time: {trucks[0].current_time} truck 2 current time: {trucks[1].current_time}")

    print("Total Mileage for Each Truck:")
    for truck in trucks:
        print(f"Truck {truck.truck_id}: {truck.total_distance} miles")
    print("")





    # Load
    for pkg in package_list:
        if pkg.package_id in [25, 32]:
            trucks[0].add_package(pkg)

    # Load 
    for pkg in package_list:
        if pkg.package_id in [28, 2, 33, 9, 27, 35]:
            trucks[1].add_package(pkg)  

    '''DELIVER'''
    perform_delivery_round(trucks, distance_data, address_to_index, hash_table)
    print(f"\ntruck 1 current time: {trucks[0].current_time} truck 2 current time: {trucks[1].current_time}")

    print("Total Mileage for Each Truck:")
    for truck in trucks:
        print(f"Truck {truck.truck_id}: {truck.total_distance} miles")
    print("") 



if __name__ == "__main__":
    main()