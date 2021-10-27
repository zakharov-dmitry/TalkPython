from typing import Optional

from data.user import User


def user_count() -> int:
    return 73_847


def create_user(name: str, email: str, password: str) -> User:
    return User(name, email, "absdefgh")


def login_user(email: str, password: str) -> Optional[User]:
    if password == "absdefgh":
        return User("test user", email, "absdefgh")
    return None