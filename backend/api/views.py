from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.serializers import MovieSerializer
from movies.models import Movie


class MovieView(mixins.ListModelMixin, GenericViewSet):
    """
    Movie View
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = (DjangoFilterBackend,)
