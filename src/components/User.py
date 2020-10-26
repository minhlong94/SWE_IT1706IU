class User:
    """
    Class User is where we store user's username and password.

    User is the manager for the system.

    Args:
        username (str)
        password (str)

    Attributes:
        username: where we store user's username.
        password: where we store user's password.
    """

    def __init__(self, username, password):
        if username is None:
            self.username = "admin"
        elif not isinstance(username, str):
            raise TypeError("'username' must be a string!")
        else:
            self.username = username

        if password is None:
            self.password = "admin"
        elif not isinstance(password, str):
            raise TypeError("'password' must be a string!")
        else:
            self.password = password
