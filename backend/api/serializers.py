from rest_framework import serializers

from movies.models import Movie, Character


class CharacterSerializer(serializers.ModelSerializer):
    """
    Character serializer
    """

    class Meta:
        model = Character
        fields = (
            "id",
            "name",
        )


class MovieSerializer(serializers.ModelSerializer):
    """
    Movie serializer.
    """

    people = CharacterSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "director",
            "producer",
            "release_date",
            "people",
        )
