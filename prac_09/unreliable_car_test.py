from prac_09.unreliable_car import UnreliableCar


def main():
    """Testing UnreliableCar class"""
    car1 = UnreliableCar("Car 1", 100, 80)
    car1.drive(3)
    print(f"{car1.name} : {car1.drive(3)}km")
    print(car1)

    car2 = UnreliableCar("Car 2", 100, 10)
    car2.drive(14)
    print(f"{car2.name} : {car2.drive(14)}km")
    print(car2)


main()
