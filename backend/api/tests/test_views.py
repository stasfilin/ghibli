import json
import os

import requests_mock
from django.conf import settings
from rest_framework.test import APITestCase

from movies.ghibli import Ghibli
from movies.models import Character, Movie


class MovieViewTest(APITestCase):
    def get_fixture(self, filename: str) -> None:
        """
        get fixture for mock test
        """
        f = os.path.join(
            settings.BASE_DIR.parent, "movies", "tests", "fixtures", filename
        )
        with open(f) as json_file:
            data = json.load(json_file)
            return data

    def test_movie_endpoint(self) -> None:
        """
        Test Movie Endpoint
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

            response = self.client.get("/api/movies/")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["count"], Movie.objects.count())
