import requests_mock
from django.test import TestCase

from movies.ghibli import Ghibli
from movies.models import Movie, Character
from utils.tests.testcase import FixtureMixin


class GhibliTest(TestCase, FixtureMixin):
    """
    Test Case for Ghibli Parser
    """

    def test_get_films(self) -> None:
        """
        Test get_films function
        """
        with requests_mock.Mocker() as mocker:
            ghibli = Ghibli()
            mocker.register_uri(
                "GET", ghibli.base_url + "films", json=self.get_fixture("films.json"),
            )
            self.assertEqual(len(ghibli.get_films()), 20)

    def test_get_people(self) -> None:
        """
        Test get_people function
        """
        with requests_mock.Mocker() as mocker:
            ghibli = Ghibli()
            mocker.register_uri(
                "GET", ghibli.base_url + "people", json=self.get_fixture("people.json"),
            )
            self.assertEqual(len(ghibli.get_people()), 43)

    def test_sync(self) -> None:
        """
        Test sync function
        """
        with requests_mock.Mocker() as mocker:
            ghibli = Ghibli()
            mocker.register_uri(
                "GET", ghibli.base_url + "people", json=self.get_fixture("people.json"),
            )
            mocker.register_uri(
                "GET", ghibli.base_url + "films", json=self.get_fixture("films.json"),
            )
            ghibli.sync()
            self.assertEqual(43, Character.objects.count())
            self.assertEqual(20, Movie.objects.count())
