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

# Deliver packages
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