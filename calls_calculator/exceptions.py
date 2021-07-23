

class NotFoundUserException(Exception):
    code = 'NOT_FOUND_USER'
    message = "The user {} you requested doesn't exist"
