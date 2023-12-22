import csv
from package import Package


def loadPackageData(hash_table, file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                # Assuming the CSV columns are in the order:
                # PackageID, Address, Deadline, City, Zip Code, Weight, Status
                package_id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]
                deadline = row[5]
                weight = row[6]
                status = row[7]
                delivery_time = None  # No delivery time in csv

                # Create a Package object
                package = Package(package_id, address, city, state, zip_code, deadline, weight, status)

                # Insert the Package object into the HashTable
                hash_table.insert(package)

def loadDistanceData(file_path):
    distanceData = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row containing the address
        for row in csv_reader:
            # Convert each string in the row to a float, replace empty strings with a default value
            distances = [float(distance) if distance != '' else 0.0 for distance in row[1:]]
            distanceData.append(distances)
    return distanceData

def displayDistanceData(distanceData):
    print("Distance Matrix:")
    for row in distanceData:
        print(row)

def loadAddressData(file_path):
    addressData = []
    address_to_index = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for index, row in enumerate(csv_reader):
            address = row[0]  # Assuming the address is in the first column
            addressData.append(address)
            address_to_index[address] = index # Map address to index, for later search in DistanceData
    return address_to_index

def displayAddressData(addressData):
    print("Addresses:")
    for index, address in enumerate(addressData):
        print(f"{index}: {address}")