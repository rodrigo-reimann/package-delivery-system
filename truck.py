import datetime

class Truck:
    def __init__(self, truck_id, capacity=16, speed=18, start_location='HUB'):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.packages = []
        self.total_distance = 0.0
        self.current_location = start_location
        self.current_time = datetime.datetime.combine(datetime.date.today(), datetime.time(8, 0))  # Start at 8:00 AM

    def add_package(self, package):
        if len(self.packages) < self.capacity:
            self.packages.append(package)
            return True
        return False
        
    def is_full(self):
        return len(self.packages) >= self.capacity

    def remove_package(self, package_id):
        for package in self.packages:
            if package.package_id == package_id:
                self.packages.remove(package)
                return True
        return False
    
    def clear_delivered_packages(self):
        # Use a list comprehension to keep only the packages that have not been delivered
        self.packages = [package for package in self.packages if package.status != 'delivered']

    def travel_distance(self, distance):
        self.total_distance += distance # Update distance
        time_taken = datetime.timedelta(hours=distance / self.speed) # Calculate the time taken to travel the distance
        self.current_time += time_taken  # Update the current time

    def __str__(self):
        return f"Truck {self.truck_id}: {len(self.packages)} packages, Total Distance: {self.total_distance} miles"