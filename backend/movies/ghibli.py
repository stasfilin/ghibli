import requests
from django.db import IntegrityError

from movies.exceptions import EndpointException, FetchException
from movies.log import logger
from movies.models import Movie, Character


class Ghibli(requests.Session):
    """
    Ghibli Class
    """

    base_url = "https://ghibliapi.herokuapp.com/"
    endpoints = ["films", "people"]

    def fetch(self, endpoint: str) -> list:
        """
        Fetch data, check if endpoint allowed
        """
        if endpoint not in self.endpoints:
            raise EndpointException()
        response = self.get(self.base_url + endpoint)

        if response.status_code == 200:
            return response.json()
        raise FetchException()

    def get_films(self) -> list:
        """
        Get Films from Ghibli
        """
        return self.fetch("films")

    def get_people(self) -> list:
        """
        Get People from Ghibli
        """
        return self.fetch("people")

    def sync(self) -> None:
        """
        Sync data from Ghibli and push to Database
        """
        logger.info("Sync Ghibli data")
        films = self.get_films()

        movies_objects = {}

        for film in films:
            defaults = {
                "id": film.get("id"),
                "title": film.get("title"),
                "description": film.get("description"),
                "director": film.get("director"),
                "producer": film.get("producer"),
                "release_date": int(film.get("release_date", 0)),
            }
            try:
                movie, _ = Movie.objects.update_or_create(
                    id=film.get("id"), defaults=defaults
                )
                movies_objects[film.get("id")] = movie
            except IntegrityError as e:
                logger.exception(e)
        people = self.get_people()

        for person in people:
            defaults = {
                "name": person.get("name"),
            }
            person_films = [
                movies_objects.get(url.rsplit("films/", 1).pop())
                for url in person.get("films", [])
            ]
            try:
                character, _ = Character.objects.update_or_create(
                    id=person.get("id"), defaults=defaults
                )
                character.movie.add(*person_films)
                character.save()
            except IntegrityError as e:
                logger.exception(e)
