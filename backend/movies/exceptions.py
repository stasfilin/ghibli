class FetchException(Exception):
    message: str = "Error with fetching data from ghibli service"


class EndpointException(Exception):
    message: str = "Invalid endpoint, use only `films` and `people`"
