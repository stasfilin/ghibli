import json
import os

from django.conf import settings


class FixtureMixin(object):
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
