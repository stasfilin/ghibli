import os
import json
import requests_mock
from django.conf import settings
from django.test import TestCase
from movies.ghibli import Ghibli
from movies.models import Movie, Character


class GhibliTest(TestCase):
    """
    Test Case for Ghibli Parser
    """

    def get_fixture(self, filename: str):
        f = os.path.join(
            settings.BASE_DIR.parent, "movies", "tests", "fixtures", filename
        )
        with open(f) as json_file:
            data = json.load(json_file)
            return data

    def test_get_films(self):
        with requests_mock.Mocker() as mocker:
            ghibli = Ghibli()
            mocker.register_uri(
                "GET", ghibli.base_url + "films", json=self.get_fixture("films.json"),
            )
            self.assertEqual(len(ghibli.get_films()), 20)

    def test_get_people(self):
        with requests_mock.Mocker() as mocker:
            ghibli = Ghibli()
            mocker.register_uri(
                "GET", ghibli.base_url + "people", json=self.get_fixture("people.json"),
            )
            self.assertEqual(len(ghibli.get_people()), 43)

    def test_sync(self):
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
