from django.test import TestCase
from django.contrib.auth import get_user_model

from taxi.models import Car, Manufacturer
from taxi.forms import DriverSearchForm, CarSearchForm, ManufacturerSearchForm


class DriverSearchFormTest(TestCase):
    def setUp(self) -> None:
        self.driver = get_user_model().objects.create_user(
            username="test",
            password="testpassword",
            first_name="Test",
            last_name="Test",
            license_number="ABC12345"
        )

    def test_driver_search_form_valid_data(self) -> None:
        form_data = {"username": "test"}
        form = DriverSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        drivers = get_user_model().objects.filter(
            username__icontains=form_data["username"]
        )
        self.assertEqual(list(drivers), [self.driver])


class CarSearchFormTest(TestCase):
    def setUp(self) -> None:
        self.manufacturer = Manufacturer.objects.create(
            name="test_manufacturer",
            country="test_country"
        )
        self.car = Car.objects.create(
            model="test_model",
            manufacturer=self.manufacturer
        )

    def test_car_search_form_valid_data(self) -> None:
        form_data = {"model": "test_model"}
        form = CarSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        cars = Car.objects.filter(
            model__icontains=form_data["model"]
        )
        self.assertEqual(list(cars), [self.car])


class ManufacturerSearchFormTest(TestCase):
    def setUp(self) -> None:
        self.manufacturer = Manufacturer.objects.create(
            name="test_manufacturer",
            country="test_country"
        )

    def test_manufacturer_search_form_valid_data(self) -> None:
        form_data = {"name": "test_manufacturer"}
        form = ManufacturerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        manufacturers = Manufacturer.objects.filter(
            name__icontains=form_data["name"]
        )
        self.assertEqual(list(manufacturers), [self.manufacturer])
