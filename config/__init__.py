# Standard library
from os import environ

from decouple import config

# DATA SOURCE
MUSEUMS = config("MUSEUMS", cast=str)
LIBRARIES = config("LIBRARIES", cast=str)
CINEMAS = config("CINEMAS", cast=str)

DATA_SOURCES = [MUSEUMS, LIBRARIES, CINEMAS]

# Postgres
DATABASE_URL = environ["DATABASE_URL"]
