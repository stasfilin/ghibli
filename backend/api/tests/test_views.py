import requests_mock
from rest_framework.test import APITestCase

from movies.ghibli import Ghibli
from movies.models import Character, Movie
from utils.tests.testcase import FixtureMixin


class MovieViewTest(APITestCase, FixtureMixin):
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
