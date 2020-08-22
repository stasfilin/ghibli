from django.contrib import admin

from movies.models import Movie, Character


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Add Movie Model to Admintool
    """

    list_display = (
        "id",
        "title",
        "description",
        "director",
        "producer",
        "release_date",
    )

    list_filter = (
        "director",
        "producer",
        "release_date",
    )


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """
    Add Character Model to Admintool
    """

    list_display = (
        "id",
        "name",
    )

    list_filter = (
        "name",
        "movie",
    )
