class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def fare(self):
        return self.mileage * 10

class Bus(Vehicle):
    def fare(self):
        # Calculate base fare from parent class
        base_fare = super().fare()
        # Add 10% for maintenance
        total_fare = base_fare + (base_fare * 0.1)
        return total_fare

# Example usage:
my_bus = Bus("School Bus", 100)
print(f"Total fare for {my_bus.name}: ${my_bus.fare():.2f}")