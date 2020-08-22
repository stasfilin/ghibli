from rest_framework import routers

from api.views import MovieView

urlpatterns = []
router = routers.SimpleRouter()

router.register(r"movies", MovieView)

urlpatterns.extend(router.urls)
