class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # 'driver' or 'passenger'


class Ride:
    def __init__(self, driver, origin, destination, seats):
        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.passengers = []

    def add_passenger(self, passenger):
        if self.seats > 0:
            self.passengers.append(passenger)
            self.seats -= 1
            print(f"{passenger.username} added to the ride.")
        else:
            print("No available seats.")


class CarpoolSystem:
    def __init__(self):
        self.users = []
        self.rides = []

    def register_user(self, username, role):
        user = User(username, role)
        self.users.append(user)
        print(f"User {username} registered as {role}.")

    def create_ride(self, driver_name, origin, destination, seats):
        driver = self.find_user(driver_name)
        if driver and driver.role == 'driver':
            ride = Ride(driver, origin, destination, seats)
            self.rides.append(ride)
            print(f"Ride created from {origin} to {destination} by {driver_name}.")
        else:
            print("Driver not found or invalid role.")

    def request_ride(self, passenger_name, origin, destination):
        passenger = self.find_user(passenger_name)
        if passenger and passenger.role == 'passenger':
            matched = False
            for ride in self.rides:
                if ride.origin == origin and ride.destination == destination and ride.seats > 0:
                    ride.add_passenger(passenger)
                    matched = True
                    break
            if not matched:
                print("No matching ride found.")
        else:
            print("Passenger not found or invalid role.")

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


# Sample usage
if __name__ == "__main__":
    system = CarpoolSystem()

    system.register_user("alice", "driver")
    system.register_user("bob", "passenger")

    system.create_ride("alice", "CityA", "CityB", 3)

    system.request_ride("bob", "CityA", "CityB")
