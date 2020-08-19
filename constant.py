import string


# idealy this should be dividede into 2 paths, for /generate and /password
PASSWORD_PATH = "/generate/password"

ALLOWED_CHARACTERS = string.ascii_letters + string.punctuation+string.digits


MIN_LENGTH = 8
