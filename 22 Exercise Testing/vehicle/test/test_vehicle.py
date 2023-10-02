from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(10.5, 120.5)

    def test_default_fuel_consumption_class_var(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialisation(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(120.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive_with_not_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_decrease_fuel(self):
        self.vehicle.drive(1)
        self.assertEqual(9.25, self.vehicle.fuel)

    def test_refuel_raises_exception_for_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_successfully_added_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(1)

        self.assertEqual(1, self.vehicle.fuel)

    def test__str__(self):
        self.assertEqual("The vehicle has 120.5 " +
                         "horse power with 10.5 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()
