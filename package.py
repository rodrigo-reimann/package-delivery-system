class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, special_notes, status='at the hub'):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code     
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = None
        self.special_notes = special_notes

    # Update package status function
    def update_status(self, new_status, delivery_time=None):
        self.status = new_status
        self.delivery_time = delivery_time

    # Return print function
    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, Deadline: {self.deadline}, "
                f"City: {self.city}, Zip: {self.zip_code}, Weight: {self.weight}lbs, "
                f"Status: {self.status}, Delivery Time: {self.delivery_time}")

