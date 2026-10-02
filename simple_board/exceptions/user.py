class UserNotFoundException(Exception):
    pass


class UserExistingException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass


class SamePasswordException(Exception):
    pass
