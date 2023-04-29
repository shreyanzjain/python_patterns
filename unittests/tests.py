import unittest
from vehicle_info import VehicleInfo


class Tests(unittest.TestCase):

    def test_compute_non_electric_tax(self):
        car = VehicleInfo('BMW', False, 18000)
        self.assertEqual(car.compute_tax(), 900)

    def test_compute_electric_test(self):
        car = VehicleInfo('TATA', True, 12000)
        self.assertEqual(car.compute_tax(), 240)

    def test_compute_tax_raises_value_error(self):
        car = VehicleInfo('MASERATI', False, 75000)
        self.assertRaises(ValueError, car.compute_tax, -800)

    def test_compute_tax_exemption(self):
        car = VehicleInfo('DAZ', False, 50000)
        self.assertEqual(car.compute_tax(20000), 1500)

    def test_compute_tax_exemption_greater_than_price(self):
        car = VehicleInfo('TESLA', True, 80000)
        self.assertEqual(car.compute_tax(81000), 0)

    def test_can_lease(self):
        car = VehicleInfo('TOYOTA', False, 50000)
        self.assertTrue(car.can_lease(100000))

    def test_cannot_lease(self):
        car = VehicleInfo('LAMBORGHINI', False, 100000)
        self.assertFalse(car.can_lease(110000))


unittest.main()
