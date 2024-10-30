class Plane:
    def __init__(self, name="", volume=0, passengers=0, race=0, destination="", total_flights = 0):
        self.__volume = volume
        self.__name = name
        self.__passengers = passengers
        self.race = race
        self.destination = destination
        self.__total_flights = total_flights

    def __str__(self):
        return (f"STRAbout Plane:\n"
                f" (Name: {self.get_name()})\n"
                f" (Volume: {self.get_volume()})\n"
                f" (Number of passengers: {self.get_passengers()})\n"
                f" (Race№: {self.race})\n"
                f" (Destination: {self.destination})\n"
                f" (Total Flights: {self.get_total_flights()})\n")

    def __repr__(self):
        return (f"Plane(name='{self.__name}', volume={self.__volume}, "
                f"passengers={self.__passengers}, race={self.race}, "
                f"destination='{self.destination}', total_flights={self.__total_flights})")

    def get_volume(self):
        return self.__volume

    def get_name(self):
        return self.__name

    def get_passengers(self):
        return self.__passengers

    def get_total_flights(self):
        return self.__total_flights

    def set_volume(self, volume):
        if volume > 0:
            self.__volume = volume
        else:
            print("Volume should be greater than zero.")

    def set_name(self, name):
        if name:
            self.__name = name
        else:
            print("Name cannot be empty.")

    def set_passengers(self, passengers):
        if passengers >= 0:
            self.__passengers = passengers
        else:
            print("Number of passengers cannot be negative.")

    def set_total_flights(self, additional_flights):
        self.__total_flights += additional_flights

    def max_flight(planes):
        return max(planes, key=lambda plane: plane.get_total_flights())

    def __del__(self):
        print("Object has been destroyed.")

def main():
    plane1 = Plane("AH-20", 12, 200, 958425, "Kyiv", 100)
    plane2 = Plane("Hmara", 25, 222, 654523, "Lviv", 200)
    plane3 = Plane("Condor", 65, 233, 789654, "Poltava", 300)

    plane1.set_total_flights(200)
    plane2.set_total_flights(300)
    plane3.set_total_flights(400)

    print(plane1)
    print(plane2)
    print(plane3)

    plane1.set_name("Mriya")
    plane1.set_volume(30)
    plane1.set_passengers(180)
    print("\nAfter using setters:")
    print(repr(plane1))

    plane1.set_total_flights(700)

    max_flights_plane = Plane.max_flight([plane1, plane2, plane3])
    print("\nPlane with the most flights:")
    print(max_flights_plane)

if __name__ == "__main__":
    main()
