import uuid

from django.core.exceptions import ValidationError
from django.test import TestCase

from movies.models import Movie, Character


class MovieModel(TestCase):
    """
    Test Case for Movie Model
    """

    def test_create_movie_with_valid_data(self) -> None:
        """
        Test Movie for creating new movie with valid data
        """
        data = {
            "id": uuid.uuid4(),
            "title": "Test Movie",
            "description": "Test description",
            "director": "Stanislav Filin",
            "producer": "Stanislav Filin",
            "release_date": 2020,
        }

        movie, _ = Movie.objects.get_or_create(**data)

        self.assertEqual(movie.id, data.get("id"))
        self.assertEqual(movie.title, data.get("title"))

    def test_create_movie_with_invalid_data(self) -> None:
        """
        Test Movie for creating new movie with invalid data
        """
        data = {
            "id": "invalid_id",
            "title": "Test Movie",
            "description": "Test description",
            "director": "Stanislav Filin",
            "producer": "Stanislav Filin",
            "release_date": 2020,
        }
        with self.assertRaises(ValidationError):
            movie = Movie(**data).save()

            self.assertEqual(movie, None)


class CharacterModel(TestCase):
    """
    Test Case for Character Model
    """

    def test_create_movie_with_valid_data(self) -> None:
        """
        Test Character for creating new people with valid data
        """
        data = {"id": uuid.uuid4(), "name": "Stanislav Filin"}

        movie, _ = Character.objects.get_or_create(**data)

        self.assertEqual(movie.id, data.get("id"))
        self.assertEqual(movie.name, data.get("name"))

    def test_create_movie_with_invalid_data(self) -> None:
        """
        Test Character for creating new people with invalid data
        """
        data = {"id": "invalid_id", "name": "Stanislav Filin"}
        with self.assertRaises(ValidationError):
            movie = Character(**data).save()

            self.assertEqual(movie, None)
