class Vehicle:

    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):

    def fare(self):
        amount = super().fare()
        maintenance_charge = amount * 0.10
        return amount + maintenance_charge



bus = Bus("AIUB Bus", 40)

print("Bus Name:", bus.name)
print("Seating Capacity:", bus.seating_capacity)
print("Base Fare:", super(Bus, bus).fare())
print("Final Fare:", bus.fare())